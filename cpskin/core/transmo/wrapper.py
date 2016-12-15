# -*- coding: utf-8 -*-
from Acquisition import aq_base
from collective.jsonify.wrapper import Wrapper
from Products.CMFCore.utils import getToolByName
from zope.annotation.interfaces import IAnnotations
from zope.interface import Interface
import os
import DateTime


class ISerializer(Interface):
    def __call__(value, filestore, extra=None):
        """Convert to a serializable reprentation"""


class Wrapper(Wrapper):
    """ Gets the data in a format that can be used by the
        transmogrifier blueprints in collective.jsonmigrator
    """

    def get_archetypes_fields(self):
        """ If Archetypes is used then dump schema
        """

        try:
            from Products.Archetypes.interfaces import IBaseObject
            if not IBaseObject.providedBy(self.context):
                return
        except:
            return

        import base64
        fields = self.context.Schema().fields()
        for field in fields:
            fieldname = unicode(field.__name__)
            type_ = field.__class__.__name__

            fieldnames = [
                'StringField', 'BooleanField', 'LinesField',
                'IntegerField', 'TextField', 'SimpleDataGridField',
                'FloatField', 'FixedPointField', 'TALESString',
                'TALESLines', 'ZPTField', 'DataGridField', 'EmailField',
                '_StringExtensionField', 'LeadimageCaptionField',
                'ExtensionStandardTagsField', 'ExtensionHiddenTagsField',
                'ExtensionIAmTagsField', 'ExtensionISearchTagsField',
                'CheckboxField'
            ]

            if type_ in fieldnames:
                try:
                    value = field.getRaw(self.context)
                except AttributeError:
                    value = self._get_at_field_value(field)

                if callable(value) is True:
                    value = value()

                if value and type_ in ['StringField', 'TextField']:
                    try:
                        value = self.decode(value)
                    except AttributeError:
                        # maybe an int?
                        value = unicode(value)
                    except Exception, e:
                        raise Exception('problems with %s: %s' % (
                            self.context.absolute_url(), str(e))
                        )
                elif value and type_ == 'DataGridField':
                    for i, row in enumerate(value):
                        for col_key in row.keys():
                            col_value = row[col_key]
                            if type(col_value) in (unicode, str):
                                value[i][col_key] = self.decode(col_value)

                try:
                    ct = field.getContentType(self.context)
                except AttributeError:
                    ct = ''
                self[unicode(fieldname)] = value
                self[unicode('_content_type_') + fieldname] = ct

            elif type_ in ['DateTimeField']:
                value = self._get_at_field_value(field)
                if value:
                    value = DateTime.DateTime.strftime(value, '%Y-%m-%d %H:%M')
                    # value = str(self._get_at_field_value(field))
                    # value = self._get_at_field_value(field).ISO8601()
                    self[unicode(fieldname)] = value

            elif type_ in [
                'ImageField',
                'FileField',
                'AttachmentField',
                'ExtensionBlobField',
                'LeadimageBlobImageField']:

                fieldname = unicode('_datafield_' + fieldname)
                value = self._get_at_field_value(field)
                value2 = value

                if not isinstance(value, str):
                    if isinstance(value.data, str):
                        value = base64.b64encode(value.data)
                    else:
                        data = value.data
                        value = ''
                        while data is not None:
                            value += data.data
                            data = data.next
                        value = base64.b64encode(value)

                try:
                    max_filesize = int(
                        os.environ.get('JSONIFY_MAX_FILESIZE', 20000000)
                    )
                except ValueError:
                    max_filesize = 20000000

                if value and len(value) < max_filesize:
                    size = value2.getSize()
                    try:
                        fname = field.getFilename(self.context)
                    except AttributeError:
                        fname = value2.getFilename()

                    try:
                        fname = self.decode(fname)
                    except AttributeError:
                        # maybe an int?
                        fname = unicode(fname)
                    except Exception, e:
                        raise Exception(
                            'problems with %s: %s' % (
                                self.context.absolute_url(), str(e)
                            )
                        )

                    try:
                        ctype = field.getContentType(self.context)
                    except AttributeError:
                        ctype = value2.getContentType()

                    self[fieldname] = {
                        'data': value,
                        'size': size,
                        'filename': fname or '',
                        'content_type': ctype,
                        'encoding': 'base64'
                    }

            elif type_ in ['QueryField']:
                value = field.getRaw(self.context)
                self[fieldname] = [dict(q) for q in value]

            elif type_ in ['ReferenceField']:
                pass

            elif type_ in ['ComputedField']:
                continue
            else:
                raise TypeError('Unknown field type for ArchetypesWrapper in '
                        '%s %s in %s' % (type_, fieldname, self.context.absolute_url()))

    def get_cpskin_interfaces(self):
        from cpskin.core.interfaces import IAlbumCollection
        from cpskin.core.interfaces import IBannerActivated
        from cpskin.core.interfaces import IFolderViewSelectedContent
        from cpskin.core.interfaces import IFolderViewWithBigImages
        from cpskin.core.interfaces import ILocalBannerActivated
        from cpskin.core.interfaces import IMediaActivated
        from cpskin.core.interfaces import IVideoCollection
        from cpskin.core.viewlets.interfaces import IViewletMenuToolsBox
        from cpskin.core.viewlets.interfaces import IViewletMenuToolsFaceted
        from cpskin.menu.interfaces import IDirectAccess
        from cpskin.menu.interfaces import IFourthLevelNavigation


        interfaces = [
            IAlbumCollection,
            IBannerActivated,
            IFolderViewSelectedContent,
            IFolderViewWithBigImages,
            ILocalBannerActivated,
            IMediaActivated,
            IVideoCollection,
            IViewletMenuToolsBox,
            IViewletMenuToolsFaceted,
            IDirectAccess,
            IFourthLevelNavigation
        ]
        inter = []
        for interface in interfaces:
            if interface.providedBy(self.context):
                inter.append(interface.__identifier__)
        self['cpskin_interfaces'] = inter

    def get_facted_criteria(self):
        from eea.facetednavigation.criteria.handler import Criteria
        from eea.facetednavigation.criteria.interfaces import ICriteria
        from eea.facetednavigation.indexes.language.interfaces import ILanguageWidgetAdapter
        from eea.facetednavigation.interfaces import IFacetedNavigable
        from eea.facetednavigation.settings.interfaces import IDisableSmartFacets
        from eea.facetednavigation.settings.interfaces import IHidePloneLeftColumn
        from eea.facetednavigation.settings.interfaces import IHidePloneRightColumn
        from eea.facetednavigation.subtypes.interfaces import IFacetedWrapper
        from eea.facetednavigation.views.interfaces import IViewsInfo
        from eea.facetednavigation.widgets.alphabetic.interfaces import IAlphabeticWidget
        from eea.facetednavigation.widgets.interfaces import ICriterion
        from eea.facetednavigation.widgets.interfaces import IWidget
        from eea.facetednavigation.widgets.interfaces import IWidgetsInfo
        from eea.facetednavigation.widgets.resultsfilter.interfaces import IResultsFilterWidget
        interfaces = [
            IFacetedNavigable,
            IDisableSmartFacets,
            IHidePloneLeftColumn,
            IHidePloneRightColumn,
            ICriteria,
            ILanguageWidgetAdapter,
            IFacetedWrapper,
            IViewsInfo,
            IAlphabeticWidget,
            ICriterion,
            IWidget,
            IWidgetsInfo,
            IResultsFilterWidget,
        ]
        inter = []
        for interface in interfaces:
            if interface.providedBy(self.context):
                inter.append(interface.__identifier__)
        self['faceted_interfaces'] = inter
        if IFacetedNavigable.providedBy(self.context):
            criteria = Criteria(self.context)
            import ipdb; ipdb.set_trace()
            import pickle
            serializer = pickle.dumps(criteria.criteria)
            self['faceted_criteria'] = serializer
