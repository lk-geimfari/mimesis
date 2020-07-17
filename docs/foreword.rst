Foreword
========

Advantages
----------
This library offers a number of advantages over other similar libraries, such as Faker:

-  Performance. Significantly faster than other similar libraries.
-  Completeness. Strives to provide many detailed providers that offer a variety of data generators.
-  Simplicity. Does not require any modules other than the Python standard library.


Performance
-----------

Below you can see the result of `performance comparison <https://gist.github.com/lk-geimfari/99c5b45906be5299a3088f42c3f55bf4>`_ of Mimesis and Faker:


Generating 10k full names
~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------------------------------------+---------------------+------------------------+------------------------+
| Library  | Method name                            | Iterations          |  Uniqueness            |  Runtime (in seconds)  |
+==========+========================================+=====================+========================+========================+
|  Mimesis | :meth:`~mimesis.Person.full_name`      | 10 000              |  9988 (99.88%)         |  0.137                 |
+----------+----------------------------------------+---------------------+------------------------+------------------------+
|  Faker   | **Faker.name()**                       | 10 000              |  9363 (93.63%)         |  1.758                 |
+----------+----------------------------------------+---------------------+------------------------+------------------------+

Generating 100k full names
~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------------------------------------+---------------------+------------------------+------------------------+
| Library  | Method name                            | Iterations          |  Uniqueness            |  Runtime (in seconds)  |
+==========+========================================+=====================+========================+========================+
|  Mimesis | :meth:`~mimesis.Person.full_name`      | 100 000             |  98 265 (98.27%)       |  1.344                 |
+----------+----------------------------------------+---------------------+------------------------+------------------------+
|  Faker   | **Faker.name()**                       | 100 000             |  71 067 (71.07%)       |  17.375                |
+----------+----------------------------------------+---------------------+------------------------+------------------------+

Generating 1 million full names
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------------------------------------+---------------------+------------------------+------------------------+
| Library  | Method name                            | Iterations          |  Uniqueness            |  Runtime (in seconds)  |
+==========+========================================+=====================+========================+========================+
|  Mimesis | :meth:`~mimesis.Person.full_name`      | 1 000 000           |  847 645 (84.76%)      |  13.685                |
+----------+----------------------------------------+---------------------+------------------------+------------------------+
|  Faker   | **Faker.name()**                       | 1 000 000           |  330 166 (33.02%)      |  185.945               |
+----------+----------------------------------------+---------------------+------------------------+------------------------+


What does name mean?
--------------------

Mimesis (`/maɪˈmiːsəs/ <https://en.wikipedia.org/wiki/Help:IPA/English>`_;
`Ancient Greek <https://en.wikipedia.org/wiki/Ancient_Greek_language>`_: μίμησις (*mīmēsis*), from μιμεῖσθαι (*mīmeisthai*),
"to imitate", from μῖμος (mimos), "imitator, actor") is a critical and philosophical
term that carries a wide range of meanings, which include imitation, representation,
mimicry, imitatio, receptivity, nonsensuous similarity, the act of resembling,
the act of expression, and the presentation of the self.

Why octopus?
------------
Basically, because octopuses are cool guys, but also because of the
fantastic `mimicry <https://en.wikipedia.org/wiki/Mimicry>`_ abilities of some families of octopuses.
Have you ever hear about `Thaumoctopus mimicus <https://en.wikipedia.org/wiki/Mimic_octopus>`_?
Just read about that guy, because he is a really badass one.

What is the fake data?
----------------------

Fake data is a kind of data which is used in software development.

That data looks like real data, but it is not.

What Mimesis is, What Mimesis is Not
------------------------------------

The problem that **Mimesis** solves and solves it perfectly is generating data.
When you need to populate database, create complex structured JSON/XML files,
anonymize data taken from productive services then **Mimesis** is this is
exactly what you need.

**Mimesis** is **not object factory** and it was not developed for using with
specific database or ORM (such as Django ORM, SQLAlchemy etc.).
It does not mean that you can't use it with ORM on the contrary,
this will be done very simply, this only means that possibly you'll
need third-party libraries to do it, like `mimesis-factory` or another one.
