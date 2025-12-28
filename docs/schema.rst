.. _structured_data_generation:

==========================
Structured Data Generation
==========================

Introduction
------------

The classes :class:`~mimesis.schema.Field` and :class:`~mimesis.schema.Fieldset` are used to generating
structured data in conjunction with :class:`~mimesis.schema.Schema`.

- :class:`~mimesis.schema.Field` is used to generate a single value for a given field name.
- :class:`~mimesis.schema.Fieldset` is used to generate a set of values for a given field name.
- :class:`~mimesis.schema.Schema` is used to generate structured data using a schema definition.

The instances of :class:`~mimesis.schema.Field` and :class:`~mimesis.schema.Fieldset` are callable objects
that accept the name of the method to be called as the first argument (``name``), the ``key`` argument (a key function)
as the second argument, and the remaining arguments as ``**kwargs`` passed to the method.

See :ref:`api` for more information about the available providers and their methods.

There are two ways to specify the field name: **explicit** and **implicit**. Let's take a look at each of them.

Explicit
~~~~~~~~

The explicit approach involves specifying the provider's name and the method name,
separated by a dot, like this:

.. code:: python

    >>> from mimesis import Field
    >>> field = Field()
    >>> field("person.username", mask="U_d", drange=(100, 1000))


This code is equivalent to:

.. code:: python

    >>> from mimesis import Generic
    >>> generic = Generic()
    >>> generic.person.username(mask="U_d", drange=(100, 1000))


The explicit way is more verbose but more reliable. It allows you to specify the
provider from which the method will be called, thereby avoiding method name collisions.

Implicit
~~~~~~~~

The implicit approach involves specifying only the method name without referencing
the provider's name, as shown below:

.. code:: python

    >>> from mimesis import Field, Locale
    >>> field = Field(Locale.EN)
    >>> field("username", mask="U_d", drange=(100, 1000))


In this scenario, the ``Mimesis`` will call either the first registered custom field handler
under ``username`` or the first provider with a method named ``username``.

To clarify, if you've registered a custom field handler with a name that matches any method
within a provider, the custom field handler will take precedence due to its higher priority
and will be called instead.


Generating a Single Value
-------------------------

To generate a single value for a specific field, you'll need to instantiate the :class:`~mimesis.schema.Field` class.

.. code:: python

    >>> from mimesis import Field, Locale
    >>> field = Field(locale=Locale.EN)

Then, you can use its instance as an entry point to access all the methods of the available providers:

.. code:: python

    >>> # Explicitly, like this:
    >>> field("person.name", key=str.upper, **kwargs)
    'Chase'
    >>> # Or implicitly, like this:
    >>> field("name", key=str.upper, **kwargs)


Generating a Set of Values
--------------------------

Sometimes it is necessary to generate a set of values for a given ``field`` instead of a single value.
This can be achieved using the :class:`~mimesis.schema.Fieldset` class which is very similar to :class:`~mimesis.schema.Field`.

The main difference between :class:`~mimesis.schema.Field` and :class:`~mimesis.schema.Fieldset` is that
:class:`~mimesis.schema.Fieldset` generates a set (well, actually a ``list``) of values for a given field,
while :class:`~mimesis.schema.Field` generates a single value.

Let's take a look at the example:

.. code-block:: python

    >>> from mimesis import Fieldset, Locale
    >>> fieldset = Fieldset(locale=Locale.EN)
    >>> fieldset("name", i=3)
    ['Basil', 'Carlee', 'Sheryll']

The keyword argument **i** is used to specify the number of values to generate.
If **i** is not specified, a reasonable default value (which is 10) is used.

The :class:`~mimesis.schema.Fieldset` class is a subclass of :class:`~mimesis.schema.BaseField` and inherits
all its methods, attributes and properties. This means that API of :class:`~mimesis.schema.Fieldset` is almost the same
as for :class:`~mimesis.schema.Field` which is also a subclass of :class:`~mimesis.schema.BaseField`.
Almost, because an instance of :class:`~mimesis.schema.Fieldset` accepts an additional keyword argument **i**.

