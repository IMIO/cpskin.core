# -*- coding: utf-8 -*-
from cpskin.locales import CPSkinMessageFactory as _
from plone.app.contenttypes.interfaces import IPloneAppContenttypesLayer
from sc.social.like.interfaces import ISocialLikeLayer
from zope import schema
from zope.interface import Interface


class ICPSkinCoreLayer(ISocialLikeLayer, IPloneAppContenttypesLayer):
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


class IElectedContentForTopMenu(Interface):
    """
    Marker interface to select content for action top menu
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

    contents_in_action_menu = schema.Tuple(
        title=_(u'Content to show in special action menu (top)'),
        description=_(u'Please select which contents should be taken to this menu.'),  # noqa
        required=False,
        value_type=schema.Choice(
            vocabulary=u'cpskin.core.vocabularies.action_menu_eligible'
        )
    )

    show_leadimage_in_action_menu = schema.Bool(
        title=_(u'Show leadimage in action menu'),
        description=_(u'Show leadimage (if any) in the top action menu with content selected in the field before.'),  # noqa
        required=False,
        default=False
    )

    show_slogan = schema.Bool(
        title=_(u'Show slogan with banner'),
        description=_(u'Show banner title and description as homepage slogan.'),  # noqa
        required=False,
        default=False
    )

    show_portlets_in_right_actions_panel = schema.Bool(
        title=_(u'Show (right) portlets in right actions panel'),
        description=_(u'Show (right) portlets (if any) in right actions panel after related contents.'),  # noqa
        required=False,
        default=False
    )

    media_viewlet_visible_albums = schema.Int(
        title=_(u'Viewlet media : Visible albums'),
        description=_(u'Number of visible albums on media viewlet.'),
        required=False,
        min=0,
        default=5
    )

    media_viewlet_visible_videos = schema.Int(
        title=_(u'Viewlet media : Visible videos'),
        description=_(u'Number of visible videos on media viewlet.'),
        required=False,
        min=0,
        default=2
    )

    show_description_on_themes = schema.Bool(
        title=_(u'Show description on themes'),
        description=_(u'Add content description after every portal tab menu title.'),
        required=False,
        default=False
    )

    search_position = schema.Choice(
        title=_(u'Search position'),
        description=_(u'Search box position in eligible themes.'),
        required=True,
        values=[
            u'default_position',
            u'always_in_navigation',
            u'always_in_actions',
        ],
        default=u'default_position'
    )

    collapse_minisite_menu = schema.Bool(
        title=_(u'Collapse menu on minisites'),
        description=_(u'Automatically collapse portal main menu on minisites.'),  # noqa
        required=False,
        default=False
    )

    show_footer_sitemap = schema.Bool(
        title=_(u'Show footer sitemap'),
        description=_(u'Automatically generate sitemap footer'),
        required=False,
        default=True
    )


class IVideoCollection(Interface):
    """
    Marker interface for video collection used to viewlet multimedia
    """


class IAlbumCollection(Interface):
    """
    Marker interface for album collection used to viewlet multimedia
    """
