# -*- coding: utf-8 -*-

version = '0.8.19.dev0'

from setuptools import setup, find_packages

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')

setup(name='cpskin.core',
      version=version,
      description='Core package for cpskin',
      long_description=long_description,
      classifiers=[
          "Environment :: Web Environment",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Framework :: Plone",
          "Framework :: Plone :: 4.2",
          "Framework :: Plone :: 4.3",
      ],
      keywords='',
      author='IMIO',
      author_email='support@imio.be',
      url='https://github.com/imio/cpskin.core',
      license='gpl',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.api',
          'plone.app.contenttypes',
          'Plone',
          'archetypes.schemaextender',
          'imio.ckeditortemplates',
          'collective.contentleadimage',
          'collective.directory',
          'collective.monkeypatcher',
          'cpskin.locales',
          'imio.media',
          'collective.plonetruegallery',
          'collective.geo.faceted',  # include collective.geo.leaflet
          'plone.behavior',
          'collective.sticky',
          'collective.quickupload',
          'wildcard.foldercontents',
          'eea.facetednavigation',
          'collective.iconifieddocumentactions',
          'collective.z3cform.keywordwidget',
          'httpagentparser',
          'cpskin.minisite',
          'collective.contact.core',
          'collective.taxonomy',
          'collective.navigationtoggle',
          'geocoder',
          'imio.dashboard',
      ],
      extras_require={
          'test': [
              'plone.app.robotframework',
          ]
      },
      entry_points={},
      )
