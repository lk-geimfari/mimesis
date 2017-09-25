from os import path

import re
from sys import exit, stdout

from distutils.core import setup
from setuptools import Command
from setuptools.command.test import test as TestCommand

here = path.abspath(path.dirname(__file__))

tests_requirements = [
    'pytest',
    'flake8-builtins',
    'flake8-commas',
    'flake8-quotes',
    'pytest-flake8',
]

# Long description.
with open('PYPI_README.rst', 'r', encoding='utf-8') as f:
    readme = f.read()

about = {}
# Get meta-data from __version__.py
with open(path.join(here, 'mimesis', '__version__.py')) as f:
    exec(f.read(), about)


class PyTest(TestCommand):
    """Custom command for running test using setup.py test"""

    user_options = [('pytest-args=', 'a', 'Arguments to pass to py.test')]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        exit(errno)


class Versioner(Command):
    """Custom command for versioning"""

    user_options = []

    def initialize_options(self):
        self.current = about['__version__']
        stdout.write(
            'Previous version: \033[33m{}\033[0m.\n'.format(
                self.current))

    def finalize_options(self):
        pass

    @staticmethod
    def automatically(version):
        """Automatically increment version string.

        :param version: Current version.
        :return: Next version.
        """
        major, minor, micro = [
            int(i) for i in version.split('.')
        ]

        # TODO: Refactor

        if 10 > micro:
            micro += 1
        elif 10 == micro:
            micro = 0
            minor += 1
        elif 10 > minor:
            minor += 1
        elif 10 == minor:
            micro, minor = 0, 0
            major += 1
        if 10 < minor:
            minor, micro = 0, 0
            major += 1

        return '.'.join([str(i) for i
                         in (major, minor, micro)])

    def rewrite(self, version=None):
        if not version:
            version = self.current

        with open(path.join(here, 'mimesis', '__version__.py'), 'r+') as f:
            version_str = '__version__ = \'{}\''.format(version)
            regexp = r'__version__ = .*'

            meta = re.sub(regexp, version_str, f.read())
            f.seek(0)
            f.write(meta)
            f.truncate()

        stdout.write(
            'Updated! Current version is: \033[34m{}\033[0m.\n'.format(
                version))

        exit(0)

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
    long_description=readme,
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    license=about['__license__'],
    packages=[
        'mimesis',
        'mimesis.data',
        'mimesis.data.int',
        'mimesis.builtins',
        'mimesis.constants',
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
    data_files=[
        ('', ['LICENSE',
              'PYPI_README.rst',
              ],
         ),
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Topic :: Software Development :: Testing',
    ],
    tests_require=tests_requirements,
    cmdclass={
        'test': PyTest,
        'versioner': Versioner,
    },
)
