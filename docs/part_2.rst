===========
Generating mock data using Mimesis: Part II
===========

We have already `published <http://mimesis.readthedocs.io/en/latest/part_1.html>`_ how to generate mock
data with the help of a Python library  — `Mimesis <https://github.com/lk-geimfari/mimesis>`__.
The article you are reading now is the continuation of the previous one,
therefore, we will not be going over the basics again. In case you missed
out on the first article or you felt lazy at the time, you might want to
go back to it now since this article assumes you are familiar with the library.
Here we are going to speak about best practices and a number of most
useful features of the library.

Note
----

First of all we would like to point out that Mimesis wasn’t developed to
be used with a certain database or ORM. The main problem the library
solves is generating valid data. Consequently, while there are no rigid
rules of working with the library, here are a few recommendations that
will help you keep your testing environment in order and will avert
growth of entropy within your project. Recommendations are quite simple
and are fully in tune with the Python spirit (if you disagree, feel free
to let us know).

Despite the previous note that the library isn’t to be used with a
certain database or ORM, the need for test data usually occurs in
web-apps that perform certain operations (mostly CRUD) with a database.
We have some advice on organizing test data generation for web-apps.
Functions responsible for data generation and importing it to the
database should be kept close to the models, or even better as
statistical methods of the model they are related to, as in the example
of ``_bootstrap()`` method from the previous article. This is necessary
to avoid running around files when the model structure changes and you
need to add a new filed. Model ``Patient()`` from the previous article
illustrates the idea:

