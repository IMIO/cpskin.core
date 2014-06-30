# -*- coding: utf-8 -*-
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


class IMediaActivated(Interface):
    """
    Marker interface to enable / disable (multi)media viewlet
    """


class ICPSkinSettings(Interface):
    """
    Settings for CPSkin
    """
