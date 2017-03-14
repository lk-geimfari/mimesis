import codecs

from os.path import (
    abspath,
    dirname,
    join
)

from distutils.core import setup

from elizabeth import (
    __author__,
    __version__
)

with open('other/pypir.rst', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='elizabeth',
    version=__version__,
    packages=[
        'elizabeth',
        'elizabeth.core',
        'elizabeth.intd',
        'elizabeth.builtins'
    ],
    keywords=[
        'db',
        'fake',
        'data',
        'testing',
        'generate',
        'elizabeth',
        'dummy'
    ],
    package_data={
        'elizabeth': [
            'data/*/*'
        ]
    },
    data_files=[
        ("", ["LICENSE"])
    ],
    url='https://github.com/lk-geimfari/elizabeth',
    license='MIT License',
    author=__author__,
    author_email='likid.geimfari@gmail.com',
    description='Elizabeth: dummy data for you.',
    long_description=readme,
    classifiers=[
        "Development Status :: 4 - Beta",
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development',
        'Topic :: Software Development :: Testing',
    ],
)
