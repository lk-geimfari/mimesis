Contributing Guidelines
-----------------------

The `source code`_ and `issue tracker`_ are hosted on GitHub. *Mimesis*
is tested against Python 3.8 through 3.11 on **GitHub Actions** and **AppVeyor**.

Test coverage is monitored with `Codecov`_.

Manage Dependencies
~~~~~~~~~~~~~~~~~~~

We use ``poetry`` to manage dependencies.
So, please do not use ``virtualenv`` or ``pip`` directly.
Before going any further, please, take a moment to read the `official documentation <https://poetry.eustace.io/>`_
about ``poetry`` to know some basics.

Firstly, install ``poetry``, it is recommended to do so with ``pip``:

.. code::

  ~ ⟩ pip install poetry



Installing dependencies
~~~~~~~~~~~~~~~~~~~~~~~

Please, note that ``poetry`` will automatically create a ``virtualenv`` for
this project. It will use you current ``python`` version.
To install all existing dependencies run:

.. code:: bash

  poetry install

And to activate ``virtualenv`` created by ``poetry`` run:

.. code:: bash

  poetry shell

Adding new dependencies
~~~~~~~~~~~~~~~~~~~~~~~

To add a new dependency you can run:

- ``poetry add --dev pytest`` to install ``pytest`` as a development dependency

Code Style
~~~~~~~~~~

Every contributor must follow the `PEP8`_ code style. We're using ``black`` for formatting code.

Annotating
~~~~~~~~~~

We use optional static typing (`mypy`_). Every function and method
should be annotated.

Example of annotated function:

.. code:: python

    def plus(a: int = 0, b: int = 0) -> int:
        """Get sum of a and b.

        :param a: First number.
        :param b: Second number.
        :return: Sum of a and b.
        """
        return a + b

.. _source code: https://github.com/lk-geimfari/mimesis
.. _issue tracker: https://github.com/lk-geimfari/mimesis/issues
.. _AppVeyor: https://ci.appveyor.com/project/lk-geimfari/mimesis
.. _Codecov: https://codecov.io/gh/lk-geimfari/mimesis
.. _PEP8: https://www.python.org/dev/peps/pep-0008/
.. _mypy: https://github.com/python/mypy


Documenting
~~~~~~~~~~~

Always add docstrings for your modules, classes, methods and functions.

Comment only things that are not obvious: hacks, optimizations, complex algorithms.
Obvious code does not require any additional comments.


Testing
~~~~~~~

You should write the test which shows that the bug was fixed or that the
feature works as expected, run test before you commit your changes to
the branch and create PR.

To run tests, simply:

.. code:: text

    ⟩ poetry run pytest

Check out logs of **GitHub Actions** or **AppVeyor** if tests were failed on creating
PR, there you can find useful information.

The tests are randomly shuffled by ``pytest-randomly``. To rerun the tests with the previous seed use:

.. code:: text

    ) poetry run pytest --randomly-seed=last

If you want to specify a seed ahead of time use:

.. code:: text

    ) poetry run pytest --randomly-seed=$int


Type checking
~~~~~~~~~~~~~

After adding every feature you should run the type checking and make
sure that everything is okay. You can do it using the following command:

::

    ⟩ poetry run mypy mimesis/ tests/

Code Review
~~~~~~~~~~~

Contributions will not be merged until they’ve been code reviewed by one
of our reviewers. In the event that you object to the code review
feedback, you should make your case clearly and calmly. If, after doing
so, the feedback is judged to still apply, you must either apply the
feedback or withdraw your contribution.

Questions
~~~~~~~~~

The GitHub issue tracker is for bug reports and feature requests. Please
do not create issue which does not related to features or bug reports.

New Locale
~~~~~~~~~~

Add following files to the directory ``mimesis/data/{LOCALE_CODE}/``:

``address.json``:

