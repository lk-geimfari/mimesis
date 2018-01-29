.. _installation:

Installation
============

Python Support
--------------

**Mimesis** works only on Python 3.5 and higher. Developers have not plans related to adding support
for old versions of Python, such as 2.7.

Also, possibly Mimesis will work fine on latest version of PyPy 3, but we have not tested it on PyPy,
therefore, use it with PyPy at your own risk.

Install Mimesis
---------------

Within the pre-activated environment, use the following command to install Mimesis:

.. code-block:: sh

    (env) ➜ pip install mimesis

Installation using *Pipenv* is pretty same:

.. code-block:: sh

    (env) ➜ pipenv install --dev mimesis


If you want to work with the latest Mimesis code before it's released, install or
update the code from the master branch:

.. code-block:: sh

    (env) ➜ git clone git@github.com:lk-geimfari/mimesis.git
    (env) ➜ cd mimesis/
    (env) ➜ make install
