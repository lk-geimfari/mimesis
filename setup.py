from distutils.core import setup

from church import __version__

setup(
    name='church',
    version=__version__,
    packages=['church'],
    keywords=['fake', 'data', 'testing', 'generate', 'faker'],
    package_data={
        'church': [
            'data/*/*',
        ]
    },
    url='https://github.com/lk-geimfari/church',
    license='MIT',
    author='Likid Geimfari',
    author_email='likid.geimfari@gmail.com',
    description='Church is a library that help you generate fake data.',
    classifiers=[
        "Development Status :: 3 - Alpha",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        "Topic :: Software Development :: Testing",
    ],
)
