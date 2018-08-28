Changelog
=========

0.12.30 (2018-08-28)
--------------------

- Do not change collection count_items value during homepage loading.
  [bsuttor]


0.12.29 (2018-08-03)
--------------------

- Add get_values_in_one_line export method.
  [bsuttor]


0.12.28 (2018-08-03)
--------------------

- Add new search_position option for eligible themes : #21303
  [laulaz]

- Add Namur hack.
  [bsuttor]


0.12.27 (2018-07-31)
--------------------

- Add year to formatted date to export.
  [bsuttor]

- Fix unicode export partners and info
  [bsuttor]


0.12.26 (2018-07-31)
--------------------

- Add some information to Occurrence to be exported.
  [bsuttor]


0.12.25 (2018-07-30)
--------------------

- Add get_image_from_text method to export.
  [bsuttor]


0.12.24 (2018-07-27)
--------------------

- Add display_phones method to export.
  [bsuttor]


0.12.23 (2018-07-27)
--------------------

- Occurence are now considered as event during exportation.
  [bsuttor]


0.12.22 (2018-07-16)
--------------------

- Avoid an error when `imio.gdpr` is not installed
  [mpeeters]

- Remove divs "accueil-first" and "accueil-other".
  [bsuttor]

- Adapt index view to wrap first element into div and other into another div #21989.
  [bsuttor]


0.12.21 (2018-06-13)
--------------------

- Override FooterViewlet to add is_gdpr method.
  [bsuttor]

- Improve image_scale utils, get aboslute url of album.
  [bsuttor]


0.12.20 (2018-06-06)
--------------------

- Add class on body based on faceted navigation layout : #21603
  [laulaz]

- Never scale banner if it wasn't cropped : #21448
  [laulaz]

- Refactor banner url fetching code
  [laulaz]


0.12.19 (2018-06-04)
--------------------

- Fix footer static error
  [bsuttor]

- Always use cropped scale for banner image : #21448
  [laulaz]


0.12.18 (2018-05-31)
--------------------

- Add Mentions Légales link.
  [bsuttor]

- Add held_position to related_contacts widgets.
  [bsuttor]


0.12.17 (2018-05-16)
--------------------

- Don't try to display image on faceted preview if there is none
  [laulaz]


0.12.16 (2018-05-15)
--------------------

- Override eea preview items to re-use scale defined in index view : #21333
  [laulaz]


0.12.15 (2018-05-14)
--------------------

- Show only last term of taxonomy : #21398
  [laulaz]

- Simplify organization gallery viewlet availability code
  [laulaz]

- Don't display images of sub-organizations in organization gallery : #21364
  [laulaz]


0.12.14 (2018-04-25)
--------------------

- Fix date display on index view : we need the object and not the brain to
  get occurences : #21068
  [laulaz]

- Spelling correction "gallery" in organizations.
  [mgennart]


0.12.13 (2018-04-04)
--------------------

- Add migration after allowing to display / hide titles for sliders
  [laulaz]

- Always use start / end of first / last recurrences for events : #20824
  [laulaz]

- Add title to info on export agenda view.
  [bsuttor]


0.12.12 (2018-03-29)
--------------------

- Split show_day_and_month index view setting into show_day_and_month and
  show_lead_image : #20879
  [laulaz]


0.12.11 (2018-03-27)
--------------------

- Handle link in homepage view
  [mpeeters]


0.12.10 (2018-03-26)
--------------------

- Handle top menu actions with empty sub-menus
  [laulaz]

- Add a parameter to define the states where the social viewlet should be
  displayed.
  [mpeeters]


0.12.9 (2018-03-20)
-------------------

- Improve contactdetail VCF export with mutli phones.
  [bsuttor]


0.12.8 (2018-03-19)
-------------------

- Fix missing zcml import
  [laulaz]

- Change time delay
  [osnickers ]


0.12.7 (2018-03-19)
-------------------

- Add collective.js.fancybox dependency
  [laulaz]

- Merge faceted contact preview and faceted contact preview with photos by
  using a new parameter on directory (show_organization_images) : #20754
  [laulaz]

- Fix templates for old faceted contact preview
  [laulaz]

- Allow to fetch taxonomy from behaviors : #20754
  Also move categories in template.
  [laulaz]

- Allow to specify scale for directory organization previews : #20754
  [laulaz]

- Make fancybox organization gallery scrollable : #20754
  [laulaz]

- Add 'hover' and 'hover-delay' (with delay) class when organization image
  changes : #20754
  [laulaz]


0.12.6 (2018-02-28)
-------------------

- Add photo gallery on organizations : #19171
  [laulaz]

