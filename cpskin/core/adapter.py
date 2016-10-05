# -*- coding: utf-8 -*-
from collective.documentgenerator.content.condition import ConfigurablePODTemplateCondition
from imio.dashboard.content.pod_template import DashboardPODTemplateCondition as DPTC


class DashboardPODTemplateCondition(DPTC):

    def evaluate(self):
        return super(ConfigurablePODTemplateCondition, self).evaluate()
