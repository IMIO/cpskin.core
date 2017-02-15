# -*- coding: utf-8 -*-
from plone.app.imagecropping import PAI_STORAGE_KEY
from plone.app.imagecropping.interfaces import IImageCroppingUtils
from zope.annotation.interfaces import IAnnotations
from zope.component import getMultiAdapter
from zope.globalrequest import getRequest

from cpskin.core.utils import get_address_from_obj
from cpskin.core.utils import has_lat_lng
from cpskin.core.utils import set_coord


def set_lat_lng(obj, event):
    """Set lat and lng when a organization is created"""
    if has_lat_lng(obj):
        return
    address = get_address_from_obj(obj)
    if not address:
        return
    request = obj.REQUEST
    set_coord(obj, request)


def apply_crops_after_modify(obj, event):
    """
    Bug fixed here : cropped images scales on a content are lost after a
                     modification of this content (#14901).
    This is already fixed in Plone 5 but not in Plone 4 :
        https://github.com/collective/plone.app.imagecropping/issues/21
    To fix this, we need to re-generate all the crops of an object just after
    it's modification.
    """
    crops = IAnnotations(obj).get(PAI_STORAGE_KEY)
    if not crops:
        return
    croputils = IImageCroppingUtils(obj)
    request = getRequest()
    cropper = getMultiAdapter((obj, request), name='crop-image')
    for fieldname in croputils.image_field_names():
        for crop_key in crops:
            if crop_key.startswith(fieldname):
                scalename = crop_key[len(fieldname) + 1:]
                cropper._crop(fieldname, scalename, crops[crop_key])
