# -*- coding: utf-8 -*-
import operator

from zope.component import getUtility

from plone.app.layout.viewlets import common
from plone.registry.interfaces import IRegistry

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class SocialViewlet(common.ViewletBase):

    index = ViewPageTemplateFile('social.pt')

    def getSocialLinks(self):
        registry = getUtility(IRegistry)
        links_dict = registry['cpskin.core.socialviewlet']
        links_ordered = sorted(links_dict.itervalues(), key=operator.itemgetter(0))
        # Fix bad encoded cpskin.core.socialviewlet registry :
        links_ordered = [li for li in links_ordered if len(li) == 3]
        return links_ordered