Overriding the Default Keyword Argument for Fieldset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While it may not be necessary in most cases, it is possible to override the default name
of a keyword argument **i** for a specific instance of :class:`~mimesis.schema.Fieldset`.

Let's take a look at the example:

.. code-block:: python

    >>> from mimesis import Fieldset, Locale
    >>> fs = Fieldset(locale=Locale.EN)
    >>> fs.fieldset_iterations_kwarg = "count"
    >>> fs("name", count=3)
    ['Janella', 'Beckie', 'Jeremiah']
    >>> fs("name", count=3, key=str.upper)
    ['RICKY', 'LEONORE', 'DORIAN']



Schema Definition
-----------------

Now that you better understand how to use :class:`~mimesis.schema.Field` (and :class:`~mimesis.schema.Fieldset`),
let's take a look at how to use them to generate structured data using :class:`~mimesis.schema.Schema`.

Firstly, let's import the required classes and enums and create required instances:

.. code:: python

    from mimesis import Field, Fieldset, Schema
    from mimesis.enums import Gender, TimestampFormat
    from mimesis.locales import Locale

    field = Field(Locale.EN, seed=0xff)
    fieldset = Fieldset(Locale.EN, seed=0xff)

Afterwards, we need to define a schema:

.. warning::

    The `schema` **should be wrapped in a callable object** to ensure that it is evaluated
    dynamically, rather than just once, resulting in the same data being generated for each iteration.

.. code:: python

    schema_definition = lambda: {
        "pk": field("increment"),
        "uid": field("uuid"),
        "name": field("text.word"),
        "version": field("version"),
        "timestamp": field("timestamp", fmt=TimestampFormat.POSIX),
        "owner": {
            "email": field("person.email", domains=["mimesis.name"]),
            "creator": field("full_name", gender=Gender.FEMALE),
        },
        "apiKeys": fieldset("token_hex", key=lambda s: s[:16], i=3),
    }


Finally, you can create an instance of :class:`~mimesis.schema.Schema`
and generate data by invoking the :meth:`~mimesis.schema.Schema.create` method.

Let's put all these code pieces together.

.. code:: python

    from mimesis import Field, Fieldset, Schema
    from mimesis.enums import Gender, TimestampFormat
    from mimesis.locales import Locale

    field = Field(Locale.EN, seed=0xff)
    fieldset = Fieldset(Locale.EN, seed=0xff)

    schema_definition = lambda: {
        "pk": field("increment"),
        "uid": field("uuid"),
        "name": field("text.word"),
        "version": field("version"),
        "timestamp": field("timestamp", fmt=TimestampFormat.POSIX),
        "owner": {
            "email": field("person.email", domains=["mimesis.name"]),
            "creator": field("full_name", gender=Gender.FEMALE),
        },
        "apiKeys": fieldset("token_hex", key=lambda s: s[:16], i=3),
    }

    schema = Schema(schema=schema_definition, iterations=3)
    schema.create()

The final result will look like this:

.. code:: json

    [
      {
        "pk": 1,
        "uid": "adcb2a69-ee41-4266-8d63-7bc02a7f06dd",
        "name": "arrangement",
        "version": "5.64.79",
        "timestamp": 1718992237,
        "owner": {
          "email": "metabolism1990@mimesis.name",
          "token": "cff564302f38541063a5a8243ef3715aaabe6c88eecc2f54f323fb4daab15c43",
          "creator": "Dierdre Lee"
        },
        "apiKeys": [
          "e31fac793bbda801",
          "9b844ee2cd5e66cd",
          "c9dacc05c44e3a82"
        ]
      },
      {
        "pk": 2,
        "uid": "411929ec-f85b-46a8-b247-a1b99f066aad",
        "name": "paintings",
        "version": "4.99.61",
        "timestamp": 1729820023,
        "owner": {
          "email": "pioneer2099@mimesis.name",
          "token": "86ceabe478126d918532bc4324b3ba70dfbce2bd010117f4a07ddd114a11ee54",
          "creator": "Saran Willis"
        },
        "apiKeys": [
          "98a61b80f8d7510d",
          "eed10d63059c7ea6",
          "1b1003853da9cac6"
        ]
      },
      {
        "pk": 3,
        "uid": "4d281c07-8f08-446c-a673-8444ee4f963b",
        "name": "sec",
        "version": "12.68.56",
        "timestamp": 1722235048,
        "owner": {
          "email": "shapes2013@mimesis.name",
          "token": "458f1535d9a13180eace4a4128ff051facfb66d43798eb9ef428b7a5fd436bbb",
          "creator": "Carlos Lucas"
        },
        "apiKeys": [
          "a8bfaf1c1b3fc69b",
          "268a35c593483d2d",
          "f7ecb7f5dbe3cb6e"
        ]
      }
    ]

