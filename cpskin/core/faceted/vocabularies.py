# -*- coding: utf-8 -*-
"""
cpskin.core
-----------

Created by mpeeters
:copyright: (c) 2015 by Affinitic SPRL
:license: GPL, see LICENCE.txt for more details.
"""

from eea.facetednavigation.layout.layout import FacetedLayout
from zope.i18n import translate
from zope.schema.vocabulary import SimpleVocabulary
from zope.globalrequest import getRequest

from cpskin.locales import CPSkinMessageFactory as _


class FacetedLayoutVocabularyFactory(object):

    def __call__(self, context):
        faceted_layout = FacetedLayout(context)
        request = getattr(context, 'REQUEST', getRequest())
        terms = [
            SimpleVocabulary.createTerm(
                l[0],
                l[0],
                translate(_(l[1]), context=request),
            ) for l in faceted_layout.layouts]
        return SimpleVocabulary(terms)


FacetedLayoutVocabulary = FacetedLayoutVocabularyFactory()
