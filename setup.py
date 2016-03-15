from setuptools import setup, find_packages
import os

version = '0.1b'

setup(name='collective.ogtags',
      version=version,
      description="OpenGraph for plone4",
      long_description=open("README.md").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='OpenGraph tags facebook twitter linkedin',
      author='Diederik Veeze',
      author_email='d.veeze@zestsoftware.nl',
      url='https://zestsoftware.nl/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      paster_plugins=["ZopeSkel"],
      )
