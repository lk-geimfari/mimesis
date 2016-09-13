from distutils.core import setup

from church import __version__

setup(
    name='church',
    version=__version__,
    packages=['church'],
    keywords=['fake', 'data', 'testing', 'generate', 'random'],
    package_data={
        'church': [
            'data/*/*',
        ]
    },
    url='https://github.com/lk-geimfari/church',
    license='MIT',
    author='Likid Geimfari',
    author_email='likid.geimfari@gmail.com',
    description='Library for fake data generation for testing.',
    classifiers=[
        "Development Status :: 3 - Alpha",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        "Topic :: Software Development :: Testing",
    ],
)
