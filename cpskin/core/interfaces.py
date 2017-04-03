# -*- coding: utf-8 -*-
from cpskin.locales import CPSkinMessageFactory as _
from zope import schema
from zope.interface import Interface


class ICPSkinCoreLayer(Interface):
    """
    Marker interface that defines a ZTK browser layer.
    """


class ICPSkinCoreWithMembersLayer(Interface):
    """
    Marker interface that defines a ZTK browser layer.
    """


class IBannerActivated(Interface):
    """
    Marker interface to enable / disable banner viewlet
    """


class ILocalBannerActivated(Interface):
    """
    Marker interface to enable / disable banner viewlet
    """


class IMediaActivated(Interface):
    """
    Marker interface to enable / disable (multi)media viewlet
    """


class IFolderViewSelectedContent(Interface):
    """
    Marker interface to add / remove content to / from folder view
    """


class IFolderViewWithBigImages(Interface):
    """
    Marker interface to use big images on folder view
    """


class ICPSkinSettings(Interface):
    """
    Settings for CPSkin
    """
    load_page_menu = schema.Bool(
        title=_(u'Load page menu'),
        description=_(u'Is level 1 menu load page at click?'),
        required=False,
        default=False
    )

    sub_menu_persistence = schema.Bool(
        title=_(u'Sub menu persistence'),
        description=_(u'Is level 2 menu persist?'),
        required=False,
        default=True
    )

    auto_play_slider = schema.Bool(
        title=_(u'Auto play slider'),
        description=_(u'Is the front page slider automatically play?'),
        required=False,
        default=True
    )

    slider_timer = schema.Int(
        title=_(u'Slider timer'),
        description=_(u'Number of milliseconds between each transition.'),
        required=False,
        default=5000
    )

    city_name = schema.TextLine(
        title=_(u'City name'),
        description=_(u'Name of city is used in some templates.'),
        required=True,
        default=u'City name'
    )

    slider_type = schema.Choice(
        title=_(u'Slider type'),
        description=_(u'Slider type (slider_view / slider_view_vertical).'),
        required=True,
        values=[_(u'slider_view'), _(u'slider_view_vertical')],
        default=u'slider_view'
    )


class IVideoCollection(Interface):
    """
    Marker interface for video collection used to viewlet multimedia
    """


class IAlbumCollection(Interface):
    """
    Marker interface for album collection used to viewlet multimedia
    """
