# -*- coding: utf-8 -*-
from collective.documentgenerator.browser.generation_view import DocumentGenerationView
from collective.documentgenerator.helper.dexterity import DXDocumentGenerationHelperView
from collective.taxonomy.interfaces import ITaxonomy
from cpskin.core.interfaces import IFolderViewSelectedContent as IFVSC
from cpskin.core.utils import safe_utf8
from cpskin.locales import CPSkinMessageFactory as _
from DateTime import DateTime
from eea.facetednavigation.interfaces import IFacetedNavigable
from imio.dashboard.utils import getDashboardQueryResult
from plone import api
from plone.app.event.base import date_speller
from plone.app.event.base import dates_for_display
from plone.app.layout.viewlets.common import PathBarViewlet
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.MailHost.interfaces import IMailHost
from zope.component import getSiteManager
from zope.component import getUtility
from zope.component.interfaces import ComponentLookupError
from zope.publisher.browser import BrowserView

import base64
import json
import logging


logger = logging.getLogger('cpskin.core.browser.pages')


class FrontPage(BrowserView):

    index = ViewPageTemplateFile('templates/frontpage.pt')


class HelpPage(BrowserView):

    index = ViewPageTemplateFile('templates/helppage.pt')


class OpenData(BrowserView):
    """Get data news, events rss feed and collective.directory csv files."""

    index = ViewPageTemplateFile('templates/opendata.pt')

    def get_links(self):
        portal = api.portal.get()
        links = []
        path = '/'.join(portal.getPhysicalPath())
        portal_catalog = api.portal.get_tool('portal_catalog')
        query_dict = {}
        query_dict['path'] = {'query': path, 'depth': 1}
        query_dict['portal_type'] = ['Folder']
        query_dict['object_provides'] = IFVSC.__identifier__
        query_dict['sort_on'] = 'getObjPositionInParent'
        brains = portal_catalog(query_dict)
        for brain in brains:
            folder = brain.getObject()
            if getattr(folder, 'default_page', None):
                default_page = folder.default_page
                default_obj = folder[default_page]
                rsslink = '{0}/atom.xml'.format(default_obj.absolute_url())
                links.append(rsslink)

        query_dict = {}
        query_dict['portal_type'] = ['collective.directory.directory']
        brains = portal_catalog(query_dict)
        for brain in brains:
            directory = brain.getObject()
            catalog = api.portal.get_tool('portal_catalog')
            query_dict = {}
            query_dict['portal_type'] = 'collective.directory.card'
            query_dict['path'] = {
                'query': '/'.join(directory.getPhysicalPath()), 'depth': 3}
            size = len(catalog(query_dict))
            if size > 3:
                csvlink = '{0}/collective_directory_export_view'.format(
                    directory.absolute_url()
                )
                links.append(csvlink)

        return links


class IDocumentGenerationView(DocumentGenerationView):
    """Override the 'get_generation_context' properly so 'get_base_generation_context'
       is available for sub-packages that want to extend the template generation context."""

    def _get_generation_context(self, helper_view, pod_template):
        result = super(IDocumentGenerationView, self)._get_generation_context(helper_view, pod_template)
        # if pod_template.portal_type == 'ConfigurablePODTemplate':
        if IFacetedNavigable.providedBy(self.context):
            result['brains'] = getDashboardQueryResult(self.context)
            return result


