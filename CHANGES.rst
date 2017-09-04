Changelog
=========

0.10.20 (unreleased)
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
