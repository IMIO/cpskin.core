Changelog
=========

0.5.10 (unreleased)
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
