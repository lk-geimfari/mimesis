.. _factory_plugin:

Integration with factory_boy
============================

Starting from version ``15.0.0``, Mimesis now supports ``factory_boy`` out of the box.
You no longer require any third-party packages to integrate Mimesis with ``factory_boy``.

Mimesis requires ``factory_boy`` to be installed, but it's not a hard dependency.
Therefore, you'll need to install it manually:

.. code-block:: bash

    poetry add factory_boy


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




Now, use the ``MimesisField`` class to define how fake data is generated:

.. code-block:: python

    import factory
    from mimesis.plugins.factory import MimesisField

    from account import Account

    class AccountFactory(factory.Factory):
        class Meta(object):
            model = Account

        username = MimesisField('username', template='l_d')
        name = MimesisField('name', gender='female')
        surname = MimesisField('surname', gender='female')
        age = MimesisField('age', minimum=18, maximum=90)
        email = factory.LazyAttribute(
            lambda instance: '{0}@example.org'.format(instance.username)
        )
        access_token = MimesisField('token', entropy=32)



See `factory_boy <https://factoryboy.readthedocs.io/>`_ documentation for more information about how to use factories.

pytest
------

We also recommend to use `pytest-factoryboy <https://github.com/pytest-dev/pytest-factoryboy>`_.
This way it will be possible to integrate your factories into pytest fixtures.
