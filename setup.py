# -*- coding: utf-8 -*-

import json
import os
from distutils.core import setup
from os.path import abspath, dirname, exists, getsize, join, relpath, splitext

import setuptools

from mimesis import (
    __author__,
    __author_email__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
)

here = abspath(dirname(__file__))


def get_readme():
    with open('README.rst', 'r', encoding='utf-8') as f:
        return f.read()


class Minimizer(setuptools.Command):
    """Minify content of all json files for all locales."""

    description = 'Minify content of all json files.'
    user_options = []

    def initialize_options(self):
        """Find all files of all locales."""
        self.paths = []
        self.separators = (',', ':')
        self.data_dir = join(here, 'mimesis', 'data')
        self.before_total = 0
        self.after_total = 0

        for root, _, files in os.walk(self.data_dir):
            for file in sorted(files):
                if splitext(file)[1] == '.json':
                    self.paths.append(join(
                        relpath(root, self.data_dir), file))

    def finalize_options(self):
        pass

    @staticmethod
    def size_of(num):
        for unit in ['B', 'KB', 'MB']:
            if abs(num) < 1024.0:
                return '%3.1f%s' % (num, unit)
            num = num / 1024.0
        return '%.1f' % num

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

        template = '\033[34m{}\033[0m : ' \
                   '\033[92mminimized\033[0m : ' \
                   '\033[33m{}\033[0m -> \033[92m{}\033[0m'

        print(template.format(json_file,
                              size_before, size_after))

    def run(self):
        """Start json minimizer and exit when all json files were minimized."""
        for rel_path in sorted(self.paths):
            file_path = join(self.data_dir, rel_path)
            self.minify(file_path)

        after = self.size_of(self.after_total)
        before = self.size_of(self.before_total)
        saved = self.size_of(self.before_total - self.after_total)

        template = '\nTotal: ' \
                   '\033[92m{}\033[0m -> \033[92m{}\033[0m. ' \
                   'Compressed: \033[92m{}\033[0m\n'

        print(template.format(before, after, saved))


setup(
    name=__title__,
    version=__version__,
    description=__description__,
    long_description=get_readme(),
    author=__author__,
    author_email=__author_email__,
    url=__url__,
    license=__license__,
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
        'faker',
    ],
    package_data={
        'mimesis': [
            'data/*/*',
            'py.typed',
        ],
    },
    exclude_package_data={
        'mimesis': [
            # It's for development.
            'data/locale_template/*',
        ],
    },
    data_files=[
        ('', ['LICENSE']),
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'Topic :: Utilities',
        'Topic :: Software Development',
        'Topic :: Software Development :: Testing',
        'License :: OSI Approved :: MIT License',
    ],
    cmdclass={
        'minify': Minimizer,
    },
)
