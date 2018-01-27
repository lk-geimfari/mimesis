Comparison: Mimesis vs. Faker.
==============================

Importing needing classes and creating instances:

.. code:: python

    import cProfile

    from mimesis import Personal
    from faker import Faker

    personal = Personal()
    faker = Faker()


Task 1: Generate ``10k`` full names.
====================================

Generating using ``Mimesis``:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    cProfile.run('[personal.full_name() for _ in range(10000)]')

Output:

.. code:: text

             347766 function calls in 0.254 seconds

       Ordered by: standard name

       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.009    0.009    0.254    0.254 <string>:1(<listcomp>)
            1    0.000    0.000    0.254    0.254 <string>:1(<module>)
            1    0.000    0.000    0.000    0.000 base.py:14(__init__)
        10000    0.010    0.000    0.022    0.000 base.py:25(_validate_enum)
            1    0.000    0.000    0.000    0.000 base.py:62(__init__)
        10000    0.010    0.000    0.010    0.000 enum.py:279(__iter__)
        30000    0.012    0.000    0.012    0.000 enum.py:280(<genexpr>)
        10000    0.007    0.000    0.008    0.000 enum.py:282(__len__)
        10000    0.003    0.000    0.003    0.000 enum.py:527(value)
            1    0.000    0.000    0.000    0.000 generic.py:64(__getattr__)
        10000    0.034    0.000    0.095    0.000 helpers.py:105(get_random_item)
        10000    0.028    0.000    0.245    0.000 personal.py:135(full_name)
            1    0.000    0.000    0.000    0.000 personal.py:22(__init__)
        10000    0.018    0.000    0.073    0.000 personal.py:73(name)
        10000    0.011    0.000    0.039    0.000 personal.py:86(surname)
        30000    0.036    0.000    0.051    0.000 random.py:220(_randbelow)
        30000    0.031    0.000    0.087    0.000 random.py:250(choice)
            1    0.000    0.000    0.000    0.000 random.py:84(__init__)
            1    0.000    0.000    0.000    0.000 random.py:93(seed)
        10000    0.007    0.000    0.010    0.000 types.py:130(__get__)
            1    0.000    0.000    0.000    0.000 utils.py:139(setup_locale)
            1    0.000    0.000    0.000    0.000 {built-in method builtins.callable}
            1    0.000    0.000    0.254    0.254 {built-in method builtins.exec}
        30001    0.006    0.000    0.006    0.000 {built-in method builtins.isinstance}
        40000    0.006    0.000    0.006    0.000 {built-in method builtins.len}
            1    0.000    0.000    0.000    0.000 {built-in method from_bytes}
            1    0.000    0.000    0.000    0.000 {built-in method posix.urandom}
            1    0.000    0.000    0.000    0.000 {function Random.seed at 0x7f6c109b5730}
        30000    0.004    0.000    0.004    0.000 {method 'bit_length' of 'int' objects}
            1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        10000    0.007    0.000    0.007    0.000 {method 'format' of 'str' objects}
        10000    0.002    0.000    0.002    0.000 {method 'get' of 'dict' objects}
        47749    0.011    0.000    0.011    0.000 {method 'getrandbits' of '_random.Random' objects}
            1    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}

**Result**: ``10k`` full names in ``0.254`` second.

Generating using ``Faker``:
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    cProfile.run('[faker.name() for _ in range(10000)]')

Output:

