Glossary
--------

.. _glossary:

.. glossary::
    :sorted:

    field
        A string that represents a method of a data provider.

    fieldset
        A list of fields.

    provider
        A class that provides various data generators.

    locale
        A locale that represents country-specific data for locale-dependent data providers.

        See :py:class:`~mimesis.enums.Locale`

    localized provider
        A provider that depends on external JSON files with localized data.

    universal provider
        A provider without external dependencies that can be used for any locale.

    key function
        A callable that transforms the result of a field after generation.
        Key functions are applied using the ``key`` parameter in field operations.

        See :py:mod:`~mimesis.keys`

    field handler
        A custom callable that generates data for a field. Field handlers accept
        a :py:class:`~mimesis.random.Random` instance and keyword arguments, and can be
        registered using :py:meth:`~mimesis.schema.BaseField.register_handler` or
        the :py:meth:`~mimesis.schema.BaseField.handle` decorator.

    schema context
        A context object passed to schema transformation functions. It contains
        metadata about the current iteration (index, seed, custom data) and provides
        methods for accessing related schema data.

        See :py:class:`~mimesis.schema.SchemaContext`

    schema builder
        A builder class for creating related schemas with cross-references between them.
        It allows defining multiple named schemas and generating relational data.

        See :py:class:`~mimesis.schema.SchemaBuilder`
