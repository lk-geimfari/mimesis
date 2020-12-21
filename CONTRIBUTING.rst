Contributing Guidelines
-----------------------

The `source code`_ and `issue tracker`_ are hosted on GitHub. *Mimesis*
is tested against Python 3.6 through 3.9 on `GitHub Actions`_ and `AppVeyor_`. Test coverage
is monitored with `Codecov`_.

Dependencies
~~~~~~~~~~~~

We use ``poetry`` to manage dependencies.
So, please do not use ``virtualenv`` or ``pip`` directly.
Before going any further, please,
take a moment to read the `official documentation <https://poetry.eustace.io/>`_
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

Every contributor must follow the `PEP8`_ code style.

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
Below you can see a great example of module:

.. code:: python

    """Demonstrate high quality docstrings.

    Module-level docstrings appear as the first "statement" in a module. Remember,
    that while strings are regular Python statements, comments are not, so an
    inline comment may precede the module-level docstring.

    After importing a module, you can access this special string object through the
    ``__doc__`` attribute; yes, it's actually available as a runtime attribute,
    despite not being given an explicit name! The ``__doc__`` attribute is also
    what is rendered when you call ``help()`` on a module, or really any other
    object in Python.

    You can also document a package using the module-level docstring in the
    package's ``__init__.py`` file.

    """


    class Example(object):
        """Illustrate class-level docstring.

        Classes use a special whitespace convention: the opening and closing quotes
        are preceded and followed by a blank line, respectively. No other
        docstrings should be preceded or followed by anything but code.

        A blank line at the end of a multi-line docstring before the closing
        quotation marks simply makes it easier for tooling to auto-format
        paragraphs (wrapping them at 79 characters, per PEP8), without the closing
        quotation marks interfering.

        """

        def __init__(self, *args, **kwargs) -> None:
            """Illustrate method-level docstring.

            All public callables should have docstrings, including magic methods
            like ``__init__()``.

            You'll notice that all these docstrings are wrapped in triple double
            quotes, as opposed to just "double quotes", 'single quotes', or
            '''triple single quotes.''' This is a convention for consistency and
            readability.

            ..note:: Note must look like that.

            :param foo: Description of foo.
            :param bar: Description of bar.

            """
            super().__init__(*args, **kwargs)

        def foo(self) -> str:
            """Return 'foo'.

            You can also specify summary with a lot of details about
            how the method works on multiple lines if it's really needed.

            :return: String ``foo``
            """
            return 'foo'


    def pi() -> float:
        """Illustrate function-level docstring.

        Note that all docstrings begin with a one-line summary. The summary is
        written in the imperative mood ("do", "use", "find", "return", "render",
        etc) and ends with a period. The method signature is not, in any way,
        duplicated into the comments (that would be difficult to maintain).

        All subsequent paragraphs in a docstring are indented exactly the same as
        the summary line. The same applies to the closing quotation marks.

        """
        return 3.14


Comment only things that are not obvious: hacks, optimizations, complex algorithms.
Obvious code does not require any additional comments.


Testing
~~~~~~~

You should write the test which shows that the bug was fixed or that the
feature works as expected, run test before you commit your changes to
the branch and create PR.

To run tests, simply:

.. code:: text

    ⟩ make test

Check out logs of GitHub Actions or AppVeyor if tests were failed on creating
PR, there you can find useful information.

The tests are randomly shuffled by pytest-randomly. To rerun the tests with the previous seed use:

.. code:: text

    ) make test SEED=last

If you want to specify a seed ahead of time use:

.. code:: text

    ) make test SEED=$int


Type checking
~~~~~~~~~~~~~

After adding every feature you should run the type checking and make
sure that everything is okay. You can do it using make:

::

    ⟩ make type-check

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