.. code:: text

             14235635 function calls in 15.144 seconds

       Ordered by: standard name

       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.028    0.028   15.142   15.142 <string>:1(<listcomp>)
            1    0.000    0.000   15.143   15.143 <string>:1(<module>)
        10000    0.040    0.000   15.114    0.002 __init__.py:13(name)
        10000    0.025    0.000   10.413    0.001 __init__.py:23(last_name)
         5030    0.011    0.000    1.783    0.000 __init__.py:42(first_name_male)
         4970    0.011    0.000    2.067    0.000 __init__.py:47(first_name_female)
           93    0.000    0.000    0.002    0.000 __init__.py:71(prefix_male)
           94    0.000    0.000    0.002    0.000 __init__.py:76(prefix_female)
          136    0.000    0.000    0.006    0.000 __init__.py:90(suffix_male)
        30441    2.795    0.000   14.612    0.000 __init__.py:93(random_element)
          118    0.000    0.000    0.004    0.000 __init__.py:95(suffix_female)
     13625929    2.682    0.000    2.682    0.000 distribution.py:13(cumsum)
        30441    2.257    0.000   11.770    0.000 distribution.py:20(choice_distribution)
        30441    6.574    0.000    6.574    0.000 distribution.py:31(<listcomp>)
        30441    0.056    0.000    0.120    0.000 distribution.py:7(random_sample)
        10000    0.021    0.000   14.685    0.001 generator.py:100(parse)
        20441    0.105    0.000   14.536    0.001 generator.py:107(__format_token)
        30441    0.019    0.000    0.019    0.000 generator.py:55(random)
        20441    0.062    0.000   14.398    0.001 generator.py:72(format)
        20441    0.020    0.000    0.059    0.000 generator.py:79(get_formatter)
        30441    0.056    0.000    0.065    0.000 random.py:342(uniform)
        30441    0.045    0.000    0.045    0.000 {built-in method _bisect.bisect_right}
            1    0.001    0.001   15.144   15.144 {built-in method builtins.exec}
        20441    0.039    0.000    0.039    0.000 {built-in method builtins.getattr}
        40882    0.082    0.000    0.082    0.000 {built-in method builtins.hasattr}
        30441    0.013    0.000    0.013    0.000 {built-in method builtins.isinstance}
        60882    0.014    0.000    0.014    0.000 {built-in method builtins.len}
            1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        20441    0.015    0.000    0.015    0.000 {method 'groups' of '_sre.SRE_Match' objects}
        20441    0.018    0.000    0.018    0.000 {method 'join' of 'str' objects}
        30441    0.010    0.000    0.010    0.000 {method 'keys' of 'collections.OrderedDict' objects}
        30441    0.009    0.000    0.009    0.000 {method 'random' of '_random.Random' objects}
        10000    0.128    0.000   14.664    0.001 {method 'sub' of '_sre.SRE_Pattern' objects}
        30441    0.006    0.000    0.006    0.000 {method 'values' of 'collections.OrderedDict' objects}

**Result**: ``10k`` full names in ``15.144`` second.


Task 2: Generate ``10k`` last names.
====================================

Generating using ``Mimesis``:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    cProfile.run('[personal.last_name() for _ in range(10000)]')

Output:

.. code:: text

             80249 function calls in 0.040 seconds

       Ordered by: standard name

       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.005    0.005    0.040    0.040 <string>:1(<listcomp>)
            1    0.000    0.000    0.040    0.040 <string>:1(<module>)
        10000    0.004    0.000    0.035    0.000 personal.py:104(last_name)
        10000    0.009    0.000    0.031    0.000 personal.py:86(surname)
        10000    0.008    0.000    0.011    0.000 random.py:220(_randbelow)
        10000    0.007    0.000    0.020    0.000 random.py:250(choice)
            1    0.000    0.000    0.040    0.040 {built-in method builtins.exec}
        10000    0.002    0.000    0.002    0.000 {built-in method builtins.isinstance}
        10000    0.001    0.000    0.001    0.000 {built-in method builtins.len}
        10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
            1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        10245    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}

**Result**: ``10k`` full names in ``0.040`` second.

Generating using ``Faker``:
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    cProfile.run('[personal.last_name() for _ in range(10000)]')

Output:

.. code:: text

             10160004 function calls in 8.218 seconds

       Ordered by: standard name

       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.011    0.011    8.218    8.218 <string>:1(<listcomp>)
            1    0.000    0.000    8.218    8.218 <string>:1(<module>)
        10000    0.012    0.000    8.207    0.001 __init__.py:23(last_name)
        10000    1.194    0.000    8.194    0.001 __init__.py:93(random_element)
     10010000    1.641    0.000    1.641    0.000 distribution.py:13(cumsum)
        10000    1.314    0.000    6.989    0.001 distribution.py:20(choice_distribution)
        10000    3.979    0.000    3.979    0.000 distribution.py:31(<listcomp>)
        10000    0.012    0.000    0.025    0.000 distribution.py:7(random_sample)
        10000    0.004    0.000    0.004    0.000 generator.py:55(random)
        10000    0.010    0.000    0.012    0.000 random.py:342(uniform)
        10000    0.011    0.000    0.011    0.000 {built-in method _bisect.bisect_right}
            1    0.000    0.000    8.218    8.218 {built-in method builtins.exec}
        10000    0.016    0.000    0.016    0.000 {built-in method builtins.hasattr}
        10000    0.003    0.000    0.003    0.000 {built-in method builtins.isinstance}
        20000    0.003    0.000    0.003    0.000 {built-in method builtins.len}
            1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        10000    0.002    0.000    0.002    0.000 {method 'keys' of 'collections.OrderedDict' objects}
        10000    0.002    0.000    0.002    0.000 {method 'random' of '_random.Random' objects}
        10000    0.002    0.000    0.002    0.000 {method 'values' of 'collections.OrderedDict' objects}

**Result**: ``10k`` full names in ``8.218`` second.
