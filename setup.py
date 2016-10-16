from distutils.core import setup

import church

setup(
    name='church',
    version=church.__version__,
    packages=['church'],
    keywords=['fake', 'data', 'testing',
              'generate', 'faker', 'church',
              'bootstrap', 'database'
              ],
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
    long_description="Church is a library to generate fake data."
                     "It's very useful when you need to bootstrap "
                     "your database.",
    classifiers=[
        "Development Status :: 4 - Beta",
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License',
        "Topic :: Software Development :: Testing",
    ],
)
