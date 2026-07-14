.. _structured_data_generation:

==========================
Structured Data Generation
==========================

Introduction
------------

The classes :class:`~mimesis.schema.Field` and :class:`~mimesis.schema.Fieldset` are used for generating
structured data in conjunction with :class:`~mimesis.schema.Schema`.

- :class:`~mimesis.schema.Field` is used to generate a single value for a given field name.
- :class:`~mimesis.schema.Fieldset` is used to generate a set of values for a given field name.
- :class:`~mimesis.schema.Schema` is used to generate structured data using a schema definition.

Instances of :class:`~mimesis.schema.Field` and :class:`~mimesis.schema.Fieldset` are callable objects
that accept:

- A method name as the first argument (``name``)
- An optional ``key`` function as the second argument for transformations
  (see :ref:`key_functions`)
- Additional keyword arguments (``**kwargs``) passed to the underlying method

See :doc:`api` for more information about the available providers and their methods.

Generating a Single Value
-------------------------

To generate a single value for a field, instantiate the :class:`~mimesis.schema.Field` class:

.. code:: python

    >>> from mimesis import Field, Locale
    >>> field = Field(locale=Locale.EN)

You can then use this instance as an entry point to access all methods of the available providers:

.. code:: python

    >>> field("person.name")
    'Chase'
    >>> field("person.name", key=str.upper)
    'CHASE'


Field Names
-----------

There are two ways to specify field names: **explicit** and **implicit**.

Explicit Field Names
~~~~~~~~~~~~~~~~~~~~

The explicit approach specifies both the provider name and method name,
separated by a dot:

.. code:: python

    >>> from mimesis import Field
    >>> field = Field()
    >>> field("person.username", mask="U_d", drange=(100, 1000))


This code is equivalent to:

.. code:: python

    >>> from mimesis import Generic
    >>> generic = Generic()
    >>> generic.person.username(mask="U_d", drange=(100, 1000))


This approach is more verbose but more reliable, as it explicitly specifies
the provider and avoids method name collisions.

Implicit Field Names
~~~~~~~~~~~~~~~~~~~~

The implicit approach specifies only the method name without the provider:

.. code:: python

    >>> from mimesis import Field, Locale
    >>> field = Field(Locale.EN)
    >>> field("username", mask="U_d", drange=(100, 1000))


Mimesis will call either the first registered custom field handler named ``username``
or the first provider with a method of that name.

**Note:** Custom field handlers always take precedence over provider methods
when names match, due to their higher priority in the lookup order
(see :ref:`custom_field_handlers`).


Generating a Set of Values
--------------------------

Sometimes it's necessary to generate a set of values for a given field instead of a single value.
This can be achieved using the :class:`~mimesis.schema.Fieldset` class, which is very similar to :class:`~mimesis.schema.Field`.

The main difference is that :class:`~mimesis.schema.Fieldset` generates a list of values for a field,
while :class:`~mimesis.schema.Field` generates a single value.

Example:

.. code-block:: python

    >>> from mimesis import Fieldset, Locale
    >>> fieldset = Fieldset(locale=Locale.EN)
    >>> fieldset("name", i=3)
    ['Basil', 'Carlee', 'Sheryll']

The keyword argument **i** is used to specify the number of values to generate.
If **i** is not specified, the default value of 10 is used.

The :class:`~mimesis.schema.Fieldset` class is a subclass of :class:`~mimesis.schema.BaseField` and inherits
all its methods, attributes, and properties. This means the API of :class:`~mimesis.schema.Fieldset` is almost the same
as :class:`~mimesis.schema.Field`, which is also a subclass of :class:`~mimesis.schema.BaseField`.
The only difference is that :class:`~mimesis.schema.Fieldset` accepts an additional keyword argument **i**.

Customizing the Iteration Parameter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While not necessary in most cases, you can override the default iteration parameter name **i**
for a specific :class:`~mimesis.schema.Fieldset` instance.

Example:

.. code-block:: python

    >>> from mimesis import Fieldset, Locale
    >>> fs = Fieldset(locale=Locale.EN)
    >>> fs.fieldset_iterations_kwarg = "count"
    >>> fs("name", count=3)
    ['Janella', 'Beckie', 'Jeremiah']
    >>> fs("name", count=3, key=str.upper)
    ['RICKY', 'LEONORE', 'DORIAN']


