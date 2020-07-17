.. _api-reference:

=============
API Reference
=============

This part of the documentation covers all the public interfaces of *Mimesis*.


Random object
=============

Random
------

.. autoclass:: mimesis.random.Random
   :members:
   :special-members: __init__


Builtin Data Providers
======================

BrazilSpecProvider
------------------

.. autoclass:: mimesis.builtins.BrazilSpecProvider
   :members:
   :special-members: __init__

DenmarkSpecProvider
-------------------

.. autoclass:: mimesis.builtins.DenmarkSpecProvider
   :members:
   :special-members: __init__

GermanySpecProvider
-------------------

.. autoclass:: mimesis.builtins.GermanySpecProvider
   :members:
   :special-members: __init__

NetherlandsSpecProvider
-----------------------

.. autoclass:: mimesis.builtins.NetherlandsSpecProvider
   :members:
   :special-members: __init__

RussiaSpecProvider
------------------

.. autoclass:: mimesis.builtins.RussiaSpecProvider
   :members:
   :special-members: __init__

UkraineSpecProvider
-------------------

.. autoclass:: mimesis.builtins.UkraineSpecProvider
   :members:
   :special-members: __init__

USASpecProvider
---------------

.. autoclass:: mimesis.builtins.USASpecProvider
   :members:
   :special-members: __init__

PolandSpecProvider
------------------

.. autoclass:: mimesis.builtins.PolandSpecProvider
   :members:
   :special-members: __init__

Decorators
==========

.. automodule:: mimesis.decorators
   :members:


Custom Exceptions
=================

UnsupportedAlgorithm
--------------------

.. autoclass:: mimesis.exceptions.UnsupportedAlgorithm
   :members:

UnsupportedField
----------------

.. autoclass:: mimesis.exceptions.UnsupportedField
   :members:

UnsupportedLocale
-----------------

.. autoclass:: mimesis.exceptions.UnsupportedLocale
   :members:

UndefinedField
--------------

.. autoclass:: mimesis.exceptions.UndefinedField
   :members:

UndefinedSchema
---------------

.. autoclass:: mimesis.exceptions.UndefinedSchema
   :members:

UnacceptableField
-----------------

.. autoclass:: mimesis.exceptions.UnacceptableField
   :members:

NonEnumerableError
------------------

.. autoclass:: mimesis.exceptions.NonEnumerableError
   :members:


Base Providers
==============

BaseProvider
------------

.. autoclass:: mimesis.providers.BaseProvider
   :members:
   :special-members: __init__

BaseDataProvider
----------------

.. autoclass:: mimesis.providers.BaseDataProvider
   :members:
   :special-members: __init__


Generic Providers
=================

Generic
-------

.. autoclass:: mimesis.Generic
   :members:
   :special-members: __init__



Locale-Dependent Providers
==========================

Address
-------

.. autoclass:: mimesis.Address
   :members:
   :special-members: __init__

Business
--------

.. autoclass:: mimesis.Business
   :members:
   :special-members: __init__

Datetime
--------

.. autoclass:: mimesis.Datetime
   :members:
   :special-members: __init__

Food
----
.. autoclass:: mimesis.Food
   :members:
   :special-members: __init__

Person
--------

.. autoclass:: mimesis.Person
   :members:
   :special-members: __init__

Science
-------

.. autoclass:: mimesis.Science
   :members:
   :special-members: __init__

Text
----

.. autoclass:: mimesis.Text
   :members:
   :special-members: __init__


Locale-Independent Providers
=============================

Clothing
-------------

.. autoclass:: mimesis.Clothing
   :members:
   :special-members: __init__

Code
----

.. autoclass:: mimesis.Code
   :members:
   :special-members: __init__

Choice
------

.. autoclass:: mimesis.Choice
   :members:
   :special-members: __init__

Cryptographic
-------------

.. autoclass:: mimesis.Cryptographic
   :members:
   :special-members: __init__

Development
-----------

.. autoclass:: mimesis.Development
   :members:
   :special-members: __init__

File
----

.. autoclass:: mimesis.File
   :members:
   :special-members: __init__

Hardware
--------

.. autoclass:: mimesis.Hardware
   :members:
   :special-members: __init__

Internet
--------

.. autoclass:: mimesis.Internet
   :members:
   :special-members: __init__

Numbers
-------

.. autoclass:: mimesis.Numbers
   :members:
   :special-members: __init__

Path
----

.. autoclass:: mimesis.Path
   :members:
   :special-members: __init__

Structure
----------

.. autoclass:: mimesis.Structure
   :members:
   :special-members: __init__

Transport
---------

.. autoclass:: mimesis.Transport
   :members:
   :special-members: __init__

UnitSystem
----------

.. autoclass:: mimesis.UnitSystem
   :members:
   :special-members: __init__




Schema
======

AbstractField
-------------

.. autoclass:: mimesis.schema.AbstractField
   :members:
   :special-members: __call__

Field
------

.. autoclass:: mimesis.schema.Field
   :members:

Schema
------

.. autoclass:: mimesis.schema.Schema
   :members:

Enums
=====

.. automodule:: mimesis.enums
   :members:
   :undoc-members:
