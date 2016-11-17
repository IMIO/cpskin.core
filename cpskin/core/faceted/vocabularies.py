# -*- coding: utf-8 -*-
"""
cpskin.core
-----------

Created by mpeeters
:copyright: (c) 2015 by Affinitic SPRL
:license: GPL, see LICENCE.txt for more details.
"""

from eea.facetednavigation.layout.layout import FacetedLayout
from zope.schema.vocabulary import SimpleVocabulary


class FacetedLayoutVocabularyFactory(object):

    def __call__(self, context):
        faceted_layout = FacetedLayout(context)
        terms = [SimpleVocabulary.createTerm(l[0], l[0], l[1])
                 for l in faceted_layout.layouts]
        return SimpleVocabulary(terms)


FacetedLayoutVocabulary = FacetedLayoutVocabularyFactory()
