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
        A context object passed to :meth:`~mimesis.schema.Schema.map`
        transformation functions. It exposes the current item index, seed, and
        custom data set via :meth:`~mimesis.schema.Schema.with_context`.

        See :py:class:`~mimesis.schema.SchemaContext` and the guide section
        *Transforming Items with map() and SchemaContext* in :doc:`schema`.

    schema builder
        A declarative builder for generating related fake datasets with foreign
        keys, nested schemas, and automatic dependency resolution.

        See :py:class:`~mimesis.builder.SchemaBuilder`
