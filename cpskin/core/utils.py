from plone import api


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