Defining Schemas
----------------

Now that you understand how to use :class:`~mimesis.schema.Field` and :class:`~mimesis.schema.Fieldset`,
let's look at how to use them to generate structured data with :class:`~mimesis.schema.Schema`.

First, let's import the required classes and enums and create the necessary instances:

.. code:: python

    from mimesis import Field, Fieldset, Schema
    from mimesis.enums import Gender, TimestampFormat
    from mimesis.locales import Locale

    field = Field(Locale.EN, seed=0xff)
    fieldset = Fieldset(Locale.EN, seed=0xff)

Next, we need to define a schema:

.. warning::

    The schema **must be wrapped in a callable object** to ensure it is evaluated
    dynamically, rather than just once. Otherwise, the same data will be generated for each iteration.

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


Finally, create a :class:`~mimesis.schema.Schema` instance
and generate data using the :meth:`~mimesis.schema.Schema.create` method.

Here's the complete example:

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

.. _key_functions:

Key Functions and Transformations
---------------------------------

.. versionadded:: 19.0.0

The :mod:`mimesis.keys` module provides transformation functions that can be applied to field values
via the ``key`` parameter. These functions execute after value generation but before returning to the caller.

Example:

.. code-block:: python

    >>> from mimesis import Field, Fieldset, Locale
    >>> field = Field(Locale.EN)
    >>> field("name", key=str.upper)
    'JAMES'

    >>> fieldset = Fieldset(i=3)
    >>> fieldset("name", key=str.upper)
    ['PETER', 'MARY', 'ROBERT']

As you can see, a **key** function can be applied to both **field** and **fieldset**.

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

The :func:`~mimesis.keys.romanize` function transliterates strings from Cyrillic script to Latin (romanized) script.

Example:

.. code-block:: python

    >>> from mimesis.schema import Field, Fieldset, Locale
    >>> from mimesis.keys import romanize

    >>> fieldset = Fieldset(Locale.RU, i=5)
    >>> fieldset("name", key=romanize(Locale.RU))
    ['Gerasim', 'Magdalena', 'Konstantsija', 'Egor', 'Alisa']

    >>> field = Field(locale=Locale.UK)
    >>> field("full_name", key=romanize(Locale.UK))
    'Dem'jan Babarychenko'


Currently, :func:`~mimesis.keys.romanize` only works with Russian (**Locale.RU**),
Ukrainian (**Locale.UK**), and Kazakh (**Locale.KK**) locales.

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

The :func:`~mimesis.keys.wrap` function wraps a string with specified text before and after. By default,
it uses angle brackets (``<`` and ``>``), but you can specify custom delimiters.

.. code-block:: python

    >>> field("username", key=keys.wrap(before='<', after='>'))
    '<chain_1893>'

**prefix**

The :func:`~mimesis.keys.prefix` function adds text to the beginning of a string.
This is useful for adding prefixes to usernames, IDs, or other identifiers.

.. code-block:: python

    >>> field("word", key=keys.prefix('user_'))
    'user_metal'

**suffix**

The :func:`~mimesis.keys.suffix` function adds text to the end of a string.
This is commonly used for adding file extensions or domain suffixes.

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
(by default ``...``) when truncation occurs. This is useful for creating previews or
ensuring data fits within length constraints.

.. code-block:: python

    >>> field("sentence", key=keys.truncate(20, suffix=''))
    'Messages can be shor'

**remove_whitespace**

The :func:`~mimesis.keys.remove_whitespace` function removes all whitespace characters from a string,
including spaces, tabs, and newlines. This is useful for creating compact identifiers or tokens.

.. code-block:: python

    >>> field("full_name", key=keys.remove_whitespace)
    'KanishaBurch'

Encoding and Hashing
^^^^^^^^^^^^^^^^^^^^

**hash_with**

The :func:`~mimesis.keys.hash_with` function hashes a string using a specified algorithm from
Python's :mod:`hashlib` module. Supported algorithms include ``sha256``, ``sha1``, ``md5``,
``sha512``, and others available in :data:`hashlib.algorithms_available`.

