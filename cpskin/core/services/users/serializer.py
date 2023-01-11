# -*- coding: utf-8 -*-
from cpskin.core.interfaces import ICPSkinCoreLayer
from plone.restapi.serializer.user import SerializeUserToJson
from plone.restapi.interfaces import ISerializeToJson
from Products.CMFCore.interfaces._tools import IMemberData
from zope.component import adapter
from zope.interface import implementer
from plone.restapi.serializer.converters import json_compatible


@implementer(ISerializeToJson)
@adapter(IMemberData, ICPSkinCoreLayer)
class UsersSerializer(SerializeUserToJson):
    """ Add last_login_time, login_time when getting restapi users """

    def __call__(self):
        self.context.getProperty("last_login_time")
        data = super(UsersSerializer, self).__call__()
        json_compatible(self.context.getProperty("last_login_time"))
        data["last_login_time"] = json_compatible(self.context.getProperty("last_login_time"))
        data["login_time"] = json_compatible(self.context.getProperty("login_time"))
        return data
