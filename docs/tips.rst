===============
Tips and Tricks
===============

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

Also correct:

.. code:: python

    >>> from mimesis import Person

    >>> person = Person('en')
    >>> with person.override_locale('sv')
    >>>     pass
    >>> # …


It means that importing class providers separately makes sense only if
you limit yourself to the data available through the class you imported,
otherwise it’s better to use :class:`~mimesis.Generic()`.


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
    >>> from mimesis.shortcuts import download_image

    >>> net = Internet()

    >>> url = net.stock_image(width=1920, height=1080, keywords=['love', 'passion'])
    >>> download_image(url=url, save_path='/some/path/')


Romanization of Cyrillic data
-----------------------------

If your locale belongs to the family of Cyrillic languages, but you need
latinized locale-specific data, then you can use decorator :func:`~mimesis.decorators.romanized` which
help you romanize your data.

Example of usage for romanization of Russian full name:

.. code:: python

    >>> from mimesis.decorators import romanized

    >>> @romanized('ru')
    ... def russian_name():
    ...     return 'Вероника Денисова'

    >>> russian_name()
    'Veronika Denisova'

At this moment it works only for Russian (**ru**),
Ukrainian (**uk**) and Kazakh (**kk**):



Integration with third-party libraries
--------------------------------------

- `mimesis-factory`_ - Integration with ``factory_boy``.
- `pytest-mimesis`_ - is a pytest plugin that provides pytest fixtures for Mimesis providers.

.. _mimesis-factory: https://github.com/mimesis-lab/mimesis-factory
.. _pytest-mimesis: https://github.com/lk-geimfari/pytest-mimesis
