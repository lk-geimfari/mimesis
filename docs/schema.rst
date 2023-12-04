.. _structured_data_generation:

==========================
Structured Data Generation
==========================

Schema and Field
----------------

For generating data by schema, just create an instance of :class:`~mimesis.schema.Field`
object, which takes any string which represents the name of data
provider in following formats:

- ``handler``/``method`` — the first custom field handler registered under the name ``handler`` will be chosen, or the first provider that has a method named ``method`` will be selected (See :ref:`api` to get the full list of available data providers and their methods).
- ``provider.method`` — explicitly defines that the method **method** belongs to **provider**


and **\**kwargs** of the method *method*, after that you should
describe the schema in lambda function (or any other callable object) and pass it to
the object :class:`~mimesis.schema.Schema` and call method :meth:`~mimesis.schema.Schema.create`.

.. warning::

    The `schema` **should be wrapped in a callable object** to ensure that it is evaluated
    dynamically, rather than just once, resulting in the same data being generated for each iteration.


Example of usage:

.. code:: python

    from mimesis import Field, Fieldset, Schema
    from mimesis.enums import Gender, TimestampFormat
    from mimesis.locales import Locale

    field = Field(locale=Locale.EN)
    fieldset = Fieldset(locale=Locale.EN)

    schema = Schema(
        schema=lambda: {
            "pk": field("increment"),
            "uid": field("uuid"),
            "name": field("text.word"),
            "version": field("version", pre_release=True),
            "timestamp": field("timestamp", fmt=TimestampFormat.POSIX),
            "owner": {
                "email": field("person.email", domains=["mimesis.name"]),
                "token": field("token_hex"),
                "creator": field("full_name", gender=Gender.FEMALE),
            },
            "apps": fieldset(
                "text.word", i=5, key=lambda name: {"name": name, "id": field("uuid")}
            ),
        },
        iterations=2,
    )
    schema.create()



Output:

.. code:: json

    [
      {
        "apps": [
          {
            "id": "680b1947-e747-44a5-aec2-3558491cac34",
            "name": "exit"
          },
          {
            "id": "2c030612-229a-4415-8caa-82e070604f02",
            "name": "requirement"
          }
        ],
        "name": "undergraduate",
        "owner": {
          "creator": "Temple Martinez",
          "email": "franklin1919@mimesis.name",
          "token": "18c9c17aa696fd502f27a1e9d5aff5a4e0394133491358fb85c59d07eafd2694"
        },
        "pk": 1,
        "timestamp": "2005-04-30T10:37:26Z",
        "uid": "1d30ca34-349b-4852-a9b8-dc2ecf6c7b20",
        "version": "0.4.8-alpha.11"
      },
      {
        "apps": [
          {
            "id": "e5505358-b090-4784-9148-f2acce8d3451",
            "name": "taste"
          },
          {
            "id": "2903c277-826d-4deb-9e71-7b9fe061fc3f",
            "name": "upcoming"
          }
        ],
        "name": "advisory",
        "owner": {
          "creator": "Arlena Moreno",
          "email": "progress2030@mimesis.name",
          "token": "72f0102513053cd8942eaa85c0e0ffea47eed424e40eeb9cb5ba0f45880c2893"
        },
        "pk": 2,
        "timestamp": "2021-02-24T04:46:00Z",
        "uid": "951cd971-a6a4-4cdc-9c7d-79a2245ac4a0",
        "version": "6.0.0-beta.5"
      }
    ]


By default, :class:`~mimesis.schema.Field` works only with providers which supported by :class:`~mimesis.Generic`,
to change this behavior should be passed parameter *providers* with a sequence of data providers:

.. code:: python

    from mimesis import builtins, Field
    from mimesis.locales import Locale

    custom_providers = (
         builtins.RussiaSpecProvider,
         builtins.NetherlandsSpecProvider,
    )
    field = Field(Locale.EN, providers=custom_providers)

    field('snils')
    # Output: '239-315-742-84'

    field('bsn')
    # Output: '657340522'


