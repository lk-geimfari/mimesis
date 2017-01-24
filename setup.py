import os
from distutils.core import setup

from elizabeth import __version__, \
    __author__

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'pypi_readme.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

setup(
    name='elizabeth',
    version=__version__,
    packages=['elizabeth', 'elizabeth.core', 'elizabeth.core.interdata', 'elizabeth.builtins'],
    keywords=['fake', 'data', 'testing', 'generate', 'elizabeth', 'db', 'church', 'dummy'],
    package_data={
        'elizabeth': [
            'data/*/*',
        ]
    },
    url='https://github.com/lk-geimfari/elizabeth',
    license='MIT',
    author=__author__,
    author_email='likid.geimfari@gmail.com',
    description='Elizabeth is a fast and easy to use Python library '
                'for generating dummy data for a variety of purposes.',
    long_description=long_description,
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