That's it! You've just generated structured data using Mimesis.

Efficient Data Generation
-------------------------

When using :meth:`~mimesis.schema.Schema.create`, all field and fieldset calls are evaluated immediately,
which affects performance when generating large datasets, since all values are generated upfront and
more memory is consumed. Use the iteration protocol of `Schema` to avoid this and achieve a more efficient approach.

So, instead of:

.. code-block:: python

    data = schema.create()

You can do this:

.. code-block:: python

    for item in schema: # or schema.iterator() which is the same
        print(item)


This will lead to significant memory savings and better performance when generating large datasets,
since lazy iteration is approximately 40–45% faster and 85–99%+ more memory-efficient,
with efficiency increasing at larger scales.

Universal rule of thumb: if you plan to generate more than 10,000 items or the schema complexity is high,
consider using lazy iteration.

Relational Schema
-----------------

.. versionadded:: 19.0.0

Mimesis 19.0 introduces powerful features for generating relational data with foreign key references
between different schemas. This is achieved through the :class:`~mimesis.schema.SchemaBuilder` class,
which allows you to define multiple schemas and create relationships between them.

Basic Relational Example
~~~~~~~~~~~~~~~~~~~~~~~~~

Here's a simple example of creating users and posts where each post references a user:

.. code-block:: python

    from mimesis import Field, Schema
    from mimesis.schema import SchemaBuilder
    from mimesis.locales import Locale

    field = Field(Locale.EN, seed=0xFF)
    builder = SchemaBuilder(seed=field.seed)

    # Define the users schema
    builder.define(
        "users",
        Schema(lambda: {
            "id": field("increment"),
            "username": field("username"),
            "email": field("email"),
        })
    )

    # Define the posts schema with a reference to users
    builder.define(
        "projects",
        Schema(lambda: {
            "id": field("increment"),
            "title": field("sentence"),
        })
        .map(lambda item, ctx: {
            **item,
            "user_id": ctx.pick_from("users", "id"),  # Reference to user
        })
    )

    # Create data
    data = builder.create(users=5, projects=20)

    # Access generated data
    print(data["users"])     # List of 5 users
    print(data["projects"])  # List of 20 projects with valid user_id references

Context Methods for Relational Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When using transformations inside a :class:`~mimesis.schema.SchemaBuilder`, the context object
provides special methods for working with relational data:

- ``ctx.pick_from(schema_name, field)`` - Pick a random value from a previously generated schema's field
- ``ctx.ref(schema_name)`` - Get all generated items from a schema

.. note::
    The schemas must be generated in the correct order. A schema can only reference
    schemas that were defined before it in the ``create()`` call.

Complex Relational Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here's a more complex example with three related schemas:

.. code-block:: python

    from mimesis.schema import Field, Schema, SchemaBuilder
    from mimesis.enums import TimestampFormat
    from mimesis.locales import Locale

    field = Field(Locale.EN, seed=0xFF)
    builder = SchemaBuilder(seed=0xFF)

    # Define users
    builder.define(
        "users",
        Schema(lambda: {
            "id": field("increment"),
            "username": field("username"),
            "email": field("email"),
            "created_at": field("timestamp", fmt=TimestampFormat.POSIX),
        })
    )

    # Define projects (owned by users)
    builder.define(
        "projects",
        Schema(lambda: {
            "id": field("increment"),
            "name": field("text.word"),
            "version": field("version"),
        })
        .map(lambda item, ctx: {
            **item,
            "owner_id": ctx.pick_from("users", "id"),
            "status": field.get_random_instance().choice(
                ["active", "archived", "draft"]
            ),
        })
    )

    # Define API keys (belong to projects, created by users)
    builder.define(
        "api_keys",
        Schema(lambda: {
            "id": field("increment"),
            "key": field("token_hex"),
            "created_at": field("timestamp", fmt=TimestampFormat.POSIX),
        })
        .map(lambda item, ctx: {
            **item,
            "project_id": ctx.pick_from("projects", "id"),
            "user_id": ctx.pick_from("users", "id"),
        })
    )

    # Generate all data with proper relationships
    data = builder.create(
        users=3,
        projects=5,
        api_keys=10
    )

This will generate:

- 3 users
- 5 projects (each with a valid ``owner_id`` referencing a user)
- 10 API keys (each with a valid ``project_id`` and ``user_id`` referencing projects and users)


Using Field Aliases
-------------------

.. versionadded:: 12.0.0

Sometimes, you need a field name that truly matches what your domain is about, and that's when field aliases become useful.

In order to utilize field aliases, it's necessary to instantiate either a :class:`~mimesis.schema.Field` or
:class:`~mimesis.schema.Fieldset` and then update the attribute ``aliases`` (essentially a regular :class:`dict`) to
associate aliases with field names.

Let's take a look at the example:

.. code-block:: python

    from mimesis import Field, Locale

    field = Field(Locale.EN)

    # The key is an alias, the value is the field
    # name to which the alias is associated (both should be strings).
    field.aliases.update({
        '🇺🇸': 'country',
        '🧬': 'dna_sequence',
        '📧': 'email',
        '📞': 'person.telephone',
        '🍆': 'vegetable',
        'ебаныйтокен': 'token_hex',
    })


You can now use aliases instead of standard field names:

.. code-block:: python

    >>> field("🇺🇸")
    'Iraq' # I swear this was generated randomly.
    >>> field("🧬")
    'ATTCTAGCAT'
    >>> field('📧', domains=['@gmail.com'])
    'walker1827@gmail.com'
    >>> field('📞')
    '+17181130182'
    >>> field('🍆')
    'Radicchio'
    >>> field('ебаныйтокен')
    'aef9765d029c91ac737d04119c94a2b52a52d34b61bc39bec393e82e7bf0b8b5'


As you can see, you can use any string as an alias, so I'm doing my part to get someone fired for emoji-driven code.
Putting jokes aside, although any string can work as an alias, it's wise to choose one that fits your domain or
context better to enhance clarity and comprehension.

When you no longer need aliases, you can remove them individually like regular dictionary keys or clear them all at once:

.. code-block:: python

    >>> field.aliases.pop('🇺🇸')

    # clear all aliases

    >>> field.aliases.clear()


Key Functions and Transformations
---------------------------------

.. versionadded:: 19.0.0

The :mod:`mimesis.keys` module provides transformation functions that can be applied to field values
using the ``key`` parameter in :class:`~mimesis.schema.Field` and :class:`~mimesis.schema.Fieldset`.
These functions are executed after a value is generated and before it's returned to the caller.

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

Although you can use any callable object as a key function, Mimesis provides a comprehensive
set of built-in key functions for various transformations:

- :ref:`key_string_transformations`
- :ref:`key_sequence_operations`
- :ref:`key_conditional_composition`

.. _key_string_transformations:

String Transformations
~~~~~~~~~~~~~~~~~~~~~~

Mimesis provides several key functions for transforming string values. These functions only accept
string types and will raise a :class:`TypeError` if a non-string value is provided.

Transliteration
^^^^^^^^^^^^^^^

**romanize**

The :func:`~mimesis.keys.romanize` is used to transliterate strings from Cyrillic script to Latin (romanized) script.

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

Case Conversion Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^

These functions transform strings between different naming conventions commonly used in programming.

**snake_case**