The scheme is an iterator, so you can iterate over it, for example like this:


.. code:: python

    from mimesis import Schema, Field
    from mimesis.locales import Locale

    field = Field(Locale.DE)

    schema = Schema(
        schema=lambda: {
            "pk": field("increment"),
            "name": field("full_name"),
            "email": field("email", domains=["example.org"]),
        },
        iterations=100,
    )


    for obj in schema:
        print(obj)

Output:

.. code:: text

    {'pk': 1, 'name': 'Lea Bohn', 'email': 'best2045@example.org'}
    ...
    {'pk': 100, 'name': 'Karsten Haase', 'email': 'dennis2024@example.org'}


Field vs Fieldset
-----------------

The main difference between :class:`~mimesis.schema.Field` and :class:`~mimesis.schema.Fieldset` is that
:class:`~mimesis.schema.Fieldset` generates a set (well, actually a ``list``) of values for a given field,
while :class:`~mimesis.schema.Field` generates a single value.

Let's take a look at the example:

.. code-block:: python

    >>> from mimesis import Field, Fieldset, Locale
    >>> field = Field(locale=Locale.EN)
    >>> fieldset = Fieldset(locale=Locale.EN)
    >>> field("name")
    Chase
    >>> fieldset("name", i=3)
    ['Basil', 'Carlee', 'Sheryll']

The keyword argument **i** is used to specify the number of values to generate.
If **i** is not specified, a reasonable default value (which is 10) is used.

The :class:`~mimesis.schema.Fieldset` class is a subclass of :class:`~mimesis.schema.BaseField` and inherits
all its methods, attributes and properties. This means that API of :class:`~mimesis.schema.Fieldset` is almost the same
as for :class:`~mimesis.schema.Field` which is also a subclass of :class:`~mimesis.schema.BaseField`.

Almost, because an instance of :class:`~mimesis.schema.Fieldset` accepts keyword argument **i**.

While it may not be necessary in most cases, it is possible to override the default name
of a keyword argument **i** for a specific field.

Let's take a look at the example:

.. code-block:: python

    >>> from mimesis import Fieldset, Locale
    >>> fs = Fieldset(locale=Locale.EN)
    >>> fs.fieldset_iterations_kwarg = "count"
    >>> fs("name", count=3)
    ['Janella', 'Beckie', 'Jeremiah']
    >>> fs("name", count=3, key=str.upper)
    ['RICKY', 'LEONORE', 'DORIAN']


Fieldset and Pandas
-------------------

If your aim is to create synthetic data for your `Pandas dataframes <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html>`_ ,
you can make use of the :class:`~mimesis.schema.Fieldset` as well.

With :class:`~mimesis.schema.Fieldset`, you can create datasets that are
similar in structure to your real-world data, allowing you to perform accurate
and reliable testing and analysis:

.. code-block:: python

    import pandas as pd
    from mimesis import Fieldset
    from mimesis.locales import Locale

    fs = Fieldset(locale=Locale.EN, i=5)

    df = pd.DataFrame.from_dict({
        "ID": fs("increment"),
        "Name": fs("person.full_name"),
        "Email": fs("email"),
        "Phone": fs("telephone", mask="+1 (###) #5#-7#9#"),
    })

    print(df)

Output:

.. code:: text

    ID             Name                          Email              Phone
    1     Jamal Woodard              ford1925@live.com  +1 (202) 752-7396
    2       Loma Farley               seq1926@live.com  +1 (762) 655-7893
    3  Kiersten Barrera      relationship1991@duck.com  +1 (588) 956-7099
    4   Jesus Frederick  troubleshooting1901@gmail.com  +1 (514) 255-7091
    5   Blondell Bolton       strongly2081@example.com  +1 (327) 952-7799


Key Functions
-------------

You can optionally apply a key function to the result returned by a **field**
or **fieldset**. To do this, simply pass a callable object that returns
the final result as the **key** parameter.

Let's take a look at the example:

