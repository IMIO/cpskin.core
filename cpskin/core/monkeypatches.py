# -*- coding: utf-8 -*-
from plone import api


def afterMemberAdd(self, member, id, password, properties):
    """
    Called by portal_registration.addMember() after a member
    has been added successfully
    """
    # if this is an auto registration, not an administrator action
    if api.user.is_anonymous():
        api.group.add_user(groupname='citizens', user=member)
