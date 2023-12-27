============
Installation
============

Compatibility
-------------

Mimesis is compatible with Python version 3.10 or higher (including PyPy 3.10).

To work with Mimesis on Python versions 3.8 and 3.9, the final compatible
version is Mimesis 11.1.0. Install this specific version to ensure compatibility.

Dependencies
------------

Mimesis has no hard dependencies, but you need to install `pytz` to add
timezone support for some methods of the :class:`~mimesis.Datetime` provider.


Install Mimesis
---------------

.. note::

    To prevent unintended upgrades, it is **highly advisable** to always specify
    the version of mimesis that you are using by pinning it.

    The latest version of Mimesis is:

    .. image:: https://img.shields.io/pypi/v/mimesis?color=bright-green
         :target: https://pypi.org/project/mimesis/
         :alt: PyPi Version

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