class EventGenerationHelperView(DXDocumentGenerationHelperView):

    def is_same_month(self, start, end):
        return start.get('month') == end.get('month')

    def get_formatted_date(self):
        date_formated = u''
        event = self.real_context
        dates = dates_for_display(event)
        date_spel_start = date_speller(event, dates.get('start_iso'))
        date_spel_end = date_speller(event, dates.get('end_iso'))
        # day and month
        if dates.get('same_day'):
            date_formated = u'{0} {1}'.format(
                date_spel_start.get('day'),
                date_spel_start.get('month'))
        elif self.is_same_month(date_spel_start, date_spel_end):
            date_formated = u'{0} au {1} {2}'.format(
                date_spel_start.get('day'),
                date_spel_end.get('day'),
                date_spel_start.get('month'))
        else:
            date_formated += u'{0} {1} au {2} {3}'.format(
                date_spel_start.get('day'),
                date_spel_start.get('month'),
                date_spel_end.get('day'),
                date_spel_end.get('month'))

        # hour
        if not dates.get('whole_day'):
            if dates.get('open_end'):
                date_formated += _(u'\nà ')
                date_formated += u'{0}:{1}'.format(
                    date_spel_start.get('hour'),
                    date_spel_start.get('minute2'))
            else:
                date_formated += _(u'\nde ')
                date_formated += u'{0}:{1}'.format(
                    date_spel_start.get('hour'),
                    date_spel_start.get('minute2'))
                date_formated += _(u' à ')
                date_formated += u'{0}:{1}'.format(
                    date_spel_end.get('hour'),
                    date_spel_end.get('minute2'))

        return date_formated

    def get_taxonomy_values_in_one_line(self, field_names, sep, second_sep=' '):
        text = []
        for field_name in field_names:
            value = ''
            if isinstance(field_name, dict):
                (dict_text, dict_field_name) = field_name.items()[0]
                value = self.get_taxonomy_value(dict_field_name, second_sep)
                if value:
                    text.append('{} {}'.format(dict_text, value))
            else:
                value = self.get_taxonomy_value(field_name, second_sep)
                if value:
                    text.append(value)
        return sep.join(text)

    def get_taxonomy_value(self, field_name, sep=' '):
        lang = self.real_context.language
        taxonomy_ids = self.get_value(field_name)
        if not taxonomy_ids:
            return None
        if isinstance(taxonomy_ids, basestring):
            taxonomy_ids = [taxonomy_ids]
        domain = 'collective.taxonomy.{0}'.format(
            field_name.replace('taxonomy_', '').replace('_', ''))

        sm = getSiteManager()
        utility = sm.queryUtility(ITaxonomy, name=domain)
        taxonomy_list = [taxonomy_id for taxonomy_id in taxonomy_ids]
        text = []
        if len(taxonomy_list) > 0:
            for taxonomy_id in taxonomy_list:
                text.append(
                    safe_utf8(
                        utility.translate(
                            taxonomy_id,
                            context=self.real_context,
                            target_language=lang
                        )
                    )
                )
            return sep.join(text)
        else:
            return None

    def get_relation_field(self, field_name):
        related_obj = self.get_value(field_name)
        if not related_obj:
            return None
        if isinstance(related_obj, list):
            return [obj.to_object for obj in related_obj]
        return related_obj.to_object

    def get_relation_value(self, field_name, value_name, sep=' '):
        if isinstance(value_name, list):
            result = []
            for value in value_name:
                relation_field = self.get_relation_field(field_name)
                result.append(getattr(relation_field, value, ''))
            return sep.join(result)
        relation_field = self.get_relation_field(field_name)
        if isinstance(relation_field, list):
            result = []
            for rel in relation_field:
                result.append(getattr(rel, value_name, ''))
            return sep.join(result)
        return getattr(relation_field, value_name, '')

    def get_partners(self, prefix='', sep=' '):
        partners = self.get_relation_value('partners', 'title', sep)
        text = partners
        if prefix:
            text = '{} {}'.format(prefix, partners)
        return text

    def get_info(self):
        obj = self.get_relation_field('contact')
        info = []
        phone = getattr(obj, 'phone', None)
        if not phone:
            obj = self.get_relation_field('organizer')
            phone = getattr(obj, 'phone', None)
        if phone:
            if isinstance(phone, list):
                info.append(' '.join(phone))
            else:
                info.append(phone)
        website = getattr(obj, 'website', None)
        if website:
            info.append(website)
        if len(info) >= 1:
            infomsg = _(u'Info : ')
            return '{0} {1}'.format(infomsg, ' - '.join(info))
        else:
            return ''

    def get_address(self):
        address = []
        address.append(_(u'Où ?'))
        title = self.get_relation_value('location', 'title')
        if title:
            address.append(title)
        street = self.get_relation_value('location', 'street')
        number = self.get_relation_value('location', 'number')
        if street:
            street_with_number = street
            if number:
                street_with_number = u'{0}, {1}'.format(street, str(number))
            address.append(street_with_number)
        zip_code = self.get_relation_value('location', 'zip_code')
        city = self.get_relation_value('location', 'city')
        if city and zip_code:
            address.append(u'{0} {1}'.format(zip_code, city))
        if len(address) > 1:
            return '\n'.join(address)
        else:
            return ''


class TupleErrorPage(BrowserView):
    def __call__(self):
        event_col = self.context
        queries = []
        for query in event_col.query:
            if not isinstance(query.get('v'), tuple):
                queries.append(query)
        event_col.query = queries
        return 'End of tuple error'


