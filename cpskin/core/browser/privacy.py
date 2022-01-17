# -*- coding: utf-8 -*-

from collective.privacy.browser.consent import ConsentForm
from cpskin.locales import CPSkinMessageFactory as _
from plone import api
from Products.Five import BrowserView
from z3c.form import button
from zope.i18n import translate

import json


class PrivacyView(BrowserView):
    """ """

    def allow_iframes(self):
        self.request.response.setHeader("Content-type", "application/json")
        portal_privacy = api.portal.get_tool("portal_privacy")
        return json.dumps(portal_privacy.processingIsAllowed("show_genetic_embed"))

    def allow_languages(self):
        self.request.response.setHeader("Content-type", "application/json")
        portal_privacy = api.portal.get_tool("portal_privacy")
        return json.dumps(portal_privacy.processingIsAllowed("language_preference"))


class ConsentFormWithPolicy(ConsentForm):
    def update(self):
        super(ConsentFormWithPolicy, self).update()
        root = api.portal.get_navigation_root(self.context)
        current_lang = api.portal.get_current_language()[:2]
        policy_url = u"{}/@@cookies-view".format(root.absolute_url())
        description = _(
            u"Choose to opt in or out of various pieces of functionality.<br/>"
            u'If you want, you can <a href="${policy_url}">read our cookie policy</a>.',
            mapping={u"policy_url": policy_url},
        )
        self.description = translate(description, target_language=current_lang)

    @property
    def schema(self):
        schema = super(ConsentFormWithPolicy, self).schema
        default_allowed_reasons = [
            "basic_analytics",
            "language_preference",
            "show_genetic_embed",
        ]
        for reason_id in default_allowed_reasons:
            if reason_id in schema:
                schema[reason_id].default = "Allowed"
        return schema

    @button.buttonAndHandler(_(u"Save"))
    def handleApply(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return

        privacy_tool = self.context.portal_privacy
        for topic, answer in data.items():
            answer = answer == "Allowed"
            if answer:
                privacy_tool.consentToProcessing(topic)
            else:
                privacy_tool.objectToProcessing(topic)
        self.status = _(u"Your preferences have been saved.")

        if "ajax_load" in self.request.form:
            # the form was loaded via an overlay, we need to redirect to
            # an existing page to close it
            portal = api.portal.get()
            self.request.response.redirect("{}/@@ok".format(portal.absolute_url()))
            return ""
