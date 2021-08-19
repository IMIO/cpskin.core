# -*- coding: utf-8 -*-

from collective.privacy.browser.consent import ConsentForm
from cpskin.locales import CPSkinMessageFactory as _
from plone import api
from z3c.form import button


class CPSkinConsentForm(ConsentForm):
    description = _(
        u"Choose to opt in or out of various pieces of functionality. <br/>"
        u"You can <a href=''>read our cookie policy</a> for more informations."
    )

    @button.buttonAndHandler(_(u"Ok"))
    def handleApply(self, action):
        super(CPSkinConsentForm, self).handleApply(self, action)
        if self.status == self.formErrorsMessage:
            # there were some errors
            return

        if "ajax_load" in self.request.form:
            # the form was loaded via an overlay, we need a redirect to close it
            nav_root_url = api.portal.get_navigation_root(self.context).absolute_url()
            self.request.response.redirect(nav_root_url)