.. code-block:: python

    >>> from mimesis import Field, Fieldset, Locale
    >>> field = Field(Locale.EN)
    >>> field("name", key=str.upper)
    'JAMES'

    >>> fieldset = Fieldset(i=3)
    >>> fieldset("name", key=str.upper)
    ['PETER', 'MARY', 'ROBERT']

As you can see, **key** function can be applied to both — **field** and **fieldset**.

Mimesis also provides a set of built-in key functions:

- :func:`~mimesis.keys.maybe` (See :ref:`key_maybe`)
- :func:`~mimesis.keys.romanize` (See :ref:`key_romanize`)

.. _key_maybe:


Maybe This, Maybe That
~~~~~~~~~~~~~~~~~~~~~~

Real-world data can be messy and may contain missing values.
This is why generating data with **None** values may be useful
to create more realistic synthetic data.

Luckily, you can achieve this by using key function :func:`~mimesis.keys.maybe`

It's has nothing to do with `monads <https://wiki.haskell.org/All_About_Monads>`_,
it is just a closure which accepts two arguments: **value** and **probability**.

Let's take a look at the example:

.. code-block:: python

    >>> from mimesis import Fieldset, Locale
    >>> from mimesis.keys import maybe
    >>> fieldset = Fieldset(Locale.EN, i=5)
    >>> fieldset("email", key=maybe(None, probability=0.6))

    [None, None, None, 'bobby1882@gmail.com', None]

In the example above, the probability of generating a **None** value instead of **email** is 0.6, which is 60%.

You can use any other value instead of **None**:

.. code-block:: python

    >>> from mimesis import Fieldset
    >>> from mimesis.keys import maybe
    >>> fieldset = Fieldset("en", i=5)
    >>> fieldset("email", key=maybe('N/A', probability=0.6))

    ['N/A', 'N/A', 'static1955@outlook.com', 'publish1929@live.com', 'command2060@yahoo.com']

.. _key_romanize:


Romanization of Cyrillic Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your locale is part of the Cyrillic language family, but you require locale-specific
data in romanized form, you can make use of the following key function :func:`~mimesis.keys.romanize`.

Let's take a look at the example:

.. code-block:: python

    >>> from mimesis.schema import Field, Fieldset, Locale
    >>> from mimesis.keys import romanize

    >>> fieldset = Fieldset(Locale.RU, i=5)
    >>> fieldset("name", key=romanize(Locale.RU))
    ['Gerasim', 'Magdalena', 'Konstantsija', 'Egor', 'Alisa']

    >>> field = Field(locale=Locale.UK)
    >>> field("full_name", key=romanize(Locale.UK))
    'Dem'jan Babarychenko'


At this moment :func:`~mimesis.keys.romanize` works only with Russian (**Locale.RU**),
Ukrainian (**Locale.UK**) and Kazakh (**Locale.KK**) locales.


Accessing Random Object in Key Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To ensure that all key functions have the same seed, it may be necessary to access a random object,
especially if you require a complex key function that involves performing additional tasks with **random** object.

In order to achieve this, you are required to create a **key function**
that accepts two parameters - ``result`` and ``random``.
The ``result`` argument denotes the output generated by the field,
while ``random`` is an instance of the :class:`~mimesis.random.Random`
class used to ensure that all key functions accessing random have the same seed.

Here is an example of how to do this:

.. code-block:: python

    >>> from mimesis import Field
    >>> from mimesis.locales import Locale

    >>> field = Field(Locale.EN, seed=42)
    >>> foobarify = lambda val, rand: rand.choice(["foo", "bar"]) + val

    >>> field("email", key=foobarify)
    'fooany1925@gmail.com'


Custom Field Handlers
---------------------

.. versionadded:: 11.0.0

.. note::

    We using :class:`~mimesis.schema.Field` in our examples, but all the features described
    below are available for :class:`~mimesis.schema.Fieldset` as well.

Sometimes, it's necessary to register custom fields or override existing ones to return custom data. This
can be achieved using **custom field handlers**.

A custom field handler can be any callable object. It should accept an instance of :class:`~mimesis.random.Random` as
its first argument, and **keyword arguments** (`**kwargs`) for the remaining arguments, returning the result.


