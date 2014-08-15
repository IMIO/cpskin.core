# -*- coding: utf-8 -*-
from Products.PluginIndexes.KeywordIndex.KeywordIndex import KeywordIndex
from plone import api


def afterMemberAdd(self, member, id, password, properties):
    """
    Called by portal_registration.addMember() after a member
    has been added successfully
    """
    # if this is an auto registration, not an administrator action
    if api.user.is_anonymous():
        api.group.add_user(groupname='citizens', user=member)


def keyword_apply_index(self, request, resultset=None):
    indexes = ('standardTags', 'iamTags', 'isearchTags', 'hiddenTags')
    for key in [k for k in indexes if k in request and self.id == k]:
        query_value = request[key]['query']
        if isinstance(query_value, unicode):
            request[key]['query'] = query_value.encode('utf8')
    return super(KeywordIndex, self)._apply_index(request, resultset)
