# -*- coding: utf-8 -*-
from plone.indexer.interfaces import IIndexer
from OFS.interfaces import IItem
from Products.ZCatalog.interfaces import IZCatalog

try:
    from plone.dexterity.utils import safe_utf8
except ImportError:
    # Compatibility with Plone 4.3.2 / plone.dexterity 2.1.3
    from cpskin.core.utils import safe_utf8

from zope.interface import implements
from zope.component import adapts
import logging
logger = logging.getLogger('cpskin.core.indexer')


class BaseTagIndexer(object):
    """Index the specified tag
    """
    implements(IIndexer)
    adapts(IItem, IZCatalog)

    def __init__(self, context, catalog):
        self.context = context
        self.catalog = catalog

    def _getFieldContent(self, field):
        tags = getattr(self.context, field, None)
        if not tags:
            return ""
        encodedTags = tuple(safe_utf8(s) for s in tags)
        return encodedTags


class StandardTagIndexer(BaseTagIndexer):

    def __call__(self):
        return self._getFieldContent('standardTags')


class IAmTagIndexer(BaseTagIndexer):

    def __call__(self):
        return self._getFieldContent('iamTags')


class ISearchTagIndexer(BaseTagIndexer):

    def __call__(self):
        return self._getFieldContent('isearchTags')


class HiddenTagIndexer(BaseTagIndexer):

    def __call__(self):
        return self._getFieldContent('hiddenTags')


from plone.app.querystring.interfaces import IQuerystringRegistryReader
from plone.app.querystring.registryreader import QuerystringRegistryReader
from zope.schema.interfaces import IVocabularyFactory
from zope.component import queryUtility
from operator import attrgetter
from zope.i18n import translate
from zope.i18nmessageid import Message
from zope.component import adapts
from plone.registry.interfaces import IRegistry


class CpskinQuerystringRegistryReader(QuerystringRegistryReader):
    """Adapts a registry object to parse the querystring data."""

    def getVocabularyValues(self, values):
        """Get all vocabulary values if a vocabulary is defined"""
        values = super(CpskinQuerystringRegistryReader, self).getVocabularyValues(values)
        cpskin_indexes = ['hiddenTags', 'isearchTags', 'iamTags']
        values.get(self.prefix + '.field')
        for cpskin_index in cpskin_indexes:
            index = values.get(self.prefix + '.field').get(cpskin_index, None)
            for value in index.values():
                if isinstance(value, dict):
                    i18n_value = dict((k.encode('utf8'), v) for k, v in value.items())
                    values.get(self.prefix + '.field').get(cpskin_index)['values'] = i18n_value
        return values
