from distutils.core import setup

import elizabeth

setup(
    name='elizabeth',
    version=elizabeth.__version__,
    packages=['elizabeth'],
    keywords=[
        'fake', 'data', 'testing',
        'generate', 'faker', 'elizabeth',
        'bootstrap', 'database', 'generic',
        'church', 'dummy'
    ],
    package_data={
        'elizabeth': [
            'data/*/*',
        ]
    },
    url='https://github.com/lk-geimfari/elizabeth',
    license='MIT',
    author=elizabeth.__author__,
    author_email='likid.geimfari@gmail.com',
    description='Elizabeth (ex Church) is a library that help you generate fake data.',
    long_description="Elizabeth (ex Church) is a library to generate fake data."
                     "It's very useful when you need to bootstrap "
                     "your database.",
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development',
        'Topic :: Software Development :: Testing',
    ],
)
