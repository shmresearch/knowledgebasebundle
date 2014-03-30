from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='shmresearch.knowledgebase',
      version=version,
      description="SHM Research KnowledgeeBase",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['shmresearch'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'plone.behavior',
          'plone.app.dexterity',
          'plone.app.referenceablebehavior',
          'plone.app.relationfield',
          'plone.app.textfield',
          
          'plone.namedfile[blobs]',
          'plone.formwidget.namedfile',
          'collective.z3cform.datagridfield',
          
          #'collective.z3cform.widgets',
          
          #'collective.miscbehaviors',
          #'collective.z3cform.datetimewidget>=1.1',
          'Products.ATCountryWidget',
           
          'z3c.jbot',
          'collective.js.datatables',
      ],
      extras_require={
        'test': ['plone.app.testing'],
        },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
