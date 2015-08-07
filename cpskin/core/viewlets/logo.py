# -*- coding: utf-8 -*-
from plone.app.layout.viewlets.common import LogoViewlet
from zExceptions import NotFound


class CPSkinLogoViewlet(LogoViewlet):

    def update(self):
        super(CPSkinLogoViewlet, self).update()
        logoName = 'cpskinlogo.png'
        logoTitle = self.portal_state.portal_title()
        try:
            logo_custom = self.context.restrictedTraverse(logoName)
        except (AttributeError, KeyError, NotFound):
            # If no custom logo found, super() will handle default one
            pass
        else:
            self.logo_tag = logo_custom.tag(title=logoTitle, alt=logoTitle)
