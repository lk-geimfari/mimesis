.. _factory_plugin:

Integration with factory_boy
============================

.. versionadded:: 15.0.0

You no longer require any third-party packages to integrate Mimesis with ``factory_boy``.

Mimesis requires ``factory_boy`` to be installed, but it's not a hard dependency.
Therefore, you'll need to install it manually, like this:

.. code-block:: bash

    poetry add --group dev factory_boy

Alternatively, you can include it as an extra when installing Mimesis itself, like so:

.. code-block:: bash

    poetry add --group dev mimesis[factory]


Utilization
-----------

Look at the example below and you’ll understand how it works:

.. code-block:: python

    class Account(object):
        def __init__(self, username, email, name, surname, age):
            self.username = username
            self.email = email
            self.name = name
            self.surname = surname
            self.age = age




Now, use the ``FactoryField`` class to define how fake data is generated:

.. code-block:: python

    import factory
    from mimesis.plugins.factory import FactoryField

    from account import Account

    class AccountFactory(factory.Factory):
        class Meta(object):
            model = Account

        username = FactoryField('username', template='l_d')
        name = FactoryField('name', gender='female')
        surname = FactoryField('surname', gender='female')
        age = FactoryField('age', minimum=18, maximum=90)
        email = factory.LazyAttribute(
            lambda instance: '{0}@example.org'.format(instance.username)
        )
        access_token = FactoryField('token', entropy=32)



See `factory_boy <https://factoryboy.readthedocs.io/>`_ documentation for more information about how to use factories.


Configuration
-------------

You can also define custom field handlers for your factories. To do this, you need to
define an attribute named ``field_handlers`` in the ``Params`` class of your factory.

Just like this:

.. code-block:: python

    import factory
    from mimesis.plugins.factory import FactoryField

    class FactoryWithCustomFieldHandlers(factory.Factory):
        class Meta(object):
            model = Guest # Your model here

        class Params(object):
            field_handlers = [
                ("num", lambda rand, **kwargs: rand.randint(1, 99)),
                ("nick", lambda rand, **kwargs: rand.choice(["john", "alice"])),
            ]

        age = FactoryField("num")
        nickname = FactoryField("nick")


See `Custom Field Handlers <https://mimesis.name/en/master/schema.html#custom-field-handlers>`_ for more information
about how to define custom field handlers.

Factories and pytest
--------------------

We also recommend to use `pytest-factoryboy <https://github.com/pytest-dev/pytest-factoryboy>`_.
This way it will be possible to integrate your factories into pytest fixtures.
