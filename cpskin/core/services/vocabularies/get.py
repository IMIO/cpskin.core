# -*- coding: utf-8 -*-

from plone.restapi.services.vocabularies.get import VocabulariesGet as VocGet
from zope.interface import implementer
from zope.publisher.interfaces import IPublishTraverse
from zope.security import checkPermission


@implementer(IPublishTraverse)
class VocabulariesGet(VocGet):
    def reply(self):
        if "plone.app.vocabularies.Users" in self.params:
            if not checkPermission("cpskin.accessrestapiusersvocabulary", self.context):
                self.request.response.setStatus(403)
                return
        return super(VocabulariesGet, self).reply()
