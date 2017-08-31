import os

from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))

# Long description.
with open('PYPI_README.rst', 'r', encoding='utf-8') as f:
    readme = f.read()

about = {}
# Get meta-data from __version__.py
with open(os.path.join(here, 'mimesis', '__version__.py')) as f:
    exec(f.read(), about)

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
)
