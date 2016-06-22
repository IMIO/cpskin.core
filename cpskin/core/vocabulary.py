# -*- coding: utf-8 -*-
from binascii import b2a_qp
from zope.component import getUtility
from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary
from zope.site.hooks import getSite

from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import safe_unicode
from plone import api
from zope.component.interface import nameToInterface
from plone.dexterity.interfaces import IDexterityFTI
from zope.schema import getFieldsInOrder


class BaseTagsVocabulary(object):
    """Vocabulary factory listing all catalog keywords from specified tags"""
    implements(IVocabularyFactory)
    indexName = ''

    def __call__(self, context, query=None):
        site = getSite()
        self.catalog = getToolByName(site, "portal_catalog", None)
        if self.catalog is None:
            return SimpleVocabulary([])
        if not self.indexName in self.catalog._catalog.indexes.keys():
            return SimpleVocabulary([])
        index = self.catalog._catalog.getIndex(self.indexName)

        def safe_encode(term):
            if isinstance(term, unicode):
                # no need to use portal encoding for transitional encoding from
                # unicode to ascii. utf-8 should be fine.
                term = term.encode('utf-8')
            return term

        # Vocabulary term tokens *must* be 7 bit values, titles *must* be
        # unicode
        items = [
            SimpleTerm(safe_unicode(i), b2a_qp(
                safe_encode(i)), safe_unicode(i))
            for i in index._index
            if query is None or safe_encode(query) in safe_encode(i)
        ]
        return SimpleVocabulary(items)


class IStandardTagsVocabulary(BaseTagsVocabulary):
    """Vocabulary factory listing all catalog keywords from standard tags"""
    indexName = 'standardTags'


class IAmTagsVocabulary(BaseTagsVocabulary):
    """Vocabulary factory listing all catalog keywords from I am tags"""
    indexName = 'iamTags'


class ISearchTagsVocabulary(BaseTagsVocabulary):
    """Vocabulary factory listing all catalog keywords from I search tags"""
    indexName = 'isearchTags'


class HiddenTagsVocabulary(BaseTagsVocabulary):
    """Vocabulary factory listing all catalog keywords from hidden tags"""
    indexName = 'hiddenTags'

    def __call__(self, context, query=None):
        voc = super(HiddenTagsVocabulary, self).__call__(context, query)
        # Add a-la-une term if it does not already exist, aka still not used
        # for any document
        if u'a-la-une' not in voc.by_token:
            simpleTerms = [term for term in voc]
            simpleTerms.append(SimpleTerm(u'a-la-une', title=u'A la une'))
            voc = SimpleVocabulary(simpleTerms)
        if u'homepage' not in voc.by_token:
            simpleTerms = [term for term in voc]
            simpleTerms.append(SimpleTerm(u'homepage', title=u'homepage'))
            voc = SimpleVocabulary(simpleTerms)
        return voc


IStandardTagsVocabularyFactory = IStandardTagsVocabulary()
IAmTagsVocabularyFactory = IAmTagsVocabulary()
ISearchTagsVocabularyFactory = ISearchTagsVocabulary()
HiddenTagsVocabularyFactory = HiddenTagsVocabulary()


class ContactFieldsFactory(object):
    """Vocabulary factory listing all fields from contacts"""
    implements(IVocabularyFactory)
    indexName = ''

    def __call__(self, context, query=None):
        results = []
        exclude = ['im_handle', 'use_parent_address']
        exclude_behaviors = ['plone.app.content.interfaces.INameFromTitle']

        portal_types = api.portal.get_tool('portal_types')
        contact_portal_types = ['person', 'organization']
        for contact_portal_types in contact_portal_types:
            schema = getUtility(
                IDexterityFTI, name=contact_portal_types).lookupSchema()
            for name, field in getFieldsInOrder(schema):
                if name not in exclude:
                    results.append((name, field.title))

            portal_type = getattr(portal_types, contact_portal_types)
            behaviors = list(set(portal_type.behaviors))

        behaviors = set(behaviors)
        for behavior in behaviors:
            if behavior not in exclude_behaviors:
                try:
                    interface = nameToInterface(context, behavior)
                    for name, field in getFieldsInOrder(interface):
                        if name not in exclude:
                            results.append((name, field.title))
                except:
                    pass
        items = [
            SimpleTerm(i, i, j)
            for i, j in results if j
        ]
        return SimpleVocabulary(items)

ContactFieldsVocabularyFactory = ContactFieldsFactory()