This is useful for generating hashed passwords, checksums, or unique identifiers.

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

The :func:`~mimesis.keys.urlsafe_base64_encode` function encodes a string as URL-safe base64
by replacing characters that have special meaning in URLs (``+`` and ``/``) with URL-safe
alternatives (``-`` and ``_``).

.. code-block:: python

    >>> field("token_hex", key=keys.urlsafe_base64_encode)
    'SXQgaXMgYWxzbyBhIGdhcmJhZ2UtY29sbGVjdGVkIHJ1bnRpbWUgc3lzdGVtLg=='

.. _key_sequence_operations:

Sequence Operations
~~~~~~~~~~~~~~~~~~~

Key functions for working with sequences (lists and tuples). These functions help manipulate
collections of values generated by fieldsets or methods that return sequences.

**join**

The :func:`~mimesis.keys.join` function takes a list or tuple and joins all items into a single
string using the specified separator. By default, it uses ``", "`` as the separator, and each item
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
These provide powerful ways to combine multiple transformations or apply logic
to your data generation.

**maybe**

Real-world data can be messy and may contain missing values.
Generating data with **None** values can help create more realistic synthetic data.

You can achieve this using the :func:`~mimesis.keys.maybe` key function.

It has nothing to do with `monads <https://wiki.haskell.org/All_About_Monads>`_;
it's simply a closure accepting two arguments: **value** and **probability**.

Example:

.. code-block:: python

    >>> from mimesis import Fieldset, Locale
    >>> from mimesis.keys import maybe
    >>> fieldset = Fieldset(Locale.EN, i=5)
    >>> fieldset("email", key=maybe(None, probability=0.6))

    [None, None, None, 'bobby1882@gmail.com', None]

In the example above, the probability of generating a **None** value instead of an email is 0.6 (60%).

You can use any value instead of **None**:

.. code-block:: python

    >>> from mimesis import Fieldset
    >>> from mimesis.keys import maybe
    >>> fieldset = Fieldset("en", i=5)
    >>> fieldset("email", key=maybe('N/A', probability=0.6))

    ['N/A', 'N/A', 'static1955@outlook.com', 'publish1929@live.com', 'command2060@yahoo.com']


**redact**

The :func:`~mimesis.keys.redact` function replaces any generated value with a redaction marker.
By default, it uses ``"[REDACTED]"``, but you can specify any string.

This is useful for generating datasets where sensitive fields need to be masked or
for creating test data that simulates redacted documents.

Use it with :func:`~mimesis.keys.apply_if` to make it meaningful.

.. code-block:: python

    >>> field("password", key=keys.redact('[CLASSIFIED]'))
    '[CLASSIFIED]'


**apply_if**

The :func:`~mimesis.keys.apply_if` function conditionally applies a transformation based on a
predicate function. If the condition is true, it applies the first transform; if false,
it can optionally apply an alternative transform or return the value unchanged.

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
simpler functions. It's inspired by Elixir's pipe operator (``|>``).

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

Accessing the Random Instance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To ensure all key functions share the same seed, you may need to access the random object,
especially if you write a complex key function that performs additional operations with it.

To achieve this, create a **key function** that accepts two parameters: ``result`` and ``random``.
The ``result`` parameter represents the output generated by the field,
while ``random`` is an instance of the :class:`~mimesis.random.Random`
class, ensuring all key functions that use randomness share the same seed.

Here's an example:

.. code-block:: python

    >>> from mimesis import Field
    >>> from mimesis.locales import Locale

    >>> field = Field(Locale.EN, seed=42)
    >>> foobarify = lambda val, rand: rand.choice(["foo", "bar"]) + val

    >>> field("email", key=foobarify)
    'fooany1925@gmail.com'


Transforming Items with ``map()`` and ``SchemaContext``
-------------------------------------------------------

Keep the schema definition focused on **fake domain fields**. Use
:meth:`~mimesis.schema.Schema.map` when you still need **per-record
post-processing** after values are generated:

- derive fields from other fields
- reshape records for a destination format (API payload, ORM model, DataFrame row)
- rename, drop, or nest keys
- attach generation metadata that should not live inside the schema lambda

