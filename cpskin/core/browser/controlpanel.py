from zope.interface import implements
from zope.component import adapts
from zope.component import getUtility
from zope.formlib import form

from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.CMFPlone.interfaces import IPloneSiteRoot

from plone.registry.interfaces import IRegistry
from plone.app.controlpanel.form import ControlPanelForm

from cpskin.core.interfaces import ICPSkinSettings
from cpskin.locales import CPSkinMessageFactory as _


class CPSkinControlPanelAdapter(SchemaAdapterBase):

    adapts(IPloneSiteRoot)
    implements(ICPSkinSettings)

    def __init__(self, context):
        super(CPSkinControlPanelAdapter, self).__init__(context)
        registry = getUtility(IRegistry)
        self.settings = registry.forInterface(ICPSkinSettings, False)


class CPSkinControlPanel(ControlPanelForm):

    label = _("CPSkin settings")
    description = _("Lets you change the settings of CPSkin")
    form_fields = form.FormFields(ICPSkinSettings)
