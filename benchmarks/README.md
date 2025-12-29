## Intro

The benchmark was conducted on a MacBook Pro 14″ with an Apple M1 Pro and 32 GB of RAM.


## Performance Summary

Based on the benchmark results, **Mimesis consistently and decisively outperforms Faker across all tested scenarios**.

- **100% win rate**: Mimesis was faster in **all 47 operations** tested.
- **Overall speedup**: On average, Mimesis is **~23× faster** than Faker.

Performance gains are especially noticeable in real-world workloads:

- **Text, Address, Internet, and Generic providers** show typical speedups of **20–30×**.
- **Finance and company-related data** reach extreme gains of **up to ~140× faster**.
- **Complex operations** (e.g. complete user profiles and bulk generation) are **~25× faster**, reducing
  millisecond-level Faker workloads to microsecond-level execution with Mimesis.

Overall, **Mimesis operates at nanosecond–microsecond scale where Faker frequently operates at microsecond–millisecond
scale**.


## Output

```
====================================================================================================
                              PERFORMANCE COMPARISON: MIMESIS VS FAKER
====================================================================================================

Iterations per test: 20,000
Locale: en

====================================================================================================

📊 Benchmarking Person Provider...
  Benchmarking full_name... ✓
  Benchmarking first_name... ✓
  Benchmarking last_name... ✓
  Benchmarking email... ✓
  Benchmarking phone_number... ✓
  Benchmarking username... ✓
  Benchmarking password... ✓

====================================================================================================
                                          PERSON PROVIDER
====================================================================================================
Operation                      Mimesis (avg)   Faker (avg)     Speedup         Winner
----------------------------------------------------------------------------------------------------
full_name                      0.002 µs        0.055 µs        25.72x           🏆 Mimesis
first_name                     0.002 µs        0.025 µs        14.82x           🏆 Mimesis
last_name                      0.542 ns        0.037 µs        68.21x           🏆 Mimesis
email                          0.002 µs        0.054 µs        22.88x           🏆 Mimesis
phone_number                   0.002 µs        0.009 µs        4.33x           🏆 Mimesis
username                       0.002 µs        0.052 µs        22.51x           🏆 Mimesis
password                       0.001 µs        0.007 µs        6.66x           🏆 Mimesis
----------------------------------------------------------------------------------------------------
TOTAL                          0.012 µs        0.239 µs        19.57x           🏆 Mimesis
====================================================================================================


📊 Benchmarking Address Provider...
  Benchmarking address... ✓
  Benchmarking city... ✓
  Benchmarking country... ✓
  Benchmarking street_name... ✓
  Benchmarking zip_code... ✓
  Benchmarking state... ✓

====================================================================================================
                                          ADDRESS PROVIDER
====================================================================================================
Operation                      Mimesis (avg)   Faker (avg)     Speedup         Winner
----------------------------------------------------------------------------------------------------
address                        0.002 µs        0.075 µs        32.53x           🏆 Mimesis
city                           0.485 ns        0.032 µs        66.54x           🏆 Mimesis
country                        0.511 ns        0.002 µs        2.99x           🏆 Mimesis
street_name                    0.557 ns        0.035 µs        62.92x           🏆 Mimesis
zip_code                       0.001 µs        0.001 µs        1.25x           🏆 Mimesis
state                          0.510 ns        0.002 µs        2.98x           🏆 Mimesis
----------------------------------------------------------------------------------------------------
TOTAL                          0.005 µs        0.147 µs        26.76x           🏆 Mimesis
====================================================================================================


📊 Benchmarking Internet Provider...
  Benchmarking url... ✓
  Benchmarking domain_name... ✓
  Benchmarking ipv4... ✓
  Benchmarking ipv6... ✓
  Benchmarking mac_address... ✓
  Benchmarking user_agent... ✓

====================================================================================================
                                         INTERNET PROVIDER
====================================================================================================
Operation                      Mimesis (avg)   Faker (avg)     Speedup         Winner
----------------------------------------------------------------------------------------------------
url                            0.003 µs        0.083 µs        31.42x           🏆 Mimesis
domain_name                    0.002 µs        0.080 µs        35.49x           🏆 Mimesis
ipv4                           0.001 µs        0.022 µs        16.60x           🏆 Mimesis
ipv6                           0.003 µs        0.004 µs        1.38x           🏆 Mimesis
mac_address                    0.002 µs        0.004 µs        2.08x           🏆 Mimesis
user_agent                     0.362 ns        0.016 µs        44.41x           🏆 Mimesis
----------------------------------------------------------------------------------------------------
TOTAL                          0.012 µs        0.210 µs        17.95x           🏆 Mimesis
====================================================================================================


📊 Benchmarking Datetime Provider...
  Benchmarking date... ✓
  Benchmarking time... ✓
  Benchmarking year... ✓
  Benchmarking month... ✓
  Benchmarking day_of_week... ✓

====================================================================================================
                                         DATETIME PROVIDER
====================================================================================================
Operation                      Mimesis (avg)   Faker (avg)     Speedup         Winner
----------------------------------------------------------------------------------------------------
date                           0.002 µs        0.005 µs        2.95x           🏆 Mimesis
time                           0.002 µs        0.004 µs        2.73x           🏆 Mimesis
year                           0.476 ns        0.004 µs        9.41x           🏆 Mimesis
month                          0.514 ns        0.004 µs        8.45x           🏆 Mimesis
day_of_week                    0.510 ns        0.004 µs        8.55x           🏆 Mimesis
----------------------------------------------------------------------------------------------------
TOTAL                          0.005 µs        0.022 µs        4.80x           🏆 Mimesis
====================================================================================================


📊 Benchmarking Text Provider...
  Benchmarking word... ✓
  Benchmarking sentence... ✓
  Benchmarking text... ✓

====================================================================================================
                                           TEXT PROVIDER
====================================================================================================
Operation                      Mimesis (avg)   Faker (avg)     Speedup         Winner
----------------------------------------------------------------------------------------------------
word                           0.814 ns        0.007 µs        8.64x           🏆 Mimesis
sentence                       0.790 ns        0.009 µs        11.42x           🏆 Mimesis
text                           0.001 µs        0.058 µs        55.71x           🏆 Mimesis
----------------------------------------------------------------------------------------------------
TOTAL                          0.003 µs        0.074 µs        28.07x           🏆 Mimesis
====================================================================================================


📊 Benchmarking Finance Provider...
  Benchmarking currency_code... ✓
  Benchmarking company... ✓
  Benchmarking stock_ticker... ✓

====================================================================================================
                                          FINANCE PROVIDER
====================================================================================================
Operation                      Mimesis (avg)   Faker (avg)     Speedup         Winner
----------------------------------------------------------------------------------------------------
currency_code                  0.263 ns        0.002 µs        6.06x           🏆 Mimesis
company                        0.556 ns        0.077 µs        138.98x           🏆 Mimesis
stock_ticker                   0.359 ns        0.001 µs        2.79x           🏆 Mimesis
----------------------------------------------------------------------------------------------------
TOTAL                          0.001 µs        0.080 µs        67.79x           🏆 Mimesis
====================================================================================================


📊 Benchmarking Payment Provider...
  Benchmarking credit_card_number... ✓
  Benchmarking credit_card_expiration_date... ✓
  Benchmarking cvv... ✓

====================================================================================================
                                          PAYMENT PROVIDER
====================================================================================================
Operation                      Mimesis (avg)   Faker (avg)     Speedup         Winner
----------------------------------------------------------------------------------------------------
credit_card_number             0.007 µs        0.012 µs        1.64x           🏆 Mimesis
credit_card_expiration_date    0.972 ns        0.008 µs        7.94x           🏆 Mimesis
cvv                            0.591 ns        0.004 µs        7.52x           🏆 Mimesis
----------------------------------------------------------------------------------------------------
TOTAL                          0.009 µs        0.024 µs        2.71x           🏆 Mimesis
====================================================================================================


📊 Benchmarking Code Provider...
  Benchmarking isbn... ✓
  Benchmarking ean... ✓

====================================================================================================
                                           CODE PROVIDER
====================================================================================================
Operation                      Mimesis (avg)   Faker (avg)     Speedup         Winner
----------------------------------------------------------------------------------------------------
isbn                           0.003 µs        0.011 µs        3.88x           🏆 Mimesis
ean                            0.003 µs        0.009 µs        3.39x           🏆 Mimesis
----------------------------------------------------------------------------------------------------
TOTAL                          0.005 µs        0.020 µs        3.66x           🏆 Mimesis
====================================================================================================


📊 Benchmarking Numeric Provider...
  Benchmarking integer_number... ✓
  Benchmarking float_number... ✓

====================================================================================================
                                          NUMERIC PROVIDER
====================================================================================================
Operation                      Mimesis (avg)   Faker (avg)     Speedup         Winner
----------------------------------------------------------------------------------------------------
integer_number                 0.487 ns        0.001 µs        2.55x           🏆 Mimesis
float_number                   0.739 ns        0.004 µs        5.65x           🏆 Mimesis
----------------------------------------------------------------------------------------------------
TOTAL                          0.001 µs        0.005 µs        4.42x           🏆 Mimesis
====================================================================================================


📊 Benchmarking Generic Provider (All-in-One)...
  Benchmarking generic_person_name... ✓
  Benchmarking generic_address... ✓
  Benchmarking generic_email... ✓
  Benchmarking generic_date... ✓
  Benchmarking generic_text... ✓
  Benchmarking generic_company... ✓
  Benchmarking generic_phone... ✓
  Benchmarking generic_ipv4... ✓

====================================================================================================
                                          GENERIC PROVIDER
====================================================================================================
Operation                      Mimesis (avg)   Faker (avg)     Speedup         Winner
----------------------------------------------------------------------------------------------------
generic_person_name            0.002 µs        0.055 µs        25.60x           🏆 Mimesis
generic_address                0.002 µs        0.076 µs        33.09x           🏆 Mimesis
generic_email                  0.002 µs        0.054 µs        22.44x           🏆 Mimesis
generic_date                   0.002 µs        0.005 µs        2.96x           🏆 Mimesis
generic_text                   0.913 ns        0.009 µs        9.88x           🏆 Mimesis
generic_company                0.595 ns        0.077 µs        129.93x           🏆 Mimesis
generic_phone                  0.002 µs        0.010 µs        4.34x           🏆 Mimesis
generic_ipv4                   0.001 µs        0.022 µs        16.22x           🏆 Mimesis
----------------------------------------------------------------------------------------------------
TOTAL                          0.013 µs        0.307 µs        22.82x           🏆 Mimesis
====================================================================================================


📊 Benchmarking Complex Operations...
  Benchmarking complete_user_profile... ✓
  Benchmarking generate_100_names... ✓

====================================================================================================
                                         COMPLEX OPERATIONS
====================================================================================================
Operation                      Mimesis (avg)   Faker (avg)     Speedup         Winner
----------------------------------------------------------------------------------------------------
complete_user_profile          0.017 µs        0.372 µs        22.22x           🏆 Mimesis
generate_100_names             0.212 µs        5.362 ms        25.25x           🏆 Mimesis
----------------------------------------------------------------------------------------------------
TOTAL                          0.229 µs        5.734 ms        25.03x           🏆 Mimesis
====================================================================================================


====================================================================================================
                                          OVERALL SUMMARY
====================================================================================================

Total Operations Tested: 47
Mimesis Wins: 47 (100.0%)
Faker Wins: 0 (0.0%)

Total Execution Time:
  Mimesis: 0.296 µs
  Faker:   6.863 ms

Overall Speedup: 23.18x

🏆 Overall Winner: Mimesis

====================================================================================================
```
