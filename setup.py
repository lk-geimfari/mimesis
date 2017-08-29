from distutils.core import setup

from mimesis import __author__, __version__

with open('PYPI_README.rst', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='mimesis',
    version=__version__,
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
    url='https://github.com/lk-geimfari/mimesis',
    license='MIT License',
    author=__author__,
    author_email='likid.geimfari@gmail.com',
    description='Mimesis: dummy data for developers.',
    long_description=readme,
    classifiers=[
        'Development Status :: 4 - Beta',
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