.. warning::

    **Every** field handler must take a random instance as its first argument.
    This ensures it uses the same :class:`~mimesis.random.Random` instance as the rest of the library.

    Below you can see examples of valid signatures of field handlers:

    - ``field_handler(random, **kwargs)``
    - ``field_handler(random, a=None, b=None, c=None, **kwargs)``
    - ``field_handler(random, **{a: None, b: None, c: None})``

    The **main thing** is that the first argument must be positional (a random instance), and the rest must be **keyword arguments**.


Register Field Handler
~~~~~~~~~~~~~~~~~~~~~~

Suppose you want to create a field that returns a random value from a list of values. First, you need to
create a field handler. Let's call it ``my_field``.

.. code-block:: python

    def my_field(random, a=None, b=None) -> Any:
        return random.choice([a, b])


Afterwards, you need to register this field handler using a name you intend to use later. It's important to note
that **every** field handler must be registered using a unique name, otherwise, you will override an existing
field handler.

In this example, we will name the field ``hohoho``.

.. note::

    To avoid receiving a ``FieldNameError``, the field name must be a string that conforms to a valid Python identifier,
    i.e ``field_name.isidentifier()`` returns ``True``.

.. code-block:: python

    >>> from mimesis import Field

    >>> field = Field()
    >>> field.register_field("hohoho", my_field)
    >>> field("hohoho", a="a", b="b")
    'a'

Note that you can still use a `key function`, but the order of the arguments matters, so the field name comes first,
the `key function` second, and then the rest of the keyword arguments (`**kwargs`) that are passed to the field handler:

.. code-block:: python

    >>> field("hohoho", key=str.upper, a="a", b="b")
    'A'

You can register multiple fields at once:

.. code-block:: python

    >>> field.register_fields(
        fields=[
            ('mf1', my_field_1),
            ('mf2', my_field_2),
        ]
    )
    >>> field("mf1", key=str.lower)
    >>> field("mf2", key=str.upper)


Unregister Field Handler
~~~~~~~~~~~~~~~~~~~~~~~~

If you want to unregister a field handler, you can do it like this:

.. code-block:: python

    >>> field.unregister_field("hohoho")

Now you can't use it anymore and will get a ``FieldError`` if you try to do so.

If you'll attempt to unregister a field that was never registered then nothing going to happen:

.. code-block:: python

    >>> field.unregister_field("blabla") # nothing happens


It's pretty obvious that you can unregister multiple fields at once as well:

.. code-block:: python

    >>> field.unregister_fields(
        fields=[
            'wow',
            'much',
            'fields',
        ]
    )

or all fields at once:

.. code-block:: python

    >>> field.unregister_all_fields()


Export Data to JSON, CSV or Pickle
----------------------------------

Data can be exported in JSON or CSV formats, as well as pickled object representations.

Let's take a look at the example:

.. code-block:: python

    from mimesis.enums import TimestampFormat
    from mimesis.locales import Locale
    from mimesis.keys import maybe
    from mimesis.schema import Field, Schema

    field = Field(locale=Locale.EN)
    schema = Schema(
        schema=lambda: {
            "pk": field("increment"),
            "name": field("text.word", key=maybe("N/A", probability=0.2)),
            "version": field("version"),
            "timestamp": field("timestamp", TimestampFormat.RFC_3339),
        },
        iterations=1000
    )
    schema.to_csv(file_path='data.csv')
    schema.to_json(file_path='data.json')
    schema.to_pickle(file_path='data.obj')


Example of the content of ``data.csv`` (truncated):

.. code:: text

    pk,uid,name,version,timestamp
    1,save,6.8.6-alpha.3,2018-09-21T21:30:43Z
    2,sponsors,6.9.6-rc.7,2015-03-02T06:18:44Z
    3,N/A,4.5.6-rc.8,2022-03-31T02:56:15Z
    4,queen,9.0.6-alpha.11,2008-07-22T05:56:59Z