.. code:: python

    class Patient(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        email = db.Column(db.String(120), unique=True)
        phone_number = db.Column(db.String(25))
        full_name = db.Column(db.String(100))
        weight = db.Column(db.String(64))
        height = db.Column(db.String(64))
        blood_type = db.Column(db.String(64))
        age = db.Column(db.Integer)

        def __init__(self, **kwargs):
            super(Patient, self).__init__(**kwargs)

        @staticmethod
        def _bootstrap(count=500, locale='en', gender):
            from mimesis import Personal
            person = Personal(locale)

            for _ in range(count):
                patient = Patient(
                    email=person.email(),
                    phone_number=person.telephone(),
                    full_name=person.full_name(gender=gender),
                    age=person.age(minimum=18, maximum=45),
                    weight=person.weight(),
                    height=person.height(),
                    blood_type=person.blood_type()
                )

                db.session.add(patient)
                try:
                    db.session.commit()
                except IntegrityError:
                    db.session.rollback()

Keep in mind that the example above is a model of a Flask-app used by
``SQLAlchemy``. Organizing mock data generators for such apps with the
use of different frameworks is done in the same way.

Creating objects
----------------

If your app requires data in one particular language, it’s preferable to
use class ``Generic()``, giving access to all class providers through a
single object, rather than through multiple separate class providers.
Using ``Generic()`` will allow you to get rid of several extra lines of
code.

Incorrect:

.. code:: python

    >>> from mimesis import Personal, Datetime, Text, Code

    >>> personal = Personal('ru')
    >>> datetime = Datetime('ru')
    >>> text = Text('ru')
    >>> code = Code('ru')

Correct:

.. code:: python

    >>> from mimesis import Generic
    >>> generic = Generic('ru')

    >>> generic.personal.username()
    'sherley3354'

    >>> generic.datetime.date()
    '14-05-2007'

Still correct:

.. code:: python

    >>> from mimesis import Personal

    >>> p_en = Personal('en')
    >>> p_sv = Personal('sv')
    >>> # …

It means that importing class providers separately makes sense only if
you limit yourself to the data available through the class you imported,
otherwise it’s better to use ``Generic()``.

Inserting data into database
----------------------------

If you need to generate data and import it into a database we strongly
recommend generating data in chunks rather than ``600k`` at once. Keep
in mind the possible limitations of databases, ORM, etc. The smaller the
generated data chunks are, the faster the process will go.

Good:

.. code:: python

    >>> Patient()._bootstrap(count=2000, locale='de')

Very bad:

.. code:: python

    >>> Patient()._bootstrap(count=600000, locale='de')

Importing images
----------------

Class ``Internet()`` boasts of several methods which generate image
links (more details here). Links to images locate on remote servers
would be enough, however, if you still want to have a number of random
images locally, you can download images generated by the respective
class ``Internet()`` methods with the help of function
``download_image()`` from model utils:

.. code:: python

    >>> from mimesis import Internet
    >>> from mimesis.utils import download_image

    >>> net = Internet()

    >>> img_url = net.stock_image(category='food', width=1920, height=1080)
    >>> download_image(url=img_url, save_path='/some/path/')

User providers
--------------

The library supports a vast amount of data and in most cases this would
be enough. For those who want to create their own providers with more
specific data. This can be done like this:

.. code:: python

    >>> class SomeProvider():
    ...     class Meta:
    ...         name = "some_provider"
    ...
    ...     @staticmethod
    ...     def one():
    ...         return 1

    >>> class Another():
    ...     @staticmethod
    ...     def bye():
    ...         return "Bye!"

    >>> generic.add_provider(SomeProvider)
    >>> generic.add_provider(Another)

    >>> generic.some_provider.one()
    1

    >>> generic.another.bye()
    'Bye!'

You can also add multiple providers:

.. code:: python

    >>> generic.add_providers(SomeProvider, Another)
    >>> generic.some_provider.one()
    1
    >>> generic.another.bye()
    'Bye!'

Everything is pretty easy and self-explanatory here, therefore, we will
only clarify one moment — attribute ``name``, class ``Meta`` is the name
of a class through which access to methods of user-class providers is
carried out. By default class name is the name of the class in the lower
register.

Built-in providers
------------------

Most countries, where only one language is official, have data typical
only for these particular countries. For example, ``CPF`` for Brazil
(``pt-br``), ``SSN`` for USA (``en``). This kind of data can cause
discomfort and meddle with the order (or at least annoy) by being
present in all the objects regardless of the chosen language standard.
You can see that for yourselves by looking at the example (the code
won’t run):

.. code:: python

    >>> from mimesis import Personal
    >>> person = Personal('en')

    >>> person.ssn()
    >>> person.cpf()

We bet everyone would agree that this does not look too good.
Perfectionists, as we are, have taken care of this in a way that some
specific regional provider would not bother other providers for other
regions. For this reason, class providers with locally-specific data are
separated into a special sub-package (``mimesis.builtins``) for keeping
a common class structure for all languages and their objects.

Here’s how it works:

.. code:: python

    >>> from mimesis import Generic
    >>> from mimesis.builtins import BrazilSpecProvider

    >>> generic = Generic('pt-br')
    >>> generic.add_provider(BrazilProvider)
    >>> generic.brazil_provider.cpf()
    '696.441.186-00'

If you want to change default name of built-in provider, just change
value of attribute ``name``, class ``Meta`` of the builtin provider:

.. code:: python

    >>> BrazilSpecProvider.Meta.name = 'brasil'
    >>> generic.add_provider(BrazilSpecProvider)
    >>> generic.brasil.cpf()
    '019.775.929-70'

Or just inherit the class and override the value of attribute ``name``
of class ``Meta`` of the provider (in our case this is
``BrazilSpecProvider()``) :

.. code:: python

    >>> class Brasil(BrazilSpecProvider):
    ...
    ...     class Meta:
    ...         name = "brasil"
    ...
    >>> generic.add_provider(Brasil)
    >>> generic.brasil.cnpj()
    '55.806.487/7994-45'

Generally, you don’t need to add built-it classes to the object
``Generic()``. It was done in the example with the single purpose of
demonstrating in which cases you should add a built-in class provider to
the object ``Generic()``. You can use it directly, as shown below:

.. code:: python

    >>> from mimesis.builtins import RussiaSpecProvider
    >>> ru = RussiaSpecProvider()

    >>> ru.patronymic(gender='female')
    'Петровна'

    >>> ru.patronymic(gender='male')
    'Бенедиктович'

Generate data by schema
-----------------------

Mimesis support generating data by schema from version ``0.0.5``. This
feature is still at an early stage of development. Actually is very easy
feature, here how it works:

.. code:: python

    >>> from mimesis.schema import Schema
    >>> schema = Schema('en')

    >>> schema.load(schema={
    ...     "id": "cryptographic.uuid",
    ...     "name": "text.word",
    ...     "version": "development.version",
    ...     "owner": {
    ...         "email": "personal.email",
    ...         "token": "cryptographic.token",
    ...         "creator": "personal.full_name"
    ...     }
    ... }).create(iterations=2)

    >>> # or you can load data from json file:
    >>> schema.load(path='schema.json').create(iterations=2)

Result:

.. code:: json

    [
      {
        "id": "790cce21-5f75-2652-2ee2-f9d90a26c43d",
        "name": "container",
        "owner": {
          "email": "anjelica8481@outlook.com",
          "token": "0bf924125640c46aad2a860f40ec4b7f33a516c497957abd70375c548ed56978",
          "creator": "Ileen Ellis"
        },
        "version": "4.11.6"
      },
      ...
    ]

.. note:: ``Schema()`` is an experimental feature. Be careful when using it.

Which type of data do you usually need in your work? What is the library
missing? We will be very happy to hear your suggestions and comments.


.. |Mimesis| image:: https://user-images.githubusercontent.com/15812620/29830988-701236f8-8cec-11e7-9b81-1f0082972069.png
   :target: https://github.com/lk-geimfari/mimesis