Transformers run in registration order and work with both
:meth:`~mimesis.schema.Schema.create` and lazy iteration
(``for item in schema``).

When to use ``map(item)`` vs ``map(item, ctx)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A transformer may accept either:

- ``item`` alone — enough when the output depends only on the generated record
- ``(item, ctx)`` — when you also need generation metadata from
  :class:`~mimesis.schema.SchemaContext`

:class:`~mimesis.schema.SchemaContext` provides:

- ``index`` — zero-based position of the current item
- ``iteration`` — one-based counter (``index + 1``)
- ``seed`` — schema seed for debugging or reproducible batch tags
- ``custom`` — shared values set with :meth:`~mimesis.schema.Schema.with_context`

Use context when you would otherwise reach for a mutable counter, outer
closures, or a separate ``enumerate(schema.create())`` step. Typical cases:

- number rows as they are generated
- stamp each record with tenant / environment / job IDs once for the whole run
- include the active seed in exported metadata without putting it in every field

Derive and enrich records
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from mimesis import Field, Schema
    from mimesis.locales import Locale

    field = Field(Locale.EN, seed=0xFF)

    schema = (
        Schema(
            lambda: {
                "id": field("increment"),
                "email": field("email"),
                "score": field("integer_number", start=1, end=100),
            },
            iterations=3,
        )
        # Depends only on the item:
        .map(lambda item: {**item, "passed": item["score"] >= 50})
        # Needs generation position from context:
        .map(lambda item, ctx: {
            **item,
            "row": ctx.index,
            "batch": ctx.iteration,
        })
    )

    schema.create()

Example output:

.. code-block:: json

    [
      {"id": 1, "email": "...", "score": 72, "passed": true, "row": 0, "batch": 1},
      {"id": 2, "email": "...", "score": 31, "passed": false, "row": 1, "batch": 2},
      {"id": 3, "email": "...", "score": 88, "passed": true, "row": 2, "batch": 3}
    ]

Attach shared run metadata with ``with_context``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:meth:`~mimesis.schema.Schema.with_context` stores values once for the whole
schema run. Transformers read them from ``ctx.custom``. Prefer this over
repeating constants in the schema lambda or closing over outer variables in
every ``.map()`` callback:

.. code-block:: python

    from mimesis import Field, Schema
    from mimesis.locales import Locale

    field = Field(Locale.EN, seed=0xFF)

    schema = (
        Schema(
            lambda: {
                "username": field("username"),
                "email": field("email"),
            },
            iterations=2,
            seed=0xFF,
        )
        .with_context(
            tenant="acme",
            environment="staging",
            source="seed-job",
        )
        .map(lambda item, ctx: {
            **item,
            "meta": {
                "tenant": ctx.custom["tenant"],
                "environment": ctx.custom["environment"],
                "source": ctx.custom["source"],
                "seed": ctx.seed,
                "index": ctx.index,
            },
        })
    )

    data = schema.create()
    # data[0]["meta"]["tenant"] == "acme"
    # data[0]["meta"]["index"] == 0
    # data[1]["meta"]["index"] == 1

.. note::

   Transformers are applied in the order they were registered with ``.map()``.
   Prefer small, focused transformers so each step does one job.

   Put fake domain data in the schema; use ``key=`` for per-field transforms;
   use ``.map()`` for per-record transforms; use ``SchemaContext`` when a
   transformer needs row position, seed, or shared run configuration.


.. _custom_field_handlers:

Custom Field Handlers
---------------------

.. versionadded:: 11.0.0

.. note::

    We use :class:`~mimesis.schema.Field` in our examples, but all the features described
    below are available for :class:`~mimesis.schema.Fieldset` as well.

Sometimes it's necessary to register custom field handlers or override existing ones to return custom data.
This can be achieved using **custom field handlers**.

A custom field handler can be any callable object. It should accept an instance of :class:`~mimesis.random.Random` as
its first argument and **keyword arguments** (``**kwargs``) for any remaining arguments, and return the result.


