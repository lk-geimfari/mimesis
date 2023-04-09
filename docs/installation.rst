============
Installation
============

Python compatibility
--------------------

Mimesis is compatible with Python, including PyPy, version 3.8 or higher. The Mimesis 4.1.3 is the last release that accommodates Python 3.6 and 3.7.


Dependencies
------------

Mimesis has no hard dependencies, but you have to install ``pytz`` to timezones support for some methods of the ``Datetime`` provider.


Install Mimesis
---------------

Within the pre-activated environment, use the following command to install Mimesis:

.. code-block:: sh

    (env) ➜ pip install mimesis

Use the following command to install Mimesis in Jupyter Notebook:

.. code-block:: sh

    (env) ➜ ! pip install mimesis

Installation using *poetry* is pretty same:

.. code-block:: sh

    (env) ➜ poetry add --group dev mimesis


If you want to work with the latest Mimesis code before it's released, install or
update the code from the master branch:

.. code-block:: sh

    (env) ➜ git clone git@github.com:lk-geimfari/mimesis.git
    (env) ➜ cd mimesis/
    (env) ➜ make install

