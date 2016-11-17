# -*- coding: utf-8 -*-
from Acquisition import aq_get
from binascii import b2a_qp
from collective.geo.behaviour.interfaces import ICoordinates
from plone import api
from plone.dexterity.interfaces import IDexterityFTI
from plone.supermodel.interfaces import FIELDSETS_KEY
from plone.supermodel.utils import mergedTaggedValueList
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import safe_unicode
from zope.component import getUtility
from zope.component.interface import nameToInterface
from zope.i18n import translate
from zope.interface import implements
from zope.schema import getFieldsInOrder
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


class BaseTagsVocabulary(object):
    """Vocabulary factory listing all catalog keywords from specified tags"""
    implements(IVocabularyFactory)
    indexName = ''

    def __call__(self, context, query=None):
        site = api.portal.get()
        self.catalog = getToolByName(site, 'portal_catalog', None)
        if self.catalog is None:
            return SimpleVocabulary([])
        if self.indexName not in self.catalog._catalog.indexes.keys():
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
        for contact_portal_type in contact_portal_types:
            schema = getUtility(
                IDexterityFTI, name=contact_portal_type).lookupSchema()
            fieldsets = mergedTaggedValueList(schema, FIELDSETS_KEY)
            for name, field in getFieldsInOrder(schema):
                if name not in exclude:
                    visible_name = u"{0}: {1}".format(
                        contact_portal_type, field.title)
                    results.append((name, visible_name))

            portal_type = getattr(portal_types, contact_portal_type)
            behaviors = list(set(portal_type.behaviors))

        behaviors = set(behaviors)
        for behavior in behaviors:
            if behavior not in exclude_behaviors:
                try:
                    # not able to get fields from IDirectoryContactDetails
                    # with nameToInterface(context, behavior)
                    if behavior == 'cpskin.core.behaviors.directorycontact.IDirectoryContactDetails':  # noqa
                        from cpskin.core.behaviors.directorycontact import (
                            IDirectoryContactDetails)
                        interface = IDirectoryContactDetails
                    else:
                        interface = nameToInterface(context, behavior)
                    fieldsets = mergedTaggedValueList(interface, FIELDSETS_KEY)
                    for name, field in getFieldsInOrder(interface):
                        if name not in exclude:
                            if not fieldsets:
                                visible_name = field.title
                            else:
                                fieldset = [
                                    fieldset for fieldset in fieldsets if name in fieldset.fields  # noqa
                                ][0]
                                visible_name = u"{0}: {1}".format(
                                    fieldset.label, field.title)
                            results.append((name, visible_name))
                except:
                    pass
        items = [
            SimpleTerm(i, i, j)
            for i, j in results if j
        ]
        return SimpleVocabulary(items)


ContactFieldsVocabularyFactory = ContactFieldsFactory()


class GeoTypesFactory(object):
    implements(IVocabularyFactory)

    def __call__(self, context, query=None):
        portal_types = api.portal.get_tool('portal_types')
        request = aq_get(portal_types, 'REQUEST', None)
        if portal_types is None:
            return SimpleVocabulary([])

        items = []

        for k, v in portal_types.items():
            behaviors = getattr(v, 'behaviors', [])
            if ICoordinates.__identifier__ in behaviors:
                items.append(
                        (k, translate(v.Title(), context=request))
                )
        items.sort(key=lambda x: x[1])
        items = [SimpleTerm(i[0], i[0], i[1]) for i in items]
        return SimpleVocabulary(items)


GeoTypesVocabularyFactory = GeoTypesFactory()
