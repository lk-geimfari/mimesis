.. _tips:

Tricks and Tips
===============

This section contains some tricks and tips for using Mimesis.

Dealing with ORM
----------------

If you need to generate data and import it into a database we strongly
recommend generating data in chunks rather than *600k* at once. Keep
in mind the possible limitations of databases, ORM, etc. The smaller the
generated data chunks are, the faster the process will go. Below you can
see an abstract example of a `Django command <https://docs.djangoproject.com/en/2.2/howto/custom-management-commands/>`_ which uses Mimesis to bootstrap database.

Good:

.. code:: text

    ~ python manage.py fill_fake_db --count=1000 --locale=de

Very bad:

.. code:: text

    ~ python manage.py fill_fake_db --count=600000 --locale=de


For ORM integration, you might find it useful to use `mimesis-factory`_.


Test API Endpoints
------------------

You can create dummy API endpoints when you have not data,
but need them and know the structure of the endpoint's response.

Let's define the structure of the dummy response.

`dummy_endpoints.py`:

.. code-block:: python

    from mimesis.schema import Field, Schema
    from mimesis.locales import Locale
    from mimesis.enums import Gender

    _ = Field(Locale.EN)
    dummy_users = Schema(
        lambda: {
            'id': _('uuid'),
            'name': _('name', gender=Gender.MALE),
            'surname': _('surname', gender=Gender.MALE),
            'email': _('email'),
            'age': _('age'),
            'username': _('username', template='UU_d'),
            'occupation': _('occupation'),
            "address": {
                "street": _('street_name'),
                "city": _('city'),
                "zipcode": _('zip_code'),
            },
        }
    )


Now, you can return unique response with JSON for each request.

Basically you need just create simple view, which returns `JsonResponse`:

.. code-block:: python

    from dummy_endpoints import dummy_users

    def users(request):
        dummy_data = dummy_users.create(iterations=1)
        return JsonResponse(dummy_data)

Response:

.. code-block:: json

    [
      {
        "id": "a46313ab-e218-41cb-deee-b9afd755a4dd",
        "name": "Wally",
        "surname": "Stein",
        "email": "artiller1855@yahoo.com",
        "age": 51,
        "username": "SystemicZeuzera_1985",
        "occupation": "Travel Courier",
        "address": {
          "street": "Lessing",
          "city": "Urbandale",
          "zipcode": "03983"
        }
      },
    ]


Integration with 3rd-party libraries
--------------------------------------

- `mimesis-factory`_ - Integration with ``factory_boy``.
- `pytest-mimesis`_ - is a pytest plugin that provides pytest fixtures for Mimesis providers.

.. _mimesis-factory: https://github.com/mimesis-lab/mimesis-factory
.. _pytest-mimesis: https://github.com/pytest-dev/pytest-mimesis
