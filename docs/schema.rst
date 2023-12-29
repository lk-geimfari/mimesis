.. _structured_data_generation:

==========================
Structured Data Generation
==========================

Generating Data by Schema
-------------------------

For generating data by schema, just create an instance of :class:`~mimesis.schema.Field`
object, which takes any string which represents the name of data provider in following formats:

- ``handler``/``method`` — the first custom field handler registered under the name ``handler`` will be chosen, or the first provider that has a method named ``method`` will be selected (See :ref:`api` to get the full list of available data providers and their methods).
- ``provider.method`` — explicitly defines that the method **method** belongs to **provider**


and **\**kwargs** of the method *method*, after that you should
describe the schema in lambda function (or any other callable object) and pass it to
the object :class:`~mimesis.schema.Schema` and call method :meth:`~mimesis.schema.Schema.create`.

.. warning::

    The `schema` **should be wrapped in a callable object** to ensure that it is evaluated
    dynamically, rather than just once, resulting in the same data being generated for each iteration.


Let's consider an example to understand how it works:

.. code:: python

    from mimesis import Field, Fieldset, Schema
    from mimesis.enums import Gender, TimestampFormat
    from mimesis.locales import Locale

    field = Field(locale=Locale.EN)

    schema_definition = lambda: {
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
    }

    schema = Schema(schema=schema_definition, iterations=1)
    schema.create()


Output:

.. code:: json

    [
      {
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
      }
    ]


So, what's going on here?

1. Import the required classes and enums.
2. Create an instance of :class:`~mimesis.schema.Field` and pass the locale using the enum :class:`~mimesis.enums.Locale`.
3. Create a schema definition and wrap it in a callable object (``lambda`` function in this case).
4. Create an instance of :class:`~mimesis.schema.Schema` and pass the schema definition and the number of iterations.
5. Generate data using the method  :meth:`~mimesis.schema.Schema.create` of :class:`~mimesis.schema.Schema`.

If you're wondering where the data comes from, the answer is simple: the first argument passed to the ``field``
is actually the name of the method to be called.

This can be done explicitly, indicating the provider to which the method belongs, like this:

.. code:: python

    field("text.word")


or implicitly, like this:

.. code:: python

    field("increment")


In the latter case, the first provider that has a method named ``increment`` will be selected.


Generating a Set of Values
--------------------------

Sometimes it is necessary to generate a set of values for a given field instead of a single value.
This can be achieved using the :class:`~mimesis.schema.Fieldset` class which is very similar to :class:`~mimesis.schema.Field`.


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
Almost, because an instance of :class:`~mimesis.schema.Fieldset` accepts an additional keyword argument **i**.

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



Key Functions and Post-Processing
---------------------------------

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

    We use :class:`~mimesis.schema.Field` in our examples, but all the features described
    below are available for :class:`~mimesis.schema.Fieldset` as well.

Sometimes, it's necessary to register custom field handler or override existing ones to return custom data. This
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
create a callable object that handles field. Let's call it ``my_field``.

.. code-block:: python

    def my_field(random, a=None, b=None) -> Any:
        return random.choice([a, b])


Afterwards, you need to register it using a name you intend to use later. It's important to note
that **every** field handler must be registered using a unique name, otherwise, you will override an existing handler.

In this example, we will name the field ``hohoho``.

.. note::

    To avoid receiving a ``FieldNameError``, the field name must be a string that conforms to a valid Python identifier,
    i.e ``field_name.isidentifier()`` returns ``True``.

.. code-block:: python

    >>> from mimesis import Field

    >>> field = Field()
    >>> field.register_handler("hohoho", my_field)
    >>> field("hohoho", a="a", b="b")
    'a'


Note that you can still use a `key function`, but the order of the arguments matters, so the field name comes first,
the `key function` second, and then the rest of the keyword arguments (`**kwargs`) that are passed to the field handler:

.. code-block:: python

    >>> field("hohoho", key=str.upper, a="a", b="b")
    'A'

You can register multiple handlers at once:

