=============
About Mimesis
=============

Features
--------

The key features are:

- **Multilingual**: Supports 43 different locales.
- **Extensibility**: Supports custom data providers and custom field handlers.
- **Ease of use**: Features a simple design and clear documentation for straightforward data generation.
- **Performance**: Widely recognized as the fastest data generator among Python solutions.
- **Data variety**: Includes various data providers designed for different use cases.
- **Schema-based generators**: Offers schema-based data generators to effortlessly produce data of any complexity.
- **Intuitive**: Great editor support. Fully-typed, thus autocompletion almost everywhere.

What Mimesis is?
----------------

**Mimesis** provides a perfect solution for generating data. It effectively populates databases,
creates intricate JSON/XML files, anonymizes productive service data, and generating high-quality
Pandas dataframes. If you require these functions, Mimesis is the ideal tool for you.

Mimesis **is not** an object factory intended for use with a specific database or ORM.
However, this does not mean that it cannot be used with an ORM. In fact, it can be easily
integrated with an ORM using third-party libraries like `mimesis-factory <https://github.com/lk-geimfari/mimesis-factory>`_ or others.

What is the fake data?
----------------------

Fake data refers to data that is not useful or sensitive, but is used to occupy a space
where real data is typically located. This type of data can act as a placeholder for both
testing and operational purposes. In testing, it can also serve as stubs or placeholders.

What does name mean?
--------------------

Mimesis (`/maɪˈmiːsəs/ <https://en.wikipedia.org/wiki/Help:IPA/English>`_;
`Ancient Greek <https://en.wikipedia.org/wiki/Ancient_Greek_language>`_: μίμησις (*mīmēsis*), from μιμεῖσθαι (*mīmeisthai*),
"to imitate", from μῖμος (mimos), "imitator, actor") is a term of critical and philosophical
significance, rooted in Ancient Greek, with various connotations such as imitation, representation,
mimicry, receptivity, nonsensuous similarity, resemblance, expression, and the presentation of the self.

Why octopus?
------------

Octopuses are fascinating creatures, and some families of octopuses
have incredible `mimicry <https://en.wikipedia.org/wiki/Mimicry>`_ abilities.
`Thaumoctopus mimicus <https://en.wikipedia.org/wiki/Mimic_octopus>`_ is a particularly
impressive example, and if you haven't heard of it yet, you should definitely read up on this remarkable species.

Check out that spotty bastard. Isn't it badass as hell?

.. image:: _static/thaumoctopus_mimicus.jpg
   :width: 700
   :target: https://mimesis.name/


Performance
-----------

Overall, Mimesis is many times faster (≈12 times faster) than Faker, and generates more unique data, which is important for testing.

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
