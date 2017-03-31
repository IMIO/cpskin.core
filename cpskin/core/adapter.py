# -*- coding: utf-8 -*-
from collective.documentgenerator.content.condition import ConfigurablePODTemplateCondition  # noqa
from imio.dashboard.content.pod_template import DashboardPODTemplateCondition as DPTC  # noqa


class DashboardPODTemplateCondition(DPTC):

    def evaluate(self):
        return super(ConfigurablePODTemplateCondition, self).evaluate()
