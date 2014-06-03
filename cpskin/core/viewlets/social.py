# -*- coding: utf-8 -*-
from plone.app.layout.viewlets import common

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class SocialViewlet(common.ViewletBase):

    index = ViewPageTemplateFile('social.pt')
