from distutils.core import setup

from elizabeth import __version__, \
    __author__

with open('_readme_pypi.rst', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='elizabeth',
    version=__version__,
    packages=['elizabeth', 'elizabeth.core', 'elizabeth.core.intd', 'elizabeth.builtins'],
    keywords=['fake', 'data', 'testing', 'generate', 'elizabeth', 'db', 'dummy'],
    package_data={
        'elizabeth': [
            'data/*/*',
        ]
    },
    url='https://github.com/lk-geimfari/elizabeth',
    license='MIT',
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
