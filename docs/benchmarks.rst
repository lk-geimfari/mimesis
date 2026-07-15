==========
Benchmarks
==========

Mimesis is substantially faster and uses less peak memory than Faker on typical
fake-data workloads. On a full suite of **47** comparable operations
(``20,000`` timing iterations each, locale ``en``), Mimesis won **every**
timing comparison, with an overall speedup of about **24×**.

The same suite also measures peak allocation with ``tracemalloc`` while
building batches of **50,000** values. Across those scenarios, Faker peaked
about **1.22×** higher than Mimesis.

Uniqueness is compared on shared identity-like fields (names, emails,
usernames, phones, addresses, and URLs). On a batch of **100,000** values,
Mimesis averages about **98.5%** unique values versus about **79%** for Faker.

These numbers were recorded on a **MacBook Pro 14″** (Apple **M1 Pro**, **32 GB**
RAM). Absolute timings and memory peaks vary by machine; relative gaps are what
matter.

Reproduce or refresh the numbers with the script in
`benchmarks <https://github.com/lk-geimfari/mimesis/tree/master/benchmarks>`_.

Timing
------

+---------------------------+---------------+---------------+---------------+
| Category                  | Mimesis (avg) | Faker (avg)   | Speedup       |
+===========================+===============+===============+===============+
| Person                    | 0.012 µs      | 0.240 µs      | 19.74×        |
+---------------------------+---------------+---------------+---------------+
| Address                   | 0.005 µs      | 0.148 µs      | 27.53×        |
+---------------------------+---------------+---------------+---------------+
| Internet                  | 0.011 µs      | 0.211 µs      | 18.70×        |
+---------------------------+---------------+---------------+---------------+
| Datetime                  | 0.005 µs      | 0.023 µs      | 5.03×         |
+---------------------------+---------------+---------------+---------------+
| Text                      | 0.003 µs      | 0.071 µs      | 26.23×        |
+---------------------------+---------------+---------------+---------------+
| Finance                   | 0.001 µs      | 0.081 µs      | 69.07×        |
+---------------------------+---------------+---------------+---------------+
| Payment                   | 0.009 µs      | 0.025 µs      | 2.67×         |
+---------------------------+---------------+---------------+---------------+
| Code                      | 0.006 µs      | 0.020 µs      | 3.67×         |
+---------------------------+---------------+---------------+---------------+
| Numeric                   | 0.001 µs      | 0.005 µs      | 4.60×         |
+---------------------------+---------------+---------------+---------------+
| Generic                   | 0.013 µs      | 0.309 µs      | 22.91×        |
+---------------------------+---------------+---------------+---------------+
| Complex operations        | 0.220 µs      | 5.798 ms      | 26.39×        |
+---------------------------+---------------+---------------+---------------+
| **Overall (47 ops)**      | **0.286 µs**  | **6.931 ms**  | **24.20×**    |
+---------------------------+---------------+---------------+---------------+

Notable single-operation speedups from the same run include
:meth:`~mimesis.Person.full_name` (~27×), address (~34×), company name (~150×),
and generating 100 names in one call (~27×).

Memory
------

+------------------------------------+---------------+---------------+-----------------+
| Workload                           | Mimesis peak  | Faker peak    | Faker / Mimesis |
+====================================+===============+===============+=================+
| Names                              | 3.39 MiB      | 3.49 MiB      | 1.03×           |
+------------------------------------+---------------+---------------+-----------------+
| Emails                             | 3.81 MiB      | 3.85 MiB      | 1.01×           |
+------------------------------------+---------------+---------------+-----------------+
| Addresses                          | 3.63 MiB      | 4.92 MiB      | 1.36×           |
+------------------------------------+---------------+---------------+-----------------+
| User profiles                      | 34.54 MiB     | 43.21 MiB     | 1.25×           |
+------------------------------------+---------------+---------------+-----------------+
| **Total across scenarios**         | **45.36 MiB** | **55.48 MiB** | **1.22×**       |
+------------------------------------+---------------+---------------+-----------------+

Peaks are measured with Python’s ``tracemalloc`` for one batch run after a warm-up.
Absolute values depend on interpreter and machine; the relative gap is what matters.

Uniqueness
----------

Sample size: **100,000**. Uniqueness is measured for one continuous generation
run (no reseeding between values).

+---------------+-------------+-------------------+-----------------+
| Operation     | Samples     | Mimesis           | Faker           |
+===============+=============+===================+=================+
| full_name     | 100,000     | 98.28%            | 70.98%          |
+---------------+-------------+-------------------+-----------------+
| email         | 100,000     | 99.81%            | 85.67%          |
+---------------+-------------+-------------------+-----------------+
| username      | 100,000     | 98.25%            | 72.05%          |
+---------------+-------------+-------------------+-----------------+
| phone_number  | 100,000     | 100.00%           | 100.00%         |
+---------------+-------------+-------------------+-----------------+
| address       | 100,000     | 99.98%            | 100.00%         |
+---------------+-------------+-------------------+-----------------+
| url           | 100,000     | 94.88%            | 46.88%          |
+---------------+-------------+-------------------+-----------------+

Across these 6 uniqueness comparisons, Mimesis averaged **98.53%** unique values
versus **79.27%** for Faker (4 wins for Mimesis, 2 for Faker by tiny margins on
``phone_number`` / ``address``).
