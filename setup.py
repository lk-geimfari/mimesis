"""
.. image:: http://bit.ly/2D9cp18

Mimesis
-------

**Mimesis** is a fast and easy to use the library for Python programming
language, which helps generate mock data for a variety of purposes in a
variety of languages. This data can be particularly useful during software
development and testing. For example, it could be used to populate a
testing database for a web application with user information such as
email addresses, usernames, first names, last names, etc.

Documentation
-------------

Mimesis is very simple to use, and the below examples should help you
get started. Complete documentation for Mimesis is available on `Read
the Docs`_.

.. _Read the Docs: http://mimesis.readthedocs.io/

Installation
------------

To install mimesis, simply use pip (or `pipenv <http://pipenv.org/>`_):

.. code:: bash

    ➜  ~ pip install mimesis

Getting started
---------------

As we said above, this library is really easy to use. A simple usage
example is given below:

.. code:: python

    >>> from mimesis import Personal
    >>> from mimesis.enums import Gender
    >>> person = Personal('en')

    >>> person.full_name(gender=Gender.FEMALE)
    'Antonetta Garrison'

    >>> person.occupation()
    'Backend Developer'

    >>> for template in ('U_d', 'U-d', 'l_d', 'l-d'):
    ...     person.username(template=template)

    'Adders_1893'
    'Abdel-1888'
    'constructor_1884'
    'chegre-2051'

Locales
-------

You can specify a locale when creating providers and they will return data that is appropriate for
the language or country associated with that locale. `Mimesis` currently includes support
for `33 different locales <http://mimesis.readthedocs.io/locales.html>`_.

Data Providers
--------------

List of supported data providers available `here <http://mimesis.readthedocs.io/providers.html>`_

"""

import json
import os
import re
import sys
from distutils.core import setup
from os.path import abspath, dirname, exists, getsize, join, relpath, splitext
from shutil import rmtree

from setuptools import Command
from setuptools.command.test import test as TestCommand

VERSION_MINOR_MAX = 10
VERSION_MICRO_MAX = 10

here = abspath(dirname(__file__))

about = {}
# Get meta-data from __version__.py
with open(join(here, 'mimesis', '__version__.py')) as f:
    exec(f.read(), about)


class BaseCommand(Command):
    description = ''
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        pass


class Upload(BaseCommand):
    """Support setup.py upload."""

    def run(self):
        try:
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))
        os.system('twine upload dist/*')
        sys.exit()


class Minimizer(BaseCommand):
    """Minify content of all json file for all locales.
    """

    def initialize_options(self):
        """Find all files of all locales.
        """

        self.paths = []
        self.data_path = '/mimesis/data'
        self.separators = (',', ':')
        self.data_dir = here + self.data_path
        self.before_total = 0
        self.after_total = 0

        for root, _, files in os.walk(self.data_dir):
            for file in sorted(files):
                if splitext(file)[1] == '.json':
                    self.paths.append(join(
                        relpath(root, self.data_dir),
                        file
                    ))

    @staticmethod
    def size_of(num):
        for unit in ['B', 'KB', 'MB']:
            if abs(num) < 1024.0:
                return "%3.1f%s" % (num, unit)
            num = num / 1024.0
        return "%.1f" % num

    def minify(self, file_path):
        size_before = getsize(file_path)
        self.before_total += size_before
        size_before = self.size_of(size_before)

        with open(file_path, 'r', 1) as f:
            json_text = json.loads(f.read())
            minimized = json.dumps(
                json_text, separators=self.separators, ensure_ascii=False)

        if len(file_path) > 0:
            output_path = abspath(file_path)
            abs_path = abspath(dirname(output_path))

            if not exists(abs_path):
                os.makedirs(abs_path)

            with open(output_path, 'w+', 1) as f:
                f.write(minimized)

        size_after = getsize(file_path)
        self.after_total += size_after
        size_after = self.size_of(size_after)

        json_file = '/'.join(file_path.split('/')[-2:])

        template = "\033[34m{}\033[0m : " \
                   "\033[92mminimized\033[0m : " \
                   "\033[33m{}\033[0m -> \033[92m{}\033[0m".format(
            json_file,
            size_before,
            size_after,
        )

        print(template)

    def run(self):
        """Start json minimizer and exit when all json
        files was minimized.
        """
        for rel_path in sorted(self.paths):
            file_path = join(self.data_dir, rel_path)
            self.minify(file_path)

        after = self.size_of(self.after_total)
        before = self.size_of(self.before_total)
        saved = self.size_of(self.before_total - self.after_total)

        template = '\nTotal: ' \
                   '\033[92m{}\033[0m -> \033[92m{}\033[0m. ' \
                   'Compressed: \033[92m{}\033[0m\n'.format(before, after, saved)

        print(template)


class Version(BaseCommand):
    """Custom command for versioning"""

    def initialize_options(self):
        self.current = about['__version__']
        print('Previous version: '
              '\033[33m{}\033[0m.\n'.format(self.current))

    @staticmethod
    def automatically(version):
        """Automatically increment version string.

        :param version: Current version.
        :return: Next version.
        """
        major, minor, micro = [
            int(i) for i in version.split('.')
        ]

        if VERSION_MICRO_MAX > micro:
            micro += 1
        elif VERSION_MICRO_MAX == micro:
            micro = 0
            minor += 1
        elif VERSION_MINOR_MAX > minor:
            minor += 1
        elif VERSION_MINOR_MAX == minor:
            micro, minor = 0, 0
            major += 1
        if VERSION_MINOR_MAX < minor:
            minor, micro = 0, 0
            major += 1

        return '.'.join([str(i) for i
                         in (major, minor, micro)])

    def rewrite(self, version=None):
        if not version:
            version = self.current

        with open(join(here, 'mimesis', '__version__.py'), 'r+') as f:
            version_str = '__version__ = \'{}\''.format(version)
            regexp = r'__version__ = .*'

            meta = re.sub(regexp, version_str, f.read())
            f.seek(0)
            f.write(meta)
            f.truncate()

        print('Updated! Current version is: '
              '\033[34m{}\033[0m.\n'.format(version))

        exit()

    def run(self):
        response = input('Are you sure? (yes/no): ')
        if response.lower() in ('yes', 'y'):
            self.rewrite(
                self.automatically(
                    self.current,
                ),
            )


setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=__doc__,
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    license=about['__license__'],
    packages=[
        'mimesis',
        'mimesis.data',
        'mimesis.data.int',
        'mimesis.builtins',
        'mimesis.providers',
    ],
    keywords=[
        'fake',
        'mock',
        'data',
        'populate',
        'database',
        'testing',
        'generate',
        'mimesis',
        'dummy',
    ],
    package_data={
        'mimesis': [
            'data/*/*',
        ],
    },
    exclude_package_data={
        'mimesis': [
            # It's for development.
            'data/locale_template/*'
        ],
    },
    data_files=[
        ('', ['LICENSE']),
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Topic :: Software Development :: Testing',
    ],
    cmdclass={
        'version': Version,
        'minify': Minimizer,
        'upload': Upload,
    },
)
