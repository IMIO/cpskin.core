# -*- coding: utf-8 -*-
from plone.app.layout.viewlets.common import LogoViewlet


class CPSkinLogoViewlet(LogoViewlet):

    def update(self):
        super(CPSkinLogoViewlet, self).update()
        logoName = 'cpskinlogo.png'
        logoTitle = self.portal_state.portal_title()
        try:
            logo_custom = self.context.restrictedTraverse(logoName)
        except (AttributeError, KeyError):
            #If not custom logo
            pass
        else:
            self.logo_tag = logo_custom.tag(title=logoTitle, alt=logoTitle)