- Add new faceted view for directory with changing images and optional
  taxonomy : #19171
  [laulaz]


0.12.5 (2018-01-31)
-------------------

- Temporary readd 'IUseKeywordHomepage' to fix bug with florennes.
  [bsuttor]


0.12.4 (2018-01-26)
-------------------

- Add figcaption to valid xhtml tags.
  [bsuttor]


0.12.3 (2018-01-25)
-------------------

- Check if there is a version in browser agent.
  [bsuttor]


0.12.2 (2018-01-24)
-------------------

- Improve portlet export, add visible.
  [bsuttor]


0.12.1 (2018-01-24)
-------------------

- Export behaviors for transmo view.
  [bsuttor]

- Add description into cpskin navigation views.
  [bsuttor]


0.12.0 (2018-01-18)
-------------------

- Get address for contacts with contact method.
  [bsuttor]

- Remove old collective.contentleadimage dependency.
  [bsuttor]

- Add a link to maps applications on directory addresses : #17317
  [mpeeters]


0.11.24 (2018-01-05)
--------------------

- Add replace-richtext-form view.
  [bsuttor]


0.11.23 (2018-01-03)
--------------------

- Improve export view.
  [bsuttor]


0.11.22 (2018-01-03)
--------------------

- Format phone for export view.
  [bsuttor]


0.11.21 (2017-12-19)
--------------------

- Add ContactChoice to wrapper transmo export.
  [bsuttor]


0.11.20 (2017-12-14)
--------------------

- Do not add Firefox portlet on install.
  [bsuttor]


0.11.19 (2017-12-08)
--------------------

- Add document_with_description view for document.
  [bsuttor]

- Override search view to add * at the end of SearchableText.
  [bsuttor]

- Add postion and held_position into "contact field vocabulary".
  [bsuttor]


0.11.18 (2017-12-05)
--------------------

- Improve transmo-export view.
  [bsuttor]

- Check if 'A la une' is not in hiddenTags before adding it.
  [bsuttor]


0.11.17 (2017-12-01)
--------------------
- Set default image collection value to collection.
  [bsuttor]

- Set default visible albums to 5 and default visible videos to 2.
  [bsuttor]

- Viewlets.xml : Insert "cpskin.banner" after "plone.header".
  [bsuttor]


0.11.16 (2017-11-27)
--------------------

- Use depth path to 2 to get opendata links.
  [bsuttor]


0.11.15 (2017-11-20)
--------------------

- Improve transmo-export view.
  [bsuttor]


0.11.14 (2017-11-17)
--------------------

- Bad release.
  [bsuttor]


0.11.13 (2017-11-17)
--------------------

- Get logo on related contact view if there is logo.
  [bsuttor]

- Get address from parent when use_parent_address checked.
  [bsuttor]


0.11.12 (2017-11-14)
--------------------

- Check if astimezone exists in get_event_dates method.
  [bsuttor]


0.11.11 (2017-11-09)
--------------------

- Improve cpskinhealthy.
  [bsuttor]

- Fix dates with timezones on calendar views : #19490
  [laulaz]


0.11.10 (2017-11-08)
--------------------

- Override vcard organization method to understand phones list.
  [bsuttor]


0.11.9 (2017-10-30)
-------------------

- Use Unrestrictedtraverse to get images in related_contacts.
  [bsuttor]

- Redirect to content after having submitted sendtomanager_form : #19359
  [laulaz]

- View see_map link if map is visible.
  [bsuttor]


0.11.8 (2017-10-25)
-------------------

- Add code for foldable social viewlet in right actions #19300
  [laulaz]


0.11.7 (2017-10-13)
-------------------

- Use cover instead of <img> for navigation with leadimages
  [laulaz]

- Add cellphones numbers on contact preview : #19126
  [laulaz]

- Use span instead of h2 tag for related contacts title.
  [bsuttor]

- Change events dates display to handle multi-days events
  [laulaz]

- Related items: Check if field has row to check if this is a RichTextValue value object.
  [bsuttor]

- Use sc.social.like instead of sc.social.bookmarks.
  [bsuttor]


0.11.6 (2017-10-02)
-------------------

- Use multimedia scale for images into media viewlet.
  [bsuttor]


0.11.5 (2017-09-29)
-------------------

- Reimplement validatePhone method to add / and ..
  [bsuttor]


0.11.4 (2017-09-26)
-------------------

- Get only published_and_shown objects into top menu.
  [bsuttor]


0.11.3 (2017-09-25)
-------------------

- Use navigation root instead of portal to compute level of folder.
  [bsuttor]


0.11.2 (2017-09-22)
-------------------

- Fix item count on index view for events collection.
  [bsuttor]


0.11.1 (2017-09-21)
-------------------

