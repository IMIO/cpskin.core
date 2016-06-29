# -*- coding: utf-8 -*-
from Acquisition import aq_base
from plone import api
from plone.app.layout.navigation.interfaces import INavigationRoot
from plone.dexterity.interfaces import IDexterityFTI
from plone.namedfile.file import NamedBlobImage
from Products.CMFCore.interfaces import ISiteRoot
from zope.component import queryUtility

import os


def safe_utf8(s):
    """Transform unicode to utf8"""
    if isinstance(s, unicode):
        s = s.encode('utf8')
    return s


def safe_unicode(s):
    """Decode from utf8"""
    if isinstance(s, str):
        s = s.decode('utf8')
    return s


def reactivateTopic():
    """Reactivate old Topic content type"""
    portal = api.portal.get()
    portal.portal_types.Topic.manage_changeProperties(global_allow=True)
    for action in portal.portal_controlpanel.listActions():
        if action.id == 'portal_atct':
            action.visible = True


def convertCollection(collection):
    """Convert a new collection into an old collection"""
    portal = api.portal.get()

    id = collection.id
    title = collection.title
    container = collection.aq_parent
    default_page = container.getDefaultPage()

    api.content.delete(collection)
    allowed_types = container.getLocallyAllowedTypes()
    container.setLocallyAllowedTypes(allowed_types + ('Topic', ))
    old_collection = api.content.create(container=container, type=u"Topic",
                                        id=id, title=title, safe_id=False)
    portal.portal_workflow.doActionFor(old_collection, 'publish')
    container.setLocallyAllowedTypes(allowed_types)
    container.setDefaultPage(default_page)
    return old_collection


def publish_content(content):
    """Publish an object and hide it for cpskin."""
    wftool = api.portal.get_tool('portal_workflow')
    if wftool.getInfoFor(content, 'review_state') != 'published':
        actions = [a.get('id') for a in wftool.listActions(object=content)]
        if api.content.get_state(obj=content) != 'published_and_hidden':
            # we need to handle both workflows
            if 'publish_and_hide' in actions:
                wftool.doActionFor(content, 'publish_and_hide')
            elif 'publish' in actions:
                wftool.doActionFor(content, 'publish')


def add_keyword(obj, tag_id='hiddenTags', tag_value=[]):
    """Add a keyword to a object."""
    old_value = getattr(obj, tag_id)
    if not old_value:
        values = tag_value
    else:
        values = old_value + tag_value
    setattr(obj, tag_id, values)
    obj.reindexObject()


def add_behavior(type_name, behavior_name):
    """Add a behavior to a type"""
    fti = queryUtility(IDexterityFTI, name=type_name)
    if not fti:
        return
    behaviors = list(fti.behaviors)
    if behavior_name not in behaviors:
        behaviors.append(behavior_name)
        fti._updateProperty('behaviors', tuple(behaviors))


def remove_behavior(type_name, behavior_name):
    """Add a behavior to a type"""
    fti = queryUtility(IDexterityFTI, name=type_name)
    behaviors = list(fti.behaviors)
    if behavior_name in behaviors:
        behaviors.remove(behavior_name)
        fti._updateProperty('behaviors', tuple(behaviors))


def add_leadimage_from_file(container, file_name, folder_name='data'):
    """Add leadimage from a file from a folder"""
    if not container:
        container = api.portal.get()
    data_path = os.path.join(os.path.dirname(__file__), folder_name)
    file_path = os.path.join(data_path, file_name)
    if not getattr(aq_base(container), file_name, False):
        namedblobimage = NamedBlobImage(
            data=open(file_path, 'r').read(),
            filename=unicode(file_name)
        )
        image_container = container
        if not INavigationRoot.providedBy(container) and not ISiteRoot.providedBy(container):
            image_container = container.aq_parent

        image = api.content.create(type='Image',
                                   title=file_name,
                                   image=namedblobimage,
                                   container=image_container)
        image.setTitle(file_name)
        image.reindexObject()
        setattr(container, 'image', namedblobimage)


def image_scale(obj, css_class, default_scale):
    images = obj.restrictedTraverse('@@images')
    image = images.scale('image', scale=default_scale)
    if not image:
        return False
    return image.tag(css_class=css_class) if image.tag() else ''
