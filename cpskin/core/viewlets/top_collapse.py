# -*- coding: utf-8 -*-

from plone import api
from plone.app.layout.viewlets import common


class TopCollapseViewlet(common.ViewletBase):

    def available(self):
        return api.portal.get_registry_record(
            'cpskin.core.interfaces.ICPSkinSettings.collapse_minisite_menu',
            default=False,
        )
