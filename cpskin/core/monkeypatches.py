# -*- coding: utf-8 -*-

from Products.PluginIndexes.KeywordIndex.KeywordIndex import KeywordIndex
from datetime import datetime
from plone import api
from plone.formwidget.datetime.z3cform.widget import DateWidget
from plone.formwidget.datetime.z3cform.widget import DatetimeWidget


def afterMemberAdd(self, member, id, password, properties):
    """
    Called by portal_registration.addMember() after a member
    has been added successfully
    """
    # if this is an auto registration, not an administrator action
    groups_tool = api.portal.get_tool('portal_groups')
    group_id = 'citizens'
    if group_id not in groups_tool.getGroupIds():
        groups_tool.addGroup(group_id)
    if api.user.is_anonymous():
        api.group.add_user(groupname='citizens', user=member)


def keyword_apply_index(self, request, resultset=None):
    indexes = ('standardTags', 'iamTags', 'isearchTags', 'hiddenTags')
    for key in [k for k in indexes if k in request and self.id == k]:
        request_key = request.get(key, {})
        if hasattr(request_key, 'query'):
            query_value = request_key.get('query')
            if isinstance(query_value, unicode):
                request[key]['query'] = query_value.encode('utf8')
        elif getattr(request_key, 'get', None):
            query_value = request_key.get('query')
            if isinstance(query_value, (list, tuple)):
                values = []
                for value in query_value:
                    if isinstance(value, unicode):
                        values.append(value.encode('utf8'))
                    else:
                        values.append(value)
                request[key]['query'] = values
        else:
            if isinstance(request_key, unicode):
                request[key] = request_key.encode('utf8')
    return super(KeywordIndex, self)._apply_index(request, resultset)


def date_widget_update(self):
    now = datetime.now()
    min_value = -10
    max_value = 10
    if self.field.min:
        min_value = self.field.min.year - now.year
    if self.field.max:
        max_value = self.field.max.year - now.year + 1
    self.years_range = (min_value, max_value)
    super(DateWidget, self).update()


def datetime_widget_update(self):
    now = datetime.now()
    min_value = -10
    max_value = 10
    if self.field.min:
        min_value = self.field.min.year - now.year
    if self.field.max:
        max_value = self.field.max.year - now.year + 1
    self.years_range = (min_value, max_value)
    super(DatetimeWidget, self).update()