The :func:`~mimesis.keys.snake_case` function converts strings to snake_case format:

.. code-block:: python

    >>> field("occupation", key=keys.snake_case)
    'cab_driver'

**camelCase**

The :func:`~mimesis.keys.camel_case` function converts strings to camelCase format:

.. code-block:: python

    >>> field("full_name", key=keys.camel_case)
    'ellenaEstes'

**kebab-case / slugify**

The :func:`~mimesis.keys.kebab_case` (alias: :func:`~mimesis.keys.slugify`) function converts strings
to kebab-case format, creating URL-friendly slugs. It removes special characters, replaces spaces
with hyphens, and converts everything to lowercase.

.. code-block:: python

    >>> field("full_name", key=keys.kebab_case)
    'lou-wise'

Text Wrapping and Affixes
^^^^^^^^^^^^^^^^^^^^^^^^^^

These functions add text before, after, or around generated values.

**wrap**

The :func:`~mimesis.keys.wrap` function wraps a string with specified before and after text. By default,
it wraps with angle brackets (``<`` and ``>``), but you can specify custom delimiters.

.. code-block:: python

    >>> field("username", key=keys.wrap(before='<', after='>'))
    '<chain_1893>'

**prefix**

The :func:`~mimesis.keys.prefix` function adds text to the beginning of a string. This is useful
for adding prefixes to usernames, IDs, or other identifiers.

.. code-block:: python

    >>> field("word", key=keys.prefix('user_'))
    'user_metal'

**suffix**

The :func:`~mimesis.keys.suffix` function adds text to the end of a string. This is commonly used
for adding file extensions or domain suffixes.

.. code-block:: python

    >>> field("word", key=keys.suffix('.com'))
    'priorities.com'

String Manipulation
^^^^^^^^^^^^^^^^^^^

**reverse**

The :func:`~mimesis.keys.reverse` function reverses the characters in a string:

.. code-block:: python

    >>> field("word", key=keys.reverse)
    'olleh'

**truncate**

The :func:`~mimesis.keys.truncate` function limits a string to a maximum length, adding a suffix
(by default ``...``) when truncation occurs. This is useful for creating previews or ensuring
data fits within length constraints.

.. code-block:: python

    >>> field("sentence", key=keys.truncate(20, suffix=''))
    'Messages can be shor'

**remove_whitespace**

The :func:`~mimesis.keys.remove_whitespace` function removes all whitespace characters from a string,
including spaces, tabs, and newlines. This can be useful for creating compact identifiers or tokens.

.. code-block:: python

    >>> field("full_name", key=keys.remove_whitespace)
    'KanishaBurch'

Encoding and Hashing
^^^^^^^^^^^^^^^^^^^^

**hash_with**

The :func:`~mimesis.keys.hash_with` function hashes a string using a specified algorithm from
Python's :mod:`hashlib` module. Supported algorithms include ``sha256``, ``sha1``, ``md5``,
``sha512``, and others available in :data:`hashlib.algorithms_available`.

This is useful for creating hashed passwords, checksums, or unique identifiers.

.. code-block:: python

    >>> field("password", key=keys.hash_with('sha256'))
    '8742c08c354ea086510c5a6abf7f6ed8b938ad00b35c740c3f02d01b75f11d06'
    >>> field("email", key=keys.hash_with('blake2s'))
    '86167b4b002d323526088b837edc34223a404055b7ab8b6205957ab42325f752'

**base64_encode**

The :func:`~mimesis.keys.base64_encode` function encodes a string as base64:

.. code-block:: python

    >>> field("sentence", key=keys.base64_encode)
    'SSBkb24ndCBldmVuIGNhcmUu'

**urlsafe_base64_encode**

The :func:`~mimesis.keys.urlsafe_base64_encode` function encodes a string as URL-safe base64,
replacing characters that have special meaning in URLs (``+`` and ``/``) with URL-safe
alternatives (``-`` and ``_``).

.. code-block:: python

    >>> field("token_hex", key=keys.urlsafe_base64_encode)
    'SXQgaXMgYWxzbyBhIGdhcmJhZ2UtY29sbGVjdGVkIHJ1bnRpbWUgc3lzdGVtLg=='

