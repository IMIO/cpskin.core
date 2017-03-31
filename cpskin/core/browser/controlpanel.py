# -*- coding: utf-8 -*-
from cpskin.core.interfaces import ICPSkinSettings
from cpskin.locales import CPSkinMessageFactory as _
from plone.app.controlpanel.form import ControlPanelForm
from plone.registry.interfaces import IRegistry
from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.CMFPlone.interfaces import IPloneSiteRoot
from zope.component import adapts
from zope.component import getUtility
from zope.formlib import form
from zope.interface import implements


class CPSkinControlPanelAdapter(SchemaAdapterBase):

    adapts(IPloneSiteRoot)
    implements(ICPSkinSettings)

    def __init__(self, context):
        super(CPSkinControlPanelAdapter, self).__init__(context)
        registry = getUtility(IRegistry)
        self.settings = registry.forInterface(ICPSkinSettings, False)

    def getLoadPageMenu(self):
        return self.settings.load_page_menu

    def setLoadPageMenu(self, value):
        self.settings.load_page_menu = value

    load_page_menu = property(getLoadPageMenu, setLoadPageMenu)

    def getSubMenuPersistence(self):
        return self.settings.sub_menu_persistence

    def setSubMenuPersistence(self, value):
        self.settings.sub_menu_persistence = value

    sub_menu_persistence = property(
        getSubMenuPersistence, setSubMenuPersistence)

    def getAutoPlaySlider(self):
        return self.settings.auto_play_slider

    def setAutoPlaySlider(self, value):
        self.settings.auto_play_slider = value

    auto_play_slider = property(getAutoPlaySlider, setAutoPlaySlider)

    def getSliderTimer(self):
        return self.settings.slider_timer

    def setSliderTimer(self, value):
        self.settings.slider_timer = value

    slider_timer = property(getSliderTimer, setSliderTimer)

    def getCityName(self):
        return self.settings.city_name

    def setCityName(self, value):
        self.settings.city_name = value

    city_name = property(getCityName, setCityName)

    def getSliderType(self):
        return self.settings.slider_type

    def setSliderType(self, value):
        self.settings.slider_type = value

    slider_type = property(getSliderType, setSliderType)


class CPSkinControlPanel(ControlPanelForm):

    label = _('CPSkin settings')
    description = _('Lets you change the settings of CPSkin')
    form_fields = form.FormFields(ICPSkinSettings)
