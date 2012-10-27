#!/usr/bin/env python
"""Distutils installer for extras."""

from distutils.core import setup
import os.path

import extras


def get_version():
    """Return the version of extras that we are building."""
    version = '.'.join(
        str(component) for component in extras.__version__[0:3])
    return version


def get_long_description():
    readme_path = os.path.join(
        os.path.dirname(__file__), 'README.rst')
    return open(manual_path).read()


setup(name='extras',
      author='Testing cabal',
      author_email='testtools-dev@lists.launchpad.net',
      url='https://github.com/testing-cabal/extras',
      description=('Useful extra bits for Python - things that shold be '
        'in the standard library'),
      long_description=get_long_description(),
      version=get_version(),
      classifiers=["License :: OSI Approved :: MIT License"],
      packages=[
        'extras',
        'extras.tests',
        ],
      cmdclass={'test': testtools.TestCommand})
