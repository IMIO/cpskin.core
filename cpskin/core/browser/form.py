# -*- coding: utf-8 -*-
from cpskin.core.utils import has_lat_lng
from cpskin.core.utils import set_coord
from cpskin.locales import CPSkinMessageFactory as _
from plone import api
from plone.directives import form
from z3c.form import button
from zope import schema

import logging


logger = logging.getLogger('cpskin.core.encode_lat_lng')


class IGeoForm(form.Schema):
    """ Define form fields """

    content_types = schema.List(
        title=_(u'Content type'),
        description=_(
            u'Which content type should be set latitude and longitude'),
        value_type=schema.Choice(
            title=_(u'Content types'),
            vocabulary='cpskin.core.vocabularies.geo_types',
        ),
        required=False,
    )


class GeoForm(form.SchemaForm):

    schema = IGeoForm
    ignoreContext = True

    label = u"What's object do you want to update ?"
    description = u'This script will update latitude and longitude for objects \
                    selected'

    @button.buttonAndHandler(u'Ok')
    def handleApply(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        # Do something with valid data here

        # Set status on this form page (this status message
        # is not bind to the session and does not go thru redirects)
        results = []
        if 'content_types' not in data.keys():
            pass
        else:
            for portal_type in data['content_types']:
                list_updated = set_lat_lng(portal_type, self.request)
                results.extend(list_updated)
                message = '{1} {0} are updated'.format(
                    portal_type, len(list_updated))
                api.portal.show_message(message=message, request=self.request)
        # self.status = "\n".join(results)

    @button.buttonAndHandler(u"Cancel")
    def handleCancel(self, action):
        """User cancelled. Redirect back to the front page.
        """


def set_lat_lng(portal_type, request):
    catalog = api.portal.get_tool('portal_catalog')
    query = {}
    query['portal_type'] = portal_type
    brains = catalog(query)
    nbre = len(brains)
    results = []
    i = 0
    for brain in brains:
        obj = brain.getObject()
        i += 1
        if not has_lat_lng(obj):
            message = set_coord(obj, request)
            if message:
                results.append(message)
        logger.info('{0}/{1}'.format(i, nbre))
    return results
