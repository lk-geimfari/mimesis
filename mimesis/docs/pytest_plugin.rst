.. _pytest_plugin:

Integration with Pytest
=======================

.. versionadded:: 14.0.0

You no longer require any third-party packages to seamlessly integrate Mimesis with `pytest`.


Usage
-----

Using the personal provider as part of a test.

.. code-block:: python

    # your_module/__init__.py

    def validate_email(email):
        # code that validates an e-mail address
        return True


And your test file:

.. code-block:: python

    from your_module import validate_email

    def test_validate_email(mimesis):
        assert validate_email(mimesis('email'))



You can also specify locales:


.. code-block:: python

    from mimesis.locales import Locale

    @pytest.mark.parameterize('mimesis_locale', [Locale.DE])  # use German locale
    def test_create_user(mimesis):
        assert create_user(name=mimesis('full_name'))


    @pytest.mark.parameterize('mimesis_locale', [Locale.DE, Locale.EN, Locale.JP])  # test multiple locales
    def test_add_phone(user, mimesis):
        assert user.add_phone_number(name=mimesis('full_name'))



Fixtures
--------

We offer two public fixtures: `mimesis_locale` and `mimesis`. While `mimesis_locale` is
an enum object (e.g., `Locale.EN`, `Locale.RU`), `mimesis` is an instance of :class:`mimesis.schema.Field`.

See :class:`mimesis.enums.Locale`.


Impact on Test Speed
--------------------

We employ caching of Mimesis instances for various locales throughout the entire test session, making
the creation of new instances cost-effective.
