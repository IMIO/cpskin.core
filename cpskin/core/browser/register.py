from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.users.browser.register import RegistrationForm
from zope.formlib.interfaces import WidgetInputError

from cpskin.locales import CPSkinMessageFactory as _


class CustomRegistrationForm(RegistrationForm):
    correct_captcha = None
    template = ViewPageTemplateFile('templates/register_form.pt')

    def validate_registration(self, action, data):
        errors = super(CustomRegistrationForm, self).validate_registration(
            action,
            data,
        )
        correct_captcha = self.context.restrictedTraverse('@@captcha').verify()
        if not correct_captcha:
            error = WidgetInputError(
                'captcha',
                'Captcha',
                _(u'Incorrect captcha')
            )
            errors.append(error)
        self.correct_captcha = correct_captcha
        return errors
