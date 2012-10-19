from setuptools import setup, find_packages
import os.path

version = '4.3a3.dev0'

setup(name='Products.CMFPlone',
      version=version,
      description="The Plone Content Management System (core)",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "CHANGES.txt")).read(),
      classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Zope2",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        ],
      keywords='Plone CMF python Zope',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://plone.org/',
      license='GPL version 2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products', 'plone', 'plone.app'],
      include_package_data=True,
      zip_safe=False,
      extras_require=dict(
        test=[
          'Products.PloneTestCase',
          'zope.globalrequest',
          'zope.testing',
        ]),
      install_requires=[
          'setuptools',
          'Acquisition',
          'DateTime',
          'ExtensionClass',
          'Pillow',
          'Products.ATContentTypes >= 2.1.3',
          'Products.Archetypes',
          'Products.CMFActionIcons',
          'Products.CMFCalendar',
          'Products.CMFCore',
          'Products.CMFDefault',
          'Products.CMFDiffTool',
          'Products.CMFDynamicViewFTI',
          'Products.CMFEditions',
          'Products.CMFFormController',
          'Products.CMFPlone',
          'Products.CMFQuickInstallerTool',
          'Products.CMFUid',
          'Products.DCWorkflow',
          'Products.ExtendedPathIndex',
          'Products.ExternalEditor',
          'Products.GenericSetup >=1.4',
          'Products.MimetypesRegistry',
          'Products.PasswordResetTool',
          'Products.PlacelessTranslationService',
          'Products.PloneLanguageTool',
          'Products.PlonePAS',
          'Products.PluggableAuthService',
          'Products.PluginRegistry',
          'Products.PortalTransforms',
          'Products.ResourceRegistries',
          'Products.TinyMCE',
          'Products.statusmessages',
          'ZODB3',
          'Zope2 > 2.13.0',
          'archetypes.querywidget',
          'archetypes.referencebrowserwidget',
          'borg.localrole',
          'five.customerize',
          'five.formlib',
          'five.localsitemanager',
          'plone.app.blob',
          'plone.app.collection',
          'plone.app.content',
          'plone.app.contentlisting',
          'plone.app.contentmenu >= 1.1.6dev-r22380',
          'plone.app.contentrules',
          'plone.app.customerize',
          'plone.app.discussion',
          'plone.app.folder',
          'plone.app.form',
          'plone.app.i18n',
          'plone.app.jquery',
          'plone.app.jquerytools',
          'plone.app.layout >=1.1.7dev-r23744',
          'plone.app.linkintegrity >=1.0.3',
          'plone.app.locales',
          'plone.app.portlets',
          'plone.app.redirector',
          'plone.app.registry',
          'plone.app.search',
          'plone.app.upgrade',
          'plone.app.uuid',
          'plone.app.viewletmanager',
          'plone.app.vocabularies',
          'plone.app.workflow',
          'plone.batching',
          'plone.browserlayer >= 1.0rc4',
          'plone.contentrules',
          'plone.fieldsets',
          'plone.i18n',
          'plone.indexer',
          'plone.intelligenttext',
          'plone.locking',
          'plone.memoize',
          'plone.portlet.collection',
          'plone.portlet.static',
          'plone.portlets',
          'plone.protect > 1.0',
          'plone.registry',
          'plone.session',
          'plone.theme',
          'plonetheme.classic',
          'plonetheme.sunburst',
          'transaction',
          'z3c.autoinclude',
          'zope.annotation',
          'zope.app.locales >= 3.6.0',
          'zope.cachedescriptors',
          'zope.component',
          'zope.container',
          'zope.deferredimport',
          'zope.deprecation',
          'zope.dottedname',
          'zope.event',
          'zope.formlib',
          'zope.i18n',
          'zope.i18nmessageid',
          'zope.interface',
          'zope.location',
          'zope.pagetemplate',
          'zope.publisher',
          'zope.ramcache',
          'zope.schema',
          'zope.site',
          'zope.structuredtext',
          'zope.tal',
          'zope.tales',
          'zope.testing',
          'zope.traversing',
      ],
      )
