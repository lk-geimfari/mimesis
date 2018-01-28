Foreword
========

This hopefully answers some questions about the purpose and goals of this library,
and when you should or should not be using one.


Advantages
----------
This library offers a number of advantages over other similar libraries, such as Faker:

-  Performance. Significantly faster than other similar libraries.
-  Completeness. Strives to provide many detailed providers that offer a variety of data generators.
-  Simplicity. Does not require any modules other than the Python standard library.


Comparison
----------
Below you can look how we compared performance.

Importing needing classes and creating instances:

.. code:: python

    import cProfile

    from mimesis import Personal
    from faker import Faker

    personal = Personal()
    faker = Faker()


Generate 10k full names
~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    # Generating using Mimesis:
    cProfile.run('[personal.full_name() for _ in range(10000)]')

    # Generating using Faker:
    cProfile.run('[faker.name() for _ in range(10000)]')

Result:

+----------+----------------------------------------+---------------------+------------------------+
| Library  | Method name                            | Iterations          |  Runtime (second)      |
+==========+========================================+=====================+========================+
|  Mimesis | :meth:`~mimesis.Personal.full_name`    | 10 000              |  0.254                 |
+----------+----------------------------------------+---------------------+------------------------+
|  Faker   | **Faker.name()**                       | 10 000              |  15.144                |
+----------+----------------------------------------+---------------------+------------------------+

Generate 10k last names
~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    # Generating using Mimesis:
    cProfile.run('[personal.last_name() for _ in range(10000)]')

    # Generating using Faker:
    cProfile.run('[faker.last_name() for _ in range(10000)]')


Result:

+----------+----------------------------------------+---------------------+------------------------+
| Library  | Method name                            | Iterations          |  Runtime (second)      |
+==========+========================================+=====================+========================+
|  Mimesis | :meth:`~mimesis.Personal.last_name`    | 10 000              |  0.040                 |
+----------+----------------------------------------+---------------------+------------------------+
|  Faker   | **Faker.last_name()**                  | 10 000              |  8.218                 |
+----------+----------------------------------------+---------------------+------------------------+


What does name mean?
--------------------

Mimesis (`/maɪˈmiːsəs/ <https://en.wikipedia.org/wiki/Help:IPA/English>`_;
`Ancient Greek <https://en.wikipedia.org/wiki/Ancient_Greek_language>`_: μίμησις (*mīmēsis*), from μιμεῖσθαι (*mīmeisthai*),
"to imitate", from μῖμος (mimos), "imitator, actor") is a critical and philosophical
term that carries a wide range of meanings, which include imitation, representation,
mimicry, imitatio, receptivity, nonsensuous similarity, the act of resembling,
the act of expression, and the presentation of the self.

Where should I use it?
----------------------

You can use Mimesis at any phase of development where you need mock data.
For example, you can use it to anonymize data taken from a production service,
populate a testing database, create beautiful JSON and XML files, etc.

In case, when an answer to the question "Does I really need mock data?" is negative,
then you absolutely don't need to use this library or another one alternative.
