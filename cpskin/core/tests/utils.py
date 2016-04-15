
def add_contents(portal):
    add_events(portal)




def add_events(portal):
    """Add some demo events."""
    timezone = 'Europe/Brussels'
    reg = getUtility(IRegistry)
    settings = reg.forInterface(IEventSettings, prefix="plone.app.event")
    if not settings.portal_timezone:
        settings.portal_timezone = timezone
    event_folder = api.content.get('/evenements')
    now = datetime.datetime.now()
    tomorrow = datetime.datetime(now.year, now.month, now.day + 1)
    today18 = datetime.datetime(now.year, now.month, now.day, 18)
    today21 = datetime.datetime(now.year, now.month, now.day, 21)
    today23 = datetime.datetime(now.year, now.month, now.day, 23)
    # tomorrow18 = today18 + datetime.timedelta(days=1)
    tomorrow21 = today21 + datetime.timedelta(days=1)
    tomorrow23 = today23 + datetime.timedelta(days=1)
    next_week = tomorrow + datetime.timedelta(weeks=1)
    events = [{
        'title': 'Atelier photo',
        'desc': 'Participer à un atelier photo',
        'start': today18,
        'end': today21,
        'img': 'atelierphoto.jpg',
        'alaune': True,
    }, {
        'title': 'Concert',
        'desc': 'Participer à notre concert caritatif',
        'start': tomorrow21,
        'end': tomorrow23,
        'img': 'concert.jpg'
    }, {
        'title': 'Marché aux fleurs',
        'desc': 'Vener découvrir notre marché aux fleurs',
        'start': tomorrow,
        'end': next_week,
        'img': 'marcheauxfleurs.jpg'
    }
    ]
    for e in events:
        event = api.content.create(
            container=event_folder,
            type='Event',
            title=e['title']
        )
        event.title = e['title']
        event.description = e['desc']
        event.timezone = timezone
        behavior = IEventBasic(event)
        behavior.start = e['start']
        behavior.end = e['end']
        add_leadimage_from_file(event, e['img'])
        if e.get('alaune'):
            add_alaune(event)
        api.content.transition(obj=event, transition='publish_and_hide')
        event.reindexObject()


def add_news(portal):
    news_folder = api.content.get('/actualites')
    news = [{
        'title': 'Nouvelle brasserie',
        'desc': 'Une nouvelle brasserie va ouvrir ses portes près de chez vous',
        'text': 'Bonjour, <br /><br />Une nouvelle brasserie va ouvrir ses portes près de chez vous',
        'img': 'brasserie.jpg',
        'alaune': True,
    }, {
        'title': 'Météo',
        'desc': 'Attention à la météo de ces prochains jours',
        'text': 'Bonjour, <br /><br />Faites attention à la météo de ces prochains jours',
        'img': 'meteo.jpg'
    },
    ]
    for actualite in news:
        actu = api.content.create(
            container=news_folder,
            type='News Item',
            title=actualite['title']
        )
        actu.title = actualite['title']
        add_news_image_from_file(actu, actualite['img'])
        if actualite.get('alaune'):
            add_alaune(actu)
        api.content.transition(obj=actu, transition='publish_and_hide')
        actu.reindexObject()


def add_alaune(obj):
    obj.hiddenTags = set([u'a-la-une', ])
    pass
