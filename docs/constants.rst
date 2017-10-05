===========
Constants
===========

The constraints will be useful to you, because they allows you to avoid entering values,
and this mean that they help to avoid typos.

.. code:: python

    >>> from mimesis import Personal
    >>> import mimesis.constants as c

    >>> pr = Personal(c.EN)
    # typo in parameter gender, which should be has a value "female"
    >>> female_names = [pr.full_name(gender='emale') for _ in range(5)]

    # An exception will be raised:
    # UnexpectedGender: 'Gender must be 0, 1, 2, 9, f, female, m, male.'

    # The constants helps to avoid similar issues.
    >>> female_names = [pr.full_name(c.FEMALE) for _ in range(5)]
    ['Nobuko Campos', 'Casimira Ballard', 'Lena Brady', 'Victoria Carr', 'Luetta Beard']


That's all that constants are for.
