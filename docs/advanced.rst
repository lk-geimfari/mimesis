==============
Advanced Usage
==============

Here we gonna speaking about integration with web frameworks, best practices
and a number of most useful features of the library.


Introduction
------------

It is worth noting that we will be showing the basic capabilities of the
library and we will be using a few most common class providers, since
there are too many of them to cover each one in detail. If the article
sparks your interest to the library you can visit the useful links
listed in the end of the article and find out more. The library is
pretty simple. All you need to do to start working with the data is to
create a class provider. The most common type of data in apps are
personal users’ data, such as name, last name, credit card info, etc.
There is a special class provider for this type of data — :class:`~mimesis.Person()`,
which takes the code from the language standard in the form of a line as
shown below:

.. code:: python

    >>> from mimesis import Person
    >>> from mimesis.enums import Gender
    >>> person = Person('is')
    >>> for _ in range(0, 3):
    ...     person.full_name(gender=Gender.MALE)
    ...
    'Karl Brynjúlfsson'
    'Rögnvald Eiðsson'
    'Vésteinn Ríkharðsson'


Almost every web-application requires e-mail for registration.
Naturally, the library supports the ability to generate e-mails with the
help of :meth:`~mimesis.Person.email()` method :class:`~mimesis.Person()` class, as below:

.. code:: python

    >>> person.email()
    'lvana6108@gmail.com'

There is a little problem with the method above, which may cause the
code to be slightly “dirty” in case the app uses more than one type of
class providers. In such situation you should use object :class:`~mimesis.Generic()`,
which grants access to all providers from one single object:

.. code:: python

    >>> from mimesis import Generic
    >>> g = Generic('pl')
    >>> g.person.full_name()
    'Lonisława Podsiadło'
    >>> g.datetime.birthday(readable=True)
    'Listopad 11, 1997'
    >>> g.code.imei()
    '011948003071013'
    >>> g.food.fruit()
    'Cytryna'
    >>> g.internet.http_method()
    'PUT'
    >>> g.science.math_formula()
    'A = (h * (a + b)) / 2'

As mentioned above, the library supports over 23 class providers
with data for all possible situations. For example, if you
are working on an app dedicated to transportation and logistics and you
need to generate transportation models, you can easily do this by using
:class:`~mimesis.Transport()` class provider, which contains data related to
transportation:

.. code:: python

    >>> from mimesis import Transport
    >>> trans = Transport()

    >>> for _ in range(0, 5):
    ...     trans.truck()
    ...
    'Seddon-2537 IM'
    'Karrier-7799 UN'
    'Minerva-5567 YC'
    'Hyundai-2808 XR'
    'LIAZ-7174 RM'

Or you could indicate the transport mask model:

.. code:: python

    >>> for _ in range(0, 5):
    ...     trans.truck(model_mask="##@")
    ...
    'Henschel-16G'
    'Bean-44D'
    'Unic-82S'
    'Ford-05Q'
    'Kalmar-58C'

Quite often when testing web-applications (blog would be an excellent
example) you need to generate text data (text, sentences, tags, etc.).
Manually inputting the text is long and boring, and Mimesis allows you
to avoid this thanks to a class provider :class:`~mimesis.Text()`:

.. code:: python

    >>> from mimesis import Text
    >>> text = Text('en')

    >>> text.title()
    'Python is a programming language.'

You can get a list of random words:

.. code:: python

    >>> text = Text('pt-br')
    >>> text.words(quantity=5)
    ['poder', 'de', 'maior', 'só', 'cima']

Generate a street name:

.. code:: python

    >>> from mimesis import Address
    >>> address = Address('en')

    >>> address.address()
    '77 Shephard Trace'

Get a name of a state/area/province, which is related to the chosen
language. In this case it is an state of the USA:

.. code:: python

    >>> address.state()
    'Texas'


Creating objects
----------------

If your app requires data in one particular language, it’s preferable to
use class :class:`~mimesis.Generic()`, giving access to all class providers through a
single object, rather than through multiple separate class providers.
Using :class:`~mimesis.Generic()` will allow you to get rid of several extra lines of
code.

Incorrect:

.. code:: python

    >>> from mimesis import Person, Datetime, Text, Code

    >>> person = Person('ru')
    >>> datetime = Datetime('ru')
    >>> text = Text('ru')
    >>> code = Code('ru')


Correct:

.. code:: python

    >>> from mimesis import Generic
    >>> generic = Generic('ru')

    >>> generic.person.username()
    'sherley3354'

    >>> generic.datetime.date()
    '14-05-2007'

Still correct:

.. code:: python

    >>> from mimesis import Person

    >>> p_en = Person('en')
    >>> p_sv = Person('sv')
    >>> # …

It means that importing class providers separately makes sense only if
you limit yourself to the data available through the class you imported,
otherwise it’s better to use :class:`~mimesis.Generic()`.


Using with ORM
--------------
First of all we would like to point out that Mimesis wasn’t developed to
be used with a certain database or ORM. The main problem the library
solves is generating valid data. Consequently, while there are no rigid
rules of working with the library, here are a few recommendations that
will help you keep your testing environment in order and will avert
growth of entropy within your project. Recommendations are quite simple
and are fully in tune with the Python spirit.

Despite the previous note, the need for test data usually occurs in
web-apps that perform certain operations (mostly CRUD) with a database.
We have some advice on organizing test data generation for web-apps.
Functions responsible for data generation and importing it to the
database should be kept close to the models, or even better as statistical
methods of the model they are related to. This is necessary to avoid running
around files when the model structure changes and you need to add a new filed.


Integration with Web Frameworks
-------------------------------

You simply need to define a static method that will run all the
manipulations related to the current model and call it when you need the
initial database loading, as demonstrated in the example below. Model
for Flask (Flask-SQLAlchemy) would look like this:

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
        def _bootstrap(count=500, locale='en'):
            from mimesis import Person
            person = Person(locale)

            for _ in range(count):
                patient = Patient(
                    email=person.email(),
                    phone_number=person.telephone(),
                    full_name=person.full_name(),
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

Now let’s transition to shell-mode:

.. code:: text

    (venv) ➜ python3 manage.py shell


And generate data. Beforehand, we need to make sure that the database
and the model in question are available.

.. code:: python

    >>> db
    <SQLAlchemy engine='sqlite:///db.sqlite'>

    >>> Patient
    <class 'app.models.Patient'>

    >>> # Generate 2к entries in English.
    >>> Patient()._bootstrap(count=2000, locale='en')


Inserting data into database
----------------------------

If you need to generate data and import it into a database we strongly
recommend generating data in chunks rather than *600k* at once. Keep
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

Class :class:`~mimesis.Internet()` boasts of several methods which generate image
links (more details here). Links to images locate on remote servers
would be enough, however, if you still want to have a number of random
images locally, you can download images generated by the respective
class :class:`~mimesis.Internet()` methods with the help of function
``download_image()`` from model utils:

.. code:: python

    >>> from mimesis import Internet
    >>> from mimesis.utils import download_image

    >>> net = Internet()

    >>> url = net.stock_image(width=1920, height=1080)
    >>> download_image(url=url, save_path='/some/path/')


Integration with third-party libraries
--------------------------------------

- `mimesis-factory`_ - Integration with ``factory_boy``.
- `pytest-mimesis`_ - is a pytest plugin that provides pytest fixtures for Mimesis providers.

.. _mimesis-factory: https://github.com/mimesis-lab/mimesis-factory
.. _pytest-mimesis: https://github.com/lk-geimfari/pytest-mimesis
