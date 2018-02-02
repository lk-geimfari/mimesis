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

    from mimesis import Person
    from faker import Faker

    person = Person()
    faker = Faker()


Generate 10k full names
~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    # Generating using Mimesis:
    cProfile.run('[person.full_name() for _ in range(10000)]')

    # Generating using Faker:
    cProfile.run('[faker.name() for _ in range(10000)]')

Result:

+----------+----------------------------------------+---------------------+------------------------+
| Library  | Method name                            | Iterations          |  Runtime (second)      |
+==========+========================================+=====================+========================+
|  Mimesis | :meth:`~mimesis.Person.full_name`      | 10 000              |  0.254                 |
+----------+----------------------------------------+---------------------+------------------------+
|  Faker   | **Faker.name()**                       | 10 000              |  15.144                |
+----------+----------------------------------------+---------------------+------------------------+

Generate 10k last names
~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    # Generating using Mimesis:
    cProfile.run('[person.last_name() for _ in range(10000)]')

    # Generating using Faker:
    cProfile.run('[faker.last_name() for _ in range(10000)]')


Result:

+----------+----------------------------------------+---------------------+------------------------+
| Library  | Method name                            | Iterations          |  Runtime (second)      |
+==========+========================================+=====================+========================+
|  Mimesis | :meth:`~mimesis.Person.last_name`      | 10 000              |  0.040                 |
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


What Mimesis is, What Mimesis is Not
------------------------------------

The problem that **Mimesis** solves and solves it perfectly is generating data.
When you need to populate database, create beautiful JSON or XML files,
anonymize data taken from productive services then **Mimesis** is this is
exactly what you need.

**Mimesis** is **not object factory** and it was not developed for using with
specific database or ORM (such as Django ORM, SQLAclhemy etc.).
It does not mean that you can't use it with ORM on the contrary,
this will be done very simply, this only means that possibly you'll
need third-party libraries to do it.