class TransmoExport(BrowserView):
    def __call__(self):
        objects = {}
        # get all file in custom folder
        portal_skins = api.portal.get_tool('portal_skins')
        objects['custom'] = []
        for obj_id, item in portal_skins.custom.items():
            if item.meta_type in ['Image', 'File']:
                try:
                    data = base64.b64encode(item.data)
                    objects['custom'].append({
                        'obj_id': obj_id,
                        'meta_type': item.meta_type,
                        'data': data
                    })
                except:
                    logger.info('Not able to export {}'.format(
                        '/'.join(item.getPhysicalPath()))
                    )
            else:
                try:
                    objects['custom'].append({
                        'obj_id': obj_id,
                        'meta_type': item.meta_type,
                        'raw': item.raw
                    })
                except:
                    logger.info('Not able to export {}'.format(
                        '/'.join(item.getPhysicalPath()))
                    )
        objects['default_skin'] = portal_skins.default_skin
        # get list of installed profile
        portal_quickinstaller = api.portal.get_tool('portal_quickinstaller')
        product_ids = [product['id'] for product in portal_quickinstaller.listInstalledProducts()]
        objects['products'] = product_ids

        portal_membership = api.portal.get_tool('portal_membership')
        list_members = portal_membership.listMembers()
        #groups
        groups = []
        for site_group in api.group.get_groups():
            group = {}
            group['id'] = site_group.getId()
            group['title'] = site_group.title
            group['description'] = site_group.description
            group['roles'] = site_group.getRoles()
            group['groups'] = site_group.getGroups()
            users = [user.id for user in api.user.get_users(groupname=group['id']) if user in list_members]  # noqa
            group['users'] = users
            groups.append(group)
        objects['groups'] = groups
        # users
        pas = api.portal.get().acl_users
        passwords = dict(pas.source_users._user_passwords)
        users = []
        for member in list_members:
            user = {}
            user['id'] = member.getId()
            user['name'] = member.getProperty('fullname', member.getUserName())
            user['email'] = member.getProperty('email', None)
            user['fullname'] = member.getProperty('fullname', None)
            login_time = member.getProperty('login_time', None)
            if login_time == DateTime('2000/01/01'):
                user['login_date'] = ''
            else:
                user['login_date'] = login_time.strftime('%d/%m/%Y')
            last_login_time = member.getProperty(
                'last_login_time',
                None
            )
            if last_login_time == DateTime('2000/01/01'):
                user['last_login_date'] = ''
            else:
                user['last_login_date'] = last_login_time.strftime('%d/%m/%Y')
            if user['login_date'] == user['last_login_date']:
                user['last_login_date'] = ''
            user['roles'] = member.getRoles()
            user['domains'] = member.getDomains()
            user['password'] = passwords.get(user['id'])
            users.append(user)
        objects['users'] = users

        # mail control panel
        mailhost = {}
        try:
            mail_host = getUtility(IMailHost)
        except ComponentLookupError:
            mail_host = getattr(api.portal.get(), 'MailHost')
        mailhost['smtp_host'] = mail_host.smtp_host
        mailhost['smtp_port'] = mail_host.smtp_port
        mailhost['smtp_userid'] = getattr(mail_host, 'smtp_userid', None)
        mailhost['smtp_uid'] = getattr(mail_host, 'smtp_uid', None)
        mailhost['smtp_pwd'] = mail_host.smtp_pwd
        mailhost['email_from_address'] = api.portal.get().email_from_address
        mailhost['email_from_name'] = api.portal.get().email_from_name
        objects['mailhost'] = mailhost

        # geo
        lat_key = 'collective.geo.settings.interfaces.IGeoSettings.latitude'
        lng_key = 'collective.geo.settings.interfaces.IGeoSettings.longitude'
        geo = {}
        geo['latitude'] = str(api.portal.get_registry_record(lat_key))
        geo['longitude'] = str(api.portal.get_registry_record(lng_key))
        objects['geo'] = geo

        # portal_languages
        portal_languages = api.portal.get_tool('portal_languages')
        objects['languages'] = portal_languages.supported_langs

        portal_catalog = api.portal.get_tool('portal_catalog')
        total_objects = len(portal_catalog({}))
        objects['total_objects'] = str(total_objects)
        return json.dumps(objects)


class TeleService(BrowserView):
    index = ViewPageTemplateFile('templates/teleservice.pt')


class EmptyPathBarViewlet(PathBarViewlet):
    index = ViewPageTemplateFile('templates/empty.pt')
