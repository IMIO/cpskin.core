# -*- coding: utf-8 -*-

from Products.Five import BrowserView
from plone import api
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import getUtility
from zope.schema import getFields
from zope.schema.interfaces import IVocabularyFactory


class CommonView(BrowserView):

    def see_categories(self, container):
        result = True
        taxonomy_field = getattr(container, 'taxonomy_category', '')
        if not taxonomy_field:
            result = False
        return result

    def get_categories(self, container, obj):
        portal_type = obj.portal_type
        schema = getUtility(IDexterityFTI, name=portal_type).lookupSchema()
        fields = getFields(schema)
        taxonomy_field = getattr(container, 'taxonomy_category', '')
        if taxonomy_field not in fields.keys():
            return ''

        field = fields[taxonomy_field]
        vocabulary_name = field.value_type.vocabularyName
        factory = getUtility(IVocabularyFactory, vocabulary_name)
        vocabulary = factory(api.portal.get())
        tokens = getattr(obj, taxonomy_field, '')
        if not tokens:
            return ''
        categories = []
        for token in tokens:
            cat = vocabulary.inv_data.get(token)
            categories.append(cat[1:])
        categories.sort()
        return ', '.join(categories)
