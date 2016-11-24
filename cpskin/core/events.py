# -*- coding: utf-8 -*-
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