- On cpskin_navigation_view, only get direct access object after first level folder #18827.
  [bsuttor]

- Add cpskin_navigation_view_with_leadimage.
  [bsuttor]


0.11 (2017-09-20)
-----------------

- Hide top actions submenu on page load : #18474
  [laulaz]

- Add 'expired-content' class on body if current context has expired : #18846
  [laulaz]

- Add show_description option to show description on portal tab items : #17333
  [laulaz]

- Allow to set number of albums & videos for media viewlet in control panel
  Also don't use local property visible_albums anymore
  [laulaz]

- Don't fetch / request all albums twice in media viewlet
  [laulaz]

- Fix bodyclass related error when creating a new collection : #18592
  [laulaz]

- Avoid error when cpskin is not installed
  [laulaz]

- Change date position on faceted view for News Item content types : #18697
  Refactor tal conditions
  [laulaz]


0.10.23 (2017-09-13)
--------------------

- Add publication date on faceted view for News Item content types : #18697
  [laulaz]


0.10.22 (2017-09-13)
--------------------

- Add div for class voir-tout-content.
  [mgennart]


0.10.21 (2017-09-12)
--------------------

- Fix get level navigation when you are on edit of dexterty types.
  [bsuttor]

- Add css class on body for collection portal_types : #18592
  [laulaz]


0.10.20 (2017-09-04)
--------------------

- Fix sort order in top menu : #18586
  [laulaz]


0.10.19 (2017-08-31)
--------------------

- Avoid error when related items are broken : #18546
  [laulaz]


0.10.18 (2017-08-25)
--------------------

- Fix banner acquisition : parent banner folder was taken before local banner
  image : #18467
  [laulaz]

- Add div to be able to fill schedule, etc. in Diazo even if activity is
  empty : #18469
  [laulaz]

- We must always display right actions as content is coming unconditionnaly
  from Diazo
  [laulaz]


0.10.17 (2017-08-24)
--------------------

- Add logo to coordinates in related_contact view.
  [mgennart]


0.10.16 (2017-08-18)
--------------------

- Export subscribers in transmo-export view
  [bsuttor]

- Add OrderableReferenceField for transmo.
  [bsuttor]


0.10.15 (2017-08-17)
--------------------

- Fix empty images on homepage.
  [bsuttor]


0.10.14 (2017-08-10)
--------------------

- First step on adding cpskinhealthy view.
  [bsuttor]

- Fix images scale for person with no logo.
  [bsuttor]


0.10.13 (2017-08-10)
--------------------

- Add resources to transmo-export view.
  [bsuttor]


0.10.12 (2017-08-02)
--------------------

- Check if lesscss is installed before uninstallation of diazotheme.
  [bsuttor]


0.10.11 (2017-08-01)
--------------------

- Move h2 and activity div.
  [mgennart]


0.10.10 (2017-07-28)
--------------------

- Move schedule div.
  [bsuttor]


0.10.9 (2017-07-28)
-------------------

- related contact: Move schedule div into wrapped-coord.
  [bsuttor]


0.10.8 (2017-07-27)
-------------------

- Hack for right_action with bad related.
  [bsuttor]

- Check validity of google api key.
  [bsuttor]


0.10.7 (2017-07-19)
-------------------

- Improve set lat and lng on Organization and Person.
  [bsuttor]


0.10.6 (2017-07-17)
-------------------

- Change order of slide #18057
  [Aurore]

- Add class on <body> for logged in citizen users
  [laulaz]