.. warning::

    **Every** field handler must accept a random instance as its first argument.
    This ensures it uses the same :class:`~mimesis.random.Random` instance as the rest of the library.

    Valid signatures for field handlers:

    - ``field_handler(random, **kwargs)``
    - ``field_handler(random, a=None, b=None, c=None, **kwargs)``
    - ``field_handler(random, **{a: None, b: None, c: None})``

    The key requirement is that the first argument must be positional (a random instance), and the rest must be **keyword arguments**.


Registering a Field Handler
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Suppose you want to create a field that returns a random value from a list of values. First, create
a callable object that handles the field. Let's call it ``my_field``.

.. code-block:: python

    def my_field(random, a=None, b=None) -> Any:
        return random.choice([a, b])


Next, register it using a name you intend to use later. Note that **every** field handler must be registered
with a unique name; otherwise, you will override an existing handler.

In this example, we'll name the field ``hohoho``.

.. note::

    To avoid a ``FieldNameError``, the field name must be a valid Python identifier,
    i.e., ``field_name.isidentifier()`` must return ``True``.

.. code-block:: python

    >>> from mimesis import Field

    >>> field = Field()
    >>> field.register_handler("hohoho", my_field)
    >>> field("hohoho", a="a", b="b")
    'a'


You can still use a key function, but the order of arguments matters: the field name comes first,
the key function second, followed by the keyword arguments (``**kwargs``) passed to the field handler:

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


Registering Handlers with Decorators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 12.0.0

.. note::

    The decorator ``@handle`` **can only be used with functions** and not with other callable objects.

You can also register field handlers using the ``@field.handle('field_name')`` decorator.

Example:

.. code-block:: python

    >>> from mimesis import Field

    >>> field = Field()
    >>> @field.handle("my_field")
    ... def my_field(random, a=None, b=None) -> Any:
    ...     return random.choice([a, b])
    ...
    >>> field("my_field", a="a", b="b")
    'b'


When no field name is specified, the function's name (``func.__name__``) is used instead.


Unregistering Field Handlers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To unregister a field handler:

.. code-block:: python

    >>> field.unregister_handler("hohoho")

Now you can't use it anymore and will get a ``FieldError`` if you try.

If you attempt to unregister a field handler that was never registered, nothing will happen:

.. code-block:: python

    >>> field.unregister_handler("blabla") # nothing happens


You can also unregister multiple field handlers at once:

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


Field Aliases
-------------

.. versionadded:: 12.0.0

Sometimes you need a field name that truly matches your domain, and that's when field aliases become useful.

To use field aliases, instantiate a :class:`~mimesis.schema.Field` or
:class:`~mimesis.schema.Fieldset` and update the ``aliases`` attribute (a :class:`dict`)
to map aliases to field names.

Example:

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
Jokes aside, while any string can work as an alias, it's wise to choose one that fits your domain or
context for clarity.

When you no longer need aliases, you can remove them individually like regular dictionary keys, or clear them all at once:

.. code-block:: python

    >>> field.aliases.pop('🇺🇸')

    # clear all aliases

    >>> field.aliases.clear()


Relational Schemas
------------------

.. versionadded:: 20.0.0

Use :class:`~mimesis.builder.SchemaBuilder` to generate related datasets with
foreign keys, nested documents, and automatic dependency resolution.

Basic Relational Example
~~~~~~~~~~~~~~~~~~~~~~~~

Create users and posts where each post references a user:

.. code-block:: python

    from mimesis import SchemaBuilder
    from mimesis.locales import Locale

    sb = SchemaBuilder(Locale.EN, seed=0xFF)

    users = sb.schema("users", {
        "id": sb.f("increment", accumulator="user"),
        "username": sb.f("username"),
        "email": sb.f("email"),
    })

    posts = sb.schema("posts", {
        "id": sb.f("increment", accumulator="post"),
        "title": sb.f("sentence"),
        "user_id": sb.ref(users).id,  # Foreign key to users
    })

    # Order of kwargs does not matter — dependencies are resolved automatically
    data = sb.create(posts=20, users=5)

    print(data["users"])  # 5 users
    print(data["posts"])  # 20 posts with valid user_id values

Schema References
~~~~~~~~~~~~~~~~~

``sb.schema()`` returns a :class:`~mimesis.builder.SchemaRef` that supports:

- **Foreign keys** — ``sb.ref(users).id`` picks a random field value from
  generated data
