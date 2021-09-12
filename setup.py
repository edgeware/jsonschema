#!/usr/bin/env python
#:coding=utf-8:
#:tabSize=2:indentSize=2:noTabs=true:
#:folding=explicit:collapseFolds=1:

import sys

from setuptools import setup, find_packages

if sys.version < '2.3':
    sys.exit('Error: Python-2.3 or newer is required. Current version:\n %s' % sys.version)


VERSION = '0.2.3'
DESCRIPTION = "json-schema validator for Python"
LONG_DESCRIPTION = """
jsonschema is a complete, full featured validator for json-schema
adhering to the json-schema proposal second draft.
<http://groups.google.com/group/json-schema/web/json-schema-proposal---second-draft>.

jsonschema is written in pure python and currently has no dependencies.

Validators may be subclassed much like simplejson encoders to provide
special functionality or extensions.

jsonschema currently supports ascii and utf-8 json and schema documents.
"""

CLASSIFIERS = map(str.strip,
"""
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Topic :: Software Development :: Libraries :: Python Modules
Programming Language :: Python
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3.5
""".splitlines())

setup(name='jsonschema-edgeware',
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author='Ian Lewis',
      author_email='IanLewis@member.fsf.org',
      url='http://hg.monologista.jp/json-schema',
      license="MIT License",
      platforms=["any"],
      install_requires=['six'],
      packages=find_packages(),
      test_suite="jsonschema.tests",
      zip_safe=True
     )