- Fix default_skin after uninstalling other profiles (was reset to 'Plone
  Default' causing a main_template traceback)
  [laulaz]

- Allow to have all results without sticky distinction : #18026
  [laulaz]


0.10.5 (2017-07-05)
-------------------

- Adding a condition when the right action panel is not there.
  [mgennart]

0.10.4 (2017-07-05)
-------------------

- Bad release.
  [bsuttor]


0.10.3 (2017-07-04)
-------------------

- Try to find address with OSM fi Google do not work.
  [bsuttor]

- Add banner image field for events and use it as banner : #17809
  [Aurore]


0.10.2 (2017-06-29)
-------------------

- Add publication date check to display it on index view items : #17895
  [laulaz]

- Add Faceted contacts preview view.
  [bsuttor]

- Add main-homepage css class on LRF and Plone Site portal_types.
  [bsuttor]

- Add cpskin_navigation_view.
  [bsuttor]

- Add sticky right actions panel (for portlets and TOC) : #17748
  [laulaz]

- Use banner title and description as site slogan into banner : #17207
  [laulaz]

- Add class medialink on tag  #17396
  [Aurore]


0.10.1 (2017-06-20)
-------------------

- Do not show empty phone, cell_phone or fax.
  [bsuttor]

- Remove broken related_contacts.
  [bsuttor]

- Change address position : #17751
  [laulaz]


0.10 (2017-06-15)
-----------------

- Add description to organization type to translate it in citizen : #17660
  [laulaz]

- Changing the slide configuration to stop it #16991
  [Aurore]

- Force uninstall of packages that are not marked as installed but were
  imported in portal_setup : #17714
  [laulaz]

- Allow to have random images as banner : #17395
  [AuroreMariscal]


0.9.8 (2017-06-01)
------------------

- Improve transmo wrapper.
  [bsuttor]


0.9.7 (2017-05-19)
------------------

- Use h2 balise instead of h4 in related_contacts. Now, related_contacts are no more in summary link.
  [bsuttor]

- Add missing dependency on plone.app.multilingual
  [laulaz]

- Fix traceback when a related content doesn't have complete address : #17422
  [laulaz]


0.9.6 (2017-05-16)
------------------

- Bad release.


0.9.5 (2017-05-16)
------------------

- Add toggeable top menu with contents selected in cpskin settings : #16772
  [laulaz]

- Override facetednavigation_view to add text from collection.
  [bsuttor]

- Unpin z3c.form (already pinned in main buildout versions) to fix tests
  [laulaz]


0.9.4 (2017-05-10)
------------------

- Fix: upgrade_to_nineteen upgrade steps.
  [bsuttor]


0.9.3 (2017-05-10)
------------------

- Transmo: Add author when a connect user have post a message.
  [bsuttor]


0.9.2 (2017-05-09)
------------------

- Add comments author to transmo wrapper.
  [bsuttor]


0.9.1 (2017-05-09)
------------------

- Add discussion settings to transmo-export view.
  [bsuttor]

- Add zoom to transmo-export view.
  [bsuttor]


0.9 (2017-05-08)
----------------

- Add slide number / count calculation : #16991
  [laulaz]

- Allow to give id to slider_config to allow multiple sliders on page : #16991
  [laulaz]

- Add class on each and every index view block
  [laulaz]

- Add 'use slider' option on index view collections to replace 'a-la-une'
  magic and allow to have more sliders : #16991
  [laulaz]

- Add 'show descriptions' option on index view collections to include results
  descriptions : #16991
  [laulaz]


0.8.67 (2017-05-04)
-------------------

- Add default_skin to tranmo-export view.
  [bsuttor]


0.8.66 (2017-04-27)
-------------------

- Bugfix: be able to get related contacts which are not 'active' (use unrestrictedSearchResults).
  [bsuttor]


0.8.65 (2017-04-25)
-------------------

- Use h2 balise instead of h4 in related_contacts. Now, related_contacts are no more in summary link.
  [bsuttor]


0.8.64 (2017-04-24)
-------------------

- Update transmo-export.
  [bsuttor]


0.8.63 (2017-04-24)
-------------------

- Bad release.
  [bsuttor]


0.8.62 (2017-04-24)
-------------------

- Check if user exists for transmo.
  [bsuttor]


0.8.61 (2017-04-21)
-------------------

- Bugfix: Index view get logo instead of image if there is an organization or a person.
  [bsuttor]


0.8.60 (2017-04-20)
-------------------

- Add 'day and month' option on index view collections to style results
  differently (without leadimage) : #16800
  [laulaz]


0.8.59 (2017-04-11)
-------------------

- Add logo and address into map popup.
  [bsuttor]

- Add map below related_contacts.
  [bsuttor]

- Remove collective.directory auto install.
  [bsuttor]


0.8.58 (2017-03-30)
-------------------

- Imporve clean_old_keyword_homepage scripts.
  [bsuttor]

- Improve get_address_from_obj script, check if obj is an collective.directory.card.
  [bsuttor]

- Add new homepage index macro to use background images instead of <img>
  Old index macro is kept until all the sites are migrated
  [laulaz]

- Add new faceted view for listing items without images
  [laulaz]


0.8.57 (2017-03-22)
-------------------

- Empty breadcrumb for teleservice template.
  [bsuttor]


0.8.56 (2017-03-22)
-------------------

- Add @@teleservice-template view.
  [bsuttor]


0.8.55 (2017-03-20)
-------------------

- Format fax for related_contacts view.
  [bsuttor]

- Format fax for faceted view.
  [bsuttor]


0.8.54 (2017-03-10)
-------------------

- Fix bad formating when country_code is into phonenumbers.
  [bsuttor]


0.8.53 (2017-03-09)
-------------------

- Check is_one_day event also for Archetypes.
  [bsuttor]


0.8.52 (2017-03-06)
-------------------

- Fix translate text from fr-be : #16560.
  [bsuttor]

- Hide groups for organization (already hidden in css) : #16438
  [mpeeters]

- Add plone.belowcontenttitle viewlet manager to organizations : #16438
  [mpeeters]

- Fix the message factory for phone numbers : #16438
  [mpeeters]


0.8.51 (2017-02-23)
-------------------

- Check if realObject is a collection on index view.
  [bsuttor]


0.8.50 (2017-02-22)
-------------------

- Improve way to get translations during transmogrifier.
  [bsuttor]


0.8.49 (2017-02-17)
-------------------

- Add upgrade step to add theme variables.
  [bsuttor]

- Check if collection are not empty for folderview.
  [bsuttor]


0.8.48 (2017-02-15)
-------------------

- Fix lost cropped images scales on a content after a modification : #14901
  This is already fixed in Plone 5 but not in Plone 4.
  See https://github.com/collective/plone.app.imagecropping/issues/21
  [laulaz]

- Fix typo for css class.
  [bsuttor]


0.8.47 (2017-02-13)
-------------------

- Add in-minisite and in-minisite-in-portal css class to body.
  [bsuttor]


0.8.46 (2017-02-13)
-------------------

- Add tools for set ploneCustom.css latest.
  [bsuttor]


0.8.45 (2017-02-10)
-------------------

- Update transmo migration: check if obj is transalatable.
  [bsuttor]


0.8.44 (2017-02-07)
-------------------
- Set default value of link_text empty.
  [bsuttor]

- Add IAdditionalSearchableText behavior.
  [bsuttor]


0.8.43 (2017-02-01)
-------------------

- Add an empty field if there is not values
  [mpeeters]

- Format also fax numbers
  [mpeeters]

- Add a display view for the multiline widget
  [mpeeters]

- Avoid an error if only one phone was registered
  [mpeeters]

- Add an upgrade step to add the new faceted interface for multiple layout and
  the new javascript file for the multiline phone widget
  [mpeeters]

- Add languages used in portal in transmo-export view.
  [bsuttor]


0.8.42 (2017-01-30)
-------------------

- Add translation for migration.
  [bsuttor]


0.8.41 (2017-01-25)
-------------------

- Do not get duplicates layouts for faceted vocabulary layouts.
  [bsuttor]


0.8.40 (2017-01-20)
-------------------

- Improve hide date for archetypes.
  [bsuttor]


0.8.39 (2017-01-20)
-------------------

- Use formatted phone for related contacts.
  [bsuttor]


0.8.38 (2017-01-20)
-------------------

- Hide effective date for date.
  [bsuttor]


0.8.37 (2017-01-19)
-------------------

- Improve visible date on index view.
  [bsuttor]


0.8.36 (2017-01-18)
-------------------

- Also export user groups list.
  [bsuttor]


0.8.35 (2017-01-17)
-------------------

- Fix archetypes event.
  [bsuttor]


0.8.34 (2017-01-17)
-------------------

- Add a custom widget for phone numbers and format phone numbers in display mode
  [mpeeters]

- Fix open_day on index view do not show end date.
  [bsuttor]


0.8.33 (2017-01-11)
-------------------

- Fix if there is an empty leadimage for transmo export.
  [bsuttor]


0.8.32 (2017-01-10)
-------------------

- Improve export of custom folder.
  [bsuttor]


0.8.31 (2017-01-04)
-------------------

- Add export template and methods to export events.
  [bsuttor]


0.8.30 (2016-12-15)
-------------------

- Add checkbox to hide title.
  [bsuttor]

- Add checkbox to hide see_all_link.
  [bsuttor]

- Add checkbox to hide date on index view.
  [bsuttor]


0.8.29 (2016-12-05)
-------------------

- Add get_address for event export.
  [bsuttor]

- Use navigation_root for notheme section.
  [bsuttor]

- Set max to item_count_homepage to 30 and default to 8.
  [bsuttor]


0.8.28 (2016-11-23)
-------------------

- Field item_count_homepage now works on all collections.
  [bsuttor]


0.8.27 (2016-11-23)
-------------------

- Fix tuple and new query line when index_view_keywords is used.
  [bsuttor]


0.8.26 (2016-11-22)
-------------------

- Add tuple error view.
  [bsuttor]


0.8.25 (2016-11-22)
-------------------

- Set ploneFormTabbing.max_tabs to 10 into footer.
  [bsuttor]

- Fix error avec le viewlet related_contacts #15520. Now we check if there is a schedule before render it.
  [bsuttor]


0.8.24 (2016-11-21)
-------------------

- Add and use item_count_homepage field.
  [bsuttor]

- Use list instead of tuple to store index_view_keywords : #15306
  [laulaz]


0.8.23 (2016-11-21)
-------------------

- Fix a problem with the new layout adapter when the order of interfaces
  implemented on the object varies
  [mpeeters]


0.8.22 (2016-11-18)
-------------------

- Update way to view phone of it have mutliple phone numbers.
  [bsuttor]

- Add mobile click on phone numbers.
  [bsuttor]

- Fix acquisition problem with tags indexing for objects that don't have
  the related behavior : #15327
  [laulaz]


0.8.21 (2016-11-17)
-------------------

- Add the faceted layout widget : #14994
  [mpeeters]


0.8.20 (2016-11-17)
-------------------

- Adapt collective.contact.core views to prevent JS error which arrive
  when collective.geo.behaviour is enabled.
  [bsuttor]


0.8.19 (2016-11-16)
-------------------

- Add fields from IDirectoryContactDetails into ContactFieldsFactory vocabulary in a sad way.
  [bsuttor]


0.8.18 (2016-11-16)
-------------------

- Set default item_count value to 30.
  [bsuttor]


0.8.17 (2016-11-10)
-------------------

- Add a new behavior for directory contact details
  [mpeeters]


0.8.16 (2016-11-07)
-------------------

- Set item_count to higher value to sort with all events.
  [bsuttor]


0.8.15 (2016-10-12)
-------------------

- Add event export models.
  [bsuttor]


0.8.14 (2016-10-06)
-------------------

- Subscribe to creation of organization and person for creation of lat and lng.
  [bsuttor]

- Reindex object after adding lat and lng.
  [bsuttor]


0.8.13 (2016-10-05)
-------------------

- Bad release.
  [bsuttor]


0.8.12 (2016-10-05)
-------------------

- Fix bad relative path.
  [bsuttor]


0.8.11 (2016-10-05)
-------------------

- Add adapter for collective.documentgenerator and imio.dashboard.
  [bsuttor]

- Add set-geo-contents-form view.
  [bsuttor]

- Fix wildcard.foldercontents overflow.
  [bsuttor]


0.8.10 (2016-09-28)
-------------------

- Fix bug in remove_behavior.
  [bsuttor]


0.8.9 (2016-09-28)
------------------

- Add import step to delete cpskin.core.behaviors.metadata.IUseKeywordHomepage.
  [bsuttor]


0.8.8 (2016-09-23)
------------------

- Fix bug in plone.app.event.
  [bsuttor]


0.8.7 (2016-09-22)
------------------

- Readd old code to prevent bug.
  [bsuttor]


0.8.6 (2016-09-22)
------------------

- Update way to get events, now events are sort considering recurrence.
  [bsuttor]

0.8.5 (2016-09-07)
------------------

- Add collective.geo.faceted dependency.
  [bsuttor]


0.8.4 (2016-09-06)
------------------

- Add wrapped-coord div for related_contacts fields view.
  [bsuttor]


0.8.3 (2016-08-22)
------------------

- Set address and coordinates into other div than other fields from related_contacts.
  [bsuttor]


0.8.2 (2016-08-22)
------------------

- Use schedule render widget for schedule field.
  [bsuttor]

- Resolve uid for related contacts.
  [bsuttor]


0.8.1 (2016-08-09)
------------------

- Fix open_end with no dexterity content types.
  [bsuttor]


0.8.0 (2016-08-08)
------------------

- Move CPSkin actions to a new dedicated menu
  [laulaz]

- Add missing actions in uninstall profile
  [laulaz]

- Improve events dates / times display : #14573
  [laulaz]


0.7.35 (2016-08-04)
-------------------

- Related contact below contents title is now a link to related contact.
  [bsuttor]


0.7.34 (2016-08-03)
-------------------

- We need to invalidate JS cache when defining navigation toggle
  [laulaz]


0.7.33 (2016-07-29)
-------------------

- Fix relative URL calculation for navigation toggle on folders
  [laulaz]


0.7.32 (2016-07-28)
-------------------

- Add new action to enable / disable navigation toggle on folders
  Works with collective.navigationtoggle
  [laulaz]


0.7.31 (2016-07-26)
-------------------

- Fix error on homepage with ATEvent.
  [bsuttor]


0.7.30 (2016-07-26)
-------------------

- First step for not seeing old event in homepage with occurence events.
  [bsuttor]

- Fix ascii error on see_all method.
  [bsuttor]

- Get address form related_contacts with way collective.contact.core work.
  [bsuttor]

- Add category on indexview.
  [bsuttor]


0.7.29 (2016-07-20)
-------------------

- Force OrderedSelectFieldWidget for related contact fields.
  [bsuttor]


0.7.28 (2016-07-05)
-------------------

- Fix ascii error on contact field vocabulary.
  [bsuttor]

- Improve tests.
  [bsuttor]


0.7.27 (2016-07-01)
-------------------

- Fix translations.
  [bsuttor]


0.7.25 (2016-06-30)
-------------------

- Improve vocabulary field naming for related contacts behaviors.
  [bsuttor]

- Check if FTI exist before getting its behaviors.
  [bsuttor]


0.7.24 (2016-06-28)
-------------------

- Fix folder view if no lead image on collection.
  [bsuttor]


0.7.23 (2016-06-28)
-------------------

- Use link_text into folderview and add tests
  [bsuttor]


0.7.22 (2016-06-27)
-------------------

- Add index_view_keywords option.
  [bsuttor]


0.7.21 (2016-06-27)
-------------------

- Use dynamic collection image scale.
  [bsuttor]

- Add missing space in copyright sentence
  [laulaz]

- Use the same url to the image in the portlet.
  [jfroche]


0.7.20 (2016-06-22)
-------------------

- Use navigation root instead of context for getting footer viewlet static file.
  [bsuttor]

- Update field selectionnable for related contacts.
  [bsuttor]

- Fix tuples list bug.
  [boulch, gbastien]


0.7.19 (2016-06-03)
-------------------

- Fix related_contatcs vocabulary.
  [bsuttor]


0.7.18 (2016-06-03)
-------------------

- Add homepage behavior for collection.
  [bsuttor]


0.7.17 (2016-06-02)
-------------------

- Add related contacts fields vocabulary and use it.
  [bsuttor]

- Add monkey patches for DatetimeWidget and DateWidget to use min and max
  values from zope schema field
  [mpeeters]


0.7.16 (2016-06-01)
-------------------

- Add remove_behavior.
  [bsuttor]


0.7.15 (2016-05-25)
-------------------

- Hid Plone subject (categorization) with css.
  [bsuttor]


0.7.14 (2016-05-23)
-------------------

- Add related contacts viewlets (above and below).
  [bsuttor]

- Add related contacts behavior.
  [bsuttor]


0.7.13 (2016-05-19)
-------------------

- Rename homepage leadimage container class.
  [bsuttor]


0.7.12 (2016-05-18)
-------------------

- Hid new Dexterity leadimage.
  [bsuttor]

- Update tests for using DX.
  [bsuttor]

- Add media viewlet tests.
  [bsuttor]


0.7.11 (2016-04-29)
-------------------

- Improve way to get albums for DX content types.
  [bsuttor]


0.7.10 (2016-04-27)
-------------------

- Fix media viewlet for AT.
  [bsuttor]


0.7.9 (2016-04-25)
------------------

- Add keyword homepage behavior.
  [bsuttor]

- Get leadimage for media viewlet album for DX.
  [bsuttor]

- Add opendata view
  [bsuttor]

- Fix typo error on videos folder id.
  [bsuttor]


0.7.8 (2016-03-22)
------------------

- Add override of registryreader for cpskin tags
  [bsuttor]


0.7.7 (2016-03-08)
------------------

- Remove collective.z3cform.widgets.
  [bsuttor]


0.7.6 (2016-03-08)
------------------

- Add collective.z3cform.widgets for plone subjects.
  [bsuttor]


0.7.5 (2016-02-19)
------------------

- Remove bad import.
  [bsuttor]


0.7.4 (2016-02-19)
------------------

- View only published objects on homepage.
  [bsuttor]


0.7.3 (2016-01-22)
------------------

- Remove bad <a> tag on folder_view for leadimage.
  [bsuttor]


0.7.2 (2016-01-21)
------------------

- Add translation for events, a-la-une and new folder.
  [bsuttor]

- Use new way to excliude from nav which work with dx and at
  [bsuttor]

- Fix default value of slider_value to 5000 milliseconds.
  [bsuttor]


0.7.1 (2016-01-12)
------------------

- Fix footer link to "libre".
  [bsuttor]


0.7.0 (2016-01-12)
------------------

- Index view can now take lead image from plone.app.contenttypes Images for News and Events collection
  [bsuttor]

- Folder view inherits plone app contenttypes FolderView instead of BrowserView.
  [bsuttor]

- Add behavior for I am tag.
  [bsuttor]

- Do not hid other editor than ckeditor on installation.
  [bsuttor]

- Add folderview (index) for LRF content type
  [bsuttor]

- Remove dependency on collective.contentleadimage, it's now a behiavior for Dexterity. I leave dependency on setup.py for backward compatibility.
  [bsuttor]

- Improve comptability with Dexterity during setup.
  [bsuttor]

- Remove plone.app.collection installation, we use plone.app.contenttypes now ...
  [bsuttor]


0.6.7 (2015-11-24)
------------------

- Add dx profile.
  [bsuttor]


- Check 'Modify portal content' permission for viewing [Modifier la zone statique]
  [bsuttor]


0.6.6 (2015-10-02)
------------------

- Add minisite menu viewlet.
  [bsuttor]


0.6.5 (2015-09-29)
------------------

- Fix portlet visible level for minisite objects.
  [bsuttor]


0.6.4 (2015-09-28)
------------------

- Portlet navigation is no visible on minisite homepage.
  [bsuttor]


0.6.3 (2015-09-28)
------------------

- Add sub menu persistance option.
  [schminitz]


0.6.2 (2015-08-26)
------------------

- Fix bad encoded cpskin.core.socialviewlet registry
  [bsuttor]


0.6.1 (2015-08-18)
------------------

- Add date if it's a Event on faceted-preview view
  [bsuttor]

- Add new param for cpkin: city_name.
  [bsuttor]


0.6.0 (2015-08-07)
------------------

- Add css for hidding breathcrumb on homepage
  [bsuttor]

- Add not found exception for cpskinlogo search.
  [bsuttor]

- Add upgrade step which add footer viewlets
  [bsuttor]

- Add imio footer
  [bsuttor]


0.5.10 (2015-07-29)
-------------------

- Fix batch error on eea faceted leadimage view
  [bsuttor]


0.5.9 (2015-06-12)
------------------

- Make default slider timer to 5000 instead of 3000
  [bsuttor]


0.5.8 (2015-05-13)
------------------

- Add static portlet permissions to Portlets Manager role.
  [bsuttor]

- Upgrade step for adding static portlet permissions to Portlets Manager role.
  [bsuttor]


0.5.7 (2015-03-12)
------------------

- Use `Enable autologin as  Site Administrator` into robot tests.
  [bsuttor]

- Add possibility to choose flexslider parameters (imio #9515)
  [schminitz]

- Set quickupload 'sim_upload_limit' to 1.
  [bsuttor]

- Make good way to get RSS link for homepage (content/@@syndication-util/rss_url)
  [bsuttor]


0.5.6 (2014-12-04)
------------------

- Allow keywords edition locally (affinitic #6068)
  [laulaz]
- Avoid resetting load_page_menu on (re)install / upgrade
  [laulaz]
- Fix translations with different defaults (see extender.py)
  [laulaz]
- Split configure_folderviews to allow external package to use it
  [schminitz]
- Always allow to filter collection on a-la-une hidden tag
  [schminitz]


0.5.5 (2014-11-14)
------------------

- Move * to * upgrade step to a specific profile. With collective.upgrade,
  we do not want start this kind of upgrade step.
  [bsuttor]


0.5.4 (2014-10-22)
------------------

- Performance improvements (affinitic #6008)
  [laulaz]


0.5.3 (2014-10-07)
------------------

- Readd marker interfaces for migration step (Menu tools viewlet)
  [bsuttor]


0.5.2 (2014-10-07)
------------------

- Remove MenuTools viewlet and add upgrade step (affinitic #6023)
  [laulaz]
- Add 'Portlets Manager' role to manage portlets and add role to local sharing
  tab (affinitic #5857).
  [laulaz]

- Add configuration action and ability to have big thumbnails in folder view
  (affinitic #5964).
  [laulaz]

- Minor folder view changes (affinitic #5967).
  [laulaz]

- Add local banner action (affinitic #5776).
  [FBruynbroeck]

- Indexer adapt now IItem (OFS) instead of IBaseContent (Archetype)
  [bsuttor]

0.5.1 (2014-09-02)
------------------

- Fix error if httpagentparser do not works.
  [bsuttor]


0.5 (2014-09-02)
----------------

- Add a regisrty and implements a property field for getting number of
  albums visible on media viewlet.
  [bsuttor]

- Add faceted-preview-leadimage for collection.
  [bsuttor]

- Use a macros for homepage collection view.
  [bsuttor]

- Check if slider is compatible with browser (not compatible with IE < 10).
  If not compatible use homepage collection macros instead of slider.
  [bsuttor]

0.4 (2014-08-21)
----------------

- Remove target blank from minisite logo link
  [bsuttor]


0.2 (2014-08-21)
----------------

- Add standard tag to replace Plone's Subject tag (affinitic #5873)
- Navigation takes care of 4th level (affinitic #5785)
- Banner improvements with logo, link, ... (affinitic #5851)
- Index view complete rewrite with content choosing/ordering (affinitic #5843)


0.1 (2014-07-02)
----------------

- Initial release