- **Whole records** — ``sb.ref(users)`` embeds a random full record
- **Nesting** — ``addresses(count=2)`` embeds generated items inline

.. code-block:: python

    addresses = sb.schema("addresses", {
        "city": sb.f("city"),
        "street": sb.f("street_name"),
    })

    customers = sb.schema("customers", {
        "id": sb.f("increment"),
        "name": sb.f("full_name"),
        "addresses": addresses(count=2),  # Nested documents
    })

    data = sb.create(customers=10)

.. note::
    Include every schema that is referenced via ``sb.ref()`` in the same
    ``create()`` call. Nested schemas used only via ``schema_ref(count=N)``
    do not need to be passed to ``create()``.

Lifecycle Helpers
~~~~~~~~~~~~~~~~~

:class:`~mimesis.builder.SchemaBuilder` provides a few helpers for controlling
state between runs:

- :meth:`~mimesis.builder.SchemaBuilder.reseed` — change the random seed
- :meth:`~mimesis.builder.SchemaBuilder.clear` — drop generated data, keep
  schema definitions
- :meth:`~mimesis.builder.SchemaBuilder.reset` — clear schemas and generated
  data

.. code-block:: python

    data_a = sb.create(users=5)
    sb.clear()
    data_b = sb.create(users=5)  # same schemas, fresh data

    sb.reseed(0xAB)
    data_c = sb.create(users=5)

    sb.reset()  # definitions are gone; call sb.schema() again

Complex Relational Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A multi-level graph with users, projects, and API keys:

.. code-block:: python

    from mimesis import SchemaBuilder
    from mimesis.enums import TimestampFormat
    from mimesis.locales import Locale

    sb = SchemaBuilder(Locale.EN, seed=0xFF)

    users = sb.schema("users", {
        "id": sb.f("increment", accumulator="user"),
        "username": sb.f("username"),
        "email": sb.f("email"),
        "created_at": sb.f("timestamp", fmt=TimestampFormat.POSIX),
    })

    projects = sb.schema("projects", {
        "id": sb.f("increment", accumulator="project"),
        "name": sb.f("word"),
        "version": sb.f("version"),
        "owner_id": sb.ref(users).id,
        "status": sb.choice(["active", "archived", "draft"]),
    })

    api_keys = sb.schema("api_keys", {
        "id": sb.f("uuid"),
        "key": sb.f("token_hex"),
        "project_id": sb.ref(projects).id,
        "created_at": sb.f("timestamp", fmt=TimestampFormat.POSIX),
    })

    data = sb.create(
        api_keys=10,
        projects=5,
        users=3,
    )

This will generate:

- 3 users
- 5 projects (each with a valid ``owner_id`` referencing a user)
- 10 API keys (each with a valid ``project_id`` referencing a project)

See also: :class:`~mimesis.builder.SchemaBuilder` API reference.


Performance Optimization
------------------------

When using :meth:`~mimesis.schema.Schema.create`, all values are evaluated immediately,
which impacts performance and memory usage for large datasets. Use the iteration protocol
of :class:`~mimesis.schema.Schema` for a more efficient approach.

Instead of eager evaluation:

.. code-block:: python

    data = schema.create()

Use lazy iteration:

.. code-block:: python

    for item in schema:  # or schema.iterator(), which is the same
        print(item)


This approach leads to significant memory savings and better performance when generating large datasets.
Lazy iteration is approximately 40–45% faster and 85–99%+ more memory-efficient,
with efficiency increasing at larger scales.

As a rule of thumb, if you plan to generate more than 10,000 items, or if your schema is highly complex,
use lazy iteration.

Exporting Data
--------------

Data can be exported to JSON, CSV, or pickle formats.

Example:

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


DataFrame Integration
---------------------

Pandas
~~~~~~

If you're using `pandas <https://pandas.pydata.org/>`_, you can leverage :class:`~mimesis.schema.Fieldset`.

With :class:`~mimesis.schema.Fieldset`, you can create DataFrames that mirror the structure
of your real-world data, enabling accurate and reliable testing and analysis:

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


Polars
~~~~~~

If you're using `polars <https://pola.rs/>`_, you can also leverage :class:`~mimesis.schema.Fieldset`.

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
