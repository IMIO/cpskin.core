Changelog
=========

0.8.12 (unreleased)
-------------------

- Nothing changed yet.


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
