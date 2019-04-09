# -*- coding: utf-8 -*-
from Acquisition import aq_base
from OFS.interfaces import IItem
from plone.indexer.interfaces import IIndexer
from Products.ZCatalog.interfaces import IZCatalog
from zope.component import adapts
from zope.interface import implements

import logging


try:
    from plone.dexterity.utils import safe_utf8
except ImportError:
    # Compatibility with Plone 4.3.2 / plone.dexterity 2.1.3
    from cpskin.core.utils import safe_utf8

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
        tags = getattr(aq_base(self.context), field, None)
        if not tags:
            raise AttributeError
        if field not in self.context.contentIds():
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
