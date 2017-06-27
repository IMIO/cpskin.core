from plone import api
from zope.component import getMultiAdapter

from plonetheme.sunburst.browser.sunburstview import SunburstView as BaseSunburstView


class SunburstView(BaseSunburstView):

    def getColumnsClasses(self, view=None):
        """Determine whether a column should be shown. The left column is
        called plone.leftcolumn; the right column is called plone.rightcolumn.
        CPSkin : this is overriden to be able to take right portlets into
        special right actions panel (#17748).
        """
        portal_registry = api.portal.get_tool('portal_registry')
        enabled = portal_registry['cpskin.core.interfaces.ICPSkinSettings.show_portlets_in_right_actions_panel']  # noqa
        if not enabled:
            # CPSkin : if show_portlets_in_right_actions_panel is not enabled,
            # we use default columns calculation
            return super(SunburstView, self).getColumnsClasses(view)

        plone_view = getMultiAdapter(
            (self.context, self.request), name=u'plone')
        portal_state = getMultiAdapter(
            (self.context, self.request), name=u'plone_portal_state')

        sl = plone_view.have_portlets('plone.leftcolumn', view=view)
        # CPSkin : if show_portlets_in_right_actions_panel is enabled, we
        # don't want any right portlets consideration
        sr = False

        isRTL = portal_state.is_rtl()

        # pre-fill dictionary
        columns = dict(one="", content="", two="")

        if not sl and not sr:
            # we don't have columns, thus conten takes the whole width
            columns['content'] = "width-full position-0"

        elif sl and sr:
            # In case we have both columns, content takes 50% of the whole
            # width and the rest 50% is spread between the columns
            columns['one'] = "width-1:4 position-0"
            columns['content'] = "width-1:2 position-1:4"
            columns['two'] = "width-1:4 position-3:4"

        elif (sr and not sl) and isRTL:
            # We have right column and we are in RTL language
            columns['content'] = "width-3:4 position-1:4"
            columns['two'] = "width-1:4 position-0"

        elif (sr and not sl) and not isRTL:
            # We have right column and we are NOT in RTL language
            columns['content'] = "width-3:4 position-0"
            columns['two'] = "width-1:4 position-3:4"

        elif (sl and not sr) and isRTL:
            # We have left column and we are in RTL language
            columns['one'] = "width-1:4 position-3:4"
            columns['content'] = "width-3:4 position-0"

        elif (sl and not sr) and not isRTL:
            # We have left column and we are in NOT RTL language
            columns['one'] = "width-1:4 position-0"
            columns['content'] = "width-3:4 position-1:4"

        # append cell to each css-string
        for key, value in columns.items():
            columns[key] = "cell " + value

        return columns
