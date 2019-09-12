# -*- coding: utf-8 -*-
from Acquisition import aq_base
from collective import dexteritytextindexer
from OFS.interfaces import IItem
from plone.app.contenttypes.indexers import SearchableText_document
from plone.app.contenttypes.indexers import SearchableText_file
from plone.app.contenttypes.indexers import SearchableText_link
from plone.app.contenttypes.interfaces import IDocument
from plone.app.contenttypes.interfaces import IFile
from plone.app.contenttypes.interfaces import ILink
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


class DocumentExtender(object):
    adapts(IDocument)
    implements(dexteritytextindexer.IDynamicTextIndexExtender)

    def __init__(self, context):
        self.context = context

    def __call__(self):
        return SearchableText_document(self.context)()


class LinkExtender(object):
    adapts(ILink)
    implements(dexteritytextindexer.IDynamicTextIndexExtender)

    def __init__(self, context):
        self.context = context

    def __call__(self):
        return SearchableText_link(self.context)()


class FileExtender(object):
    adapts(IFile)
    implements(dexteritytextindexer.IDynamicTextIndexExtender)

    def __init__(self, context):
        self.context = context

    def __call__(self):
        return SearchableText_file(self.context)()


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
