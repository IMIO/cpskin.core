# -*- coding: utf-8 -*-
from cpskin.locales import CPSkinMessageFactory as _
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from plone.namedfile import field as namedfile
from zope.interface import provider

from zope.component import adapter
from zope.interface import implementer
from plone.event.interfaces import IEvent


@provider(IFormFieldProvider)
class ICpskinEventViewSettings(model.Schema):
    model.fieldset(
        'eventview',
        label=_(
            u'Event view'),
        fields=(
            'image_banner',
        ),
    )

    image_banner = namedfile.NamedBlobImage(
        title=_(u'label_bannerimage', default=u'Banner image'),
        description=_(
            u'help_bannerimage',
            default=u'Image used as banner replacement when viewing this event'
        ),
        required=False,
    )


@implementer(ICpskinEventViewSettings)
@adapter(IEvent)
class CpskinEventViewSettings(object):

    def __init__(self, context):
        self.context = context
