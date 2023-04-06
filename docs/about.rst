About Mimesis
=============

What Mimesis is?
----------------

**Mimesis** provides a perfect solution for generating data. It effectively populates databases,
creates intricate JSON/XML files, and anonymizes productive service data.
If you require these functions, Mimesis is the ideal tool for you.

What Mimesis is Not?
--------------------

Mimesis was not created as an object factory intended for use with a specific database or
ORM (e.g., Django ORM, SQLAlchemy, etc.). However, this does not mean that it cannot be
used with an ORM. In fact, it can be easily integrated with an ORM using third-party libraries like `mimesis-factory <https://github.com/lk-geimfari/mimesis-factory>`_ or others.

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

Features
--------

The key features are:

- **Easy**: User-friendly data generator, with a simple design and clear documentation for easy and swift data generation.
- **Multilingual**: Mimesis generates data in a vast range of `languages <https://mimesis.name/en/latest/getting_started.html#supported-locales>`_, making it a multilingual tool that caters to numerous language requirements.
- **Performance**: Mimesis has excellent performance and is widely regarded as the fastest data generator among all Python solutions available.
- **Data variety**: Mimesis supports a broad range of data providers, including names, addresses, phone numbers, email addresses, dates, times, and more, enabling users to generate data for various purposes.
- **Country-specific data providers**: Mimesis supports country-specific data providers for generating country-specific data.
- **Extensibility**: Mimesis is extensible, allowing users to create and integrate their own data providers with the library, thus enabling them to generate custom datasets that meet their unique data generation requirements.
- **Generic data provider**: Mimesis provides a generic data provider that offers easy access to all the available data providers within the library from a single object, enabling the creation of customized data generation workflows with a simplified and streamlined approach.
- **Zero hard dependencies**: Mimesis has zero hard dependencies on external modules and does not require the installation of any libraries other than the Python standard library, making it easy to install and use.
- **Schema-based generators**: Mimesis provides schema-based data generators, offering an effortless way to produce data by the schema of any complexity. This feature enables users to generate customized data that follows a predefined structure or schema, making it especially helpful when creating test data for applications.


Advantages
----------

Compared to other similar libraries, such as Faker, this library offers several advantages, including:

-  **Performance**: It is notably faster than other similar libraries.
-  **Completeness**: It offers a wide range of detailed providers that generate various types of data.
-  **Simplicity**: It solely relies on the Python standard library and does not require any additional modules or dependencies.


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