.. code:: json

   {
     "address_fmt": "{st_num} {st_name} {st_sfx}",
     "city": [
       "Test"
     ],
     "continent": [
       "Test"
     ],
     "country": {
       "current_locale": "Test",
       "name": [
         "Test"
       ]
     },
     "postal_code_fmt": "#####",
     "state": {
       "abbr": [
         "Test"
       ],
       "name": [
         "Test"
       ]
     },
     "street": {
       "name": [
         "Test"
       ],
       "suffix": [
         "Test"
       ]
     }
   }


``builtin.json``:

.. code:: json

   {
     "any": {
       "structure": [
         "which",
         "you",
         "need"
       ]
     }
   }

``business.json``:

.. code:: json

   {
     "company": {
       "name": [
         "Test"
       ],
       "type": {
         "abbr": [
           "Test"
         ],
         "title": [
           "Test"
         ]
       }
     },
     "currency-code": "Test",
     "price-format": "# Test",
     "numeric-decimal": ".",
     "numeric-thousands": ",",
     "numeric-frac-digits": 2
   }


``datetime.json``:

.. code:: json

   {
     "day": {
       "abbr": [
         "Test"
       ],
       "name": [
         "Test"
       ]
     },
     "formats": {
       "date": "%m/%d/%Y",
       "time": "%H:%M:%S"
     },
     "month": {
       "abbr": [
         "Test"
       ],
       "name": [
         "Test"
       ]
     },
     "periodicity": [
       "Test"
     ]
   }

``food.json``:

.. code:: json

   {
     "dishes": [
       "Test"
     ],
     "drinks": [
       "Test"
     ],
     "fruits": [
       "Test"
     ],
     "spices": [
       "Test"
     ],
     "vegetables": [
       "Test"
     ]
   }


``person.json``:

.. code:: json

   {
     "academic_degree": [
       "Test"
     ],
     "gender": [
       "Test"
     ],
     "language": [
       "Test"
     ],
     "names": {
       "female": [
         "Test"
       ],
       "male": [
         "Test"
       ]
     },
     "__COMMENT_NATIONALITY__": "Optional -> nationality: {female: [], male: []}",
     "nationality": [
       "Test"
     ],
     "occupation": [
       "Test"
     ],
     "political_views": [
       "Test"
     ],
     "__COMMENT_SURNAMES__": "Optional -> surnames: {female: [], male: []}",
     "surnames": [
       "Test"
     ],
     "title": {
       "female": {
         "typical": [
           "Test"
         ],
         "academic": [
           "Test"
         ]
       },
       "male": {
         "typical": [
           "Test"
         ],
         "academic": [
           "Test"
         ]
       }
     },
     "university": [
       "Test"
     ],
     "views_on": [
       "Test"
     ],
     "worldview": [
       "Test"
     ],
     "telephone_fmt": [
       "###-###-####",
       "(###) ###-####",
       "1-###-###-####"
     ]
   }


``text.json``:

.. code:: json

   {
     "alphabet": {
       "uppercase": [
         "Test"
       ],
       "lowercase": [
         "Test"
       ]
     },
     "answers": [
       "Yes",
       "No",
       "Maybe"
     ],
     "color": [
       "Test"
     ],
     "level": [
       "low",
       "moderate",
       "high",
       "very high",
       "extreme",
       "critical"
     ],
     "quotes": [
       "Test"
     ],
     "text": [
       "Test"
     ],
     "words": {
       "bad": [
         "Test"
       ],
       "normal": [
         "Test"
       ]
     }
   }



We have created a directory with a real structure which you can use as
great example ``mimesis/data/locale_template`` if you want to add a new
locale.

Releases
~~~~~~~~

We use **GitHub Actions** for automatically creating releases. The package
will be published on PyPi after pushing the new **tag** to the master
branch. The new release can be approved or disapproved by maintainers of
this project. If the new release was disapproved, then maintainer should
justify why the new release cannot be created.


Summary
~~~~~~~

-  Add one change per one commit.
-  Always comment your code (only in English!).
-  Check your spelling and grammar.
-  Run the tests after each commit.
-  Make sure the tests pass.
-  Make sure that type check is passed.
-  If you add any functionality, then you should add tests for it.
-  Annotate your code.
-  Do not write bad code!