.. code-block:: python

    >>> field.register_handlers(
        fields=[
            ('mf1', my_field_1),
            ('mf2', my_field_2),
        ]
    )
    >>> field("mf1", key=str.lower)
    >>> field("mf2", key=str.upper)


Register Field Handlers using Decorator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 12.0.0

.. note::

    Decorator `@handle` **can only be used with functions**, not with any callable object.

You can also register field handlers using decorator ``@handle('field_name')`` that takes the name of the field as an argument.

Let's take a look at the example:

.. code-block:: python

    >>> from mimesis import Field

    >>> field = Field()
    >>> @field.handle("my_field")
    ... def my_field(random, a=None, b=None) -> Any:
    ...     return random.choice([a, b])
    ...
    >>> field("my_field", a="a", b="b")
    'b'


When the field name is not specified, the name of the function (``func.__name__``) is used instead.


Unregister Field Handler
~~~~~~~~~~~~~~~~~~~~~~~~

If you want to unregister a field handler, you can do it like this:

.. code-block:: python

    >>> field.unregister_handler("hohoho")

Now you can't use it anymore and will get a ``FieldError`` if you try to do so.

If you'll attempt to unregister a field handler that was never registered then nothing going to happen:

.. code-block:: python

    >>> field.unregister_handler("blabla") # nothing happens


It's quite evident that you can also unregister multiple field handlers at once:

.. code-block:: python

    >>> field.unregister_handlers(
        fields=[
            'wow',
            'much',
            'fields',
        ]
    )

or all of them at once:

.. code-block:: python

    >>> field.unregister_all_handlers()


Exporting Data to Files
-----------------------

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

    pk,name,     version,        timestamp
    1, save,     6.8.6-alpha.3,  2018-09-21T21:30:43Z
    2, sponsors, 6.9.6-rc.7,     2015-03-02T06:18:44Z
    3, N/A,      4.5.6-rc.8,     2022-03-31T02:56:15Z
    4, queen,    9.0.6-alpha.11, 2008-07-22T05:56:59Z


Integrating with Pandas
-----------------------

If you're using `pandas <https://pandas.pydata.org/>`_, you can make use of the :class:`~mimesis.schema.Fieldset`.

With :class:`~mimesis.schema.Fieldset`, you can create dataframes that are similar in structure
to your real-world data, allowing you to perform accurate and reliable testing and analysis:

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


Integrating with Polars
-----------------------

If you're using `polars <https://pola.rs/>`_, you can make use of the :class:`~mimesis.schema.Fieldset` as well.

.. code-block:: python

    import polars as pl
    from mimesis import Fieldset
    from mimesis.locales import Locale

    fs = Fieldset(locale=Locale.EN, i=5)

    df = pl.DataFrame({
        "ID": fs("increment"),
        "Name": fs("person.full_name"),
        "Email": fs("email"),
        "Phone": fs("telephone", mask="+1 (###) #5#-7#9#"),
    })

    print(df)


Output:

.. code:: text

    ┌─────┬─────────────────┬─────────────────────────┬───────────────────┐
    │ ID  ┆ Name            ┆ Email                   ┆ Phone             │
    │ --- ┆ ---             ┆ ---                     ┆ ---               │
    │ i64 ┆ str             ┆ str                     ┆ str               │
    ╞═════╪═════════════════╪═════════════════════════╪═══════════════════╡
    │ 1   ┆ Terrell Mccall  ┆ chubby1964@duck.com     ┆ +1 (091) 353-7298 │
    │ 2   ┆ Peter Moran     ┆ nova1830@duck.com       ┆ +1 (332) 150-7298 │
    │ 3   ┆ Samira Shaw     ┆ george1804@example.org  ┆ +1 (877) 051-7098 │
    │ 4   ┆ Rolande Fischer ┆ edge2000@duck.com       ┆ +1 (767) 653-7792 │
    │ 5   ┆ Britt Gentry    ┆ neuromancer820@duck.com ┆ +1 (756) 258-7396 │
    └─────┴─────────────────┴─────────────────────────┴───────────────────┘