.. _key_sequence_operations:

Sequence Operations
~~~~~~~~~~~~~~~~~~~

Key functions for working with sequences (lists and tuples). These functions help you manipulate
collections of values generated by fieldsets or methods that return sequences.

**join**

The :func:`~mimesis.keys.join` function takes a list or tuple and joins all items into a single
string using the specified separator. By default, it uses ``", "`` as the separator. Each item
is automatically converted to a string before joining.

This is particularly useful when working with :class:`~mimesis.schema.Fieldset` to combine
multiple generated values into a single formatted string.

.. code-block:: python

    >>> fieldset("words", key=keys.join(' | '))
    ['personals | errors', 'eyes | monday', 'kim | mn']

.. _key_conditional_composition:

Conditional and Composition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Advanced key functions that enable conditional transformations and function composition.
These functions provide powerful ways to combine multiple transformations or apply logic
to your data generation.

**maybe**

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


**redact**

The :func:`~mimesis.keys.redact` function replaces any generated value with a redaction marker.
By default, it uses ``"[REDACTED]"`` as the replacement, but you can specify any string.

This is useful for generating datasets where certain sensitive fields need to be masked or
for creating test data that simulates redacted documents.

Use it with ``apply_if`` to make it meaningful.

.. code-block:: python

    >>> field("password", key=keys.redact('[CLASSIFIED]'))
    '[CLASSIFIED]'


**apply_if**

The :func:`~mimesis.keys.apply_if` function conditionally applies a transformation based on a
predicate function. If the condition is true, it applies the first transform; if false,
it optionally applies an alternative transform or returns the value unchanged.

This enables dynamic data transformations based on the generated value's characteristics.

.. code-block:: python

    >>> field("integer_number", key=keys.apply_if(
    ...     lambda x: x > 100,
    ...     lambda x: x * 2,
    ...     lambda x: x / 2
    ... ))

    >>> # Mark long strings with a prefix
    >>> field("sentence", key=keys.apply_if(
    ...     lambda s: len(s) > 50,
    ...     keys.prefix('[LONG] '),
    ...     keys.prefix('[SHORT] ')
    ... ))
    '[LONG] This is a very long sentence...'

    >>> # Convert to uppercase only if it contains a digit
    >>> field("person.username", key=keys.apply_if(
    ...     lambda s: any(c.isdigit() for c in s),
    ...     str.upper
    ... ))
    'USER123'

**pipe**

The :func:`~mimesis.keys.pipe` function chains multiple key functions together, applying them
in sequence from left to right. The output of each function becomes the input to the next.

This is one of the most powerful key functions, enabling complex transformations by composing
simpler functions. It's inspired by Elixir's pipe operator (`|>`).

.. code-block:: python

    >>> field("full_name", key=keys.pipe(
    ...     str.lower,
    ...     keys.slugify,
    ...     keys.prefix('user-')
    ... ))
    'user-ken-hopper'

    >>> # Create a hashed, prefixed username
    >>> field("email", key=keys.pipe(
    ...     lambda s: s.split('@')[0],
    ...     keys.hash_with('md5'),
    ...     keys.prefix('usr_'),
    ...     lambda x: x[:16]
    ... ))
    'usr_5d2be58391f3'

    >>> # Complex transformation chain
    >>> field("sentence", key=keys.pipe(
    ...     str.lower,
    ...     keys.remove_whitespace,
    ...     keys.base64_encode
    ... ))
    'YW55ZWxlbWVudG9mYXR1cGxlY2FuYmVhY2Nlc3NlZGluY29uc3RhbnR0aW1lLg=='

The :func:`~mimesis.keys.pipe` function is compatible with all other key functions and can also
work with regular Python functions. It automatically handles functions that require a random
instance as their second parameter (like :func:`~mimesis.keys.maybe`).

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

    The decorator `@handle` **can only be used with functions** and not with any callable object.

You can also register field handlers using decorator ``@field.handle('field_name')`` that takes the name of the field as an argument.

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
