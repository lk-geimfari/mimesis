import statistics
import time
from typing import Callable, Dict, List, Tuple

from mimesis import Generic
from mimesis.locales import Locale
from mimesis.providers import (
    Address,
    Code,
    Datetime,
    Finance,
    Internet,
    Numeric,
    Payment,
    Person,
    Text,
)

try:
    from faker import Faker
except ImportError:
    print("Error: Faker is not installed.")
    exit(1)

ITERATIONS = 20_000
LOCALE = "en"


def benchmark(func: Callable, iterations: int = ITERATIONS) -> Tuple[float, float]:
    """Benchmark a function and return average execution time.

    Args:
        func: Function to benchmark
        iterations: Number of iterations to run

    Returns:
        Tuple of (average_time, median_time) in milliseconds
    """
    times = []

    for _ in range(iterations):
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        times.append((end - start) * 1000)

    return statistics.mean(times), statistics.median(times)


def benchmark_provider(
    name: str,
    mimesis_func: Callable,
    faker_func: Callable,
    iterations: int = ITERATIONS
) -> Dict[str, float]:
    print(f"  Benchmarking {name}...", end=" ", flush=True)

    mimesis_avg, mimesis_median = benchmark(mimesis_func, iterations)
    faker_avg, faker_median = benchmark(faker_func, iterations)

    speedup = faker_avg / mimesis_avg if mimesis_avg > 0 else 0

    print(f"✓")

    return {
        "operation": name,
        "mimesis_avg": mimesis_avg,
        "mimesis_median": mimesis_median,
        "faker_avg": faker_avg,
        "faker_median": faker_median,
        "speedup": speedup,
    }


def format_time(ms: float) -> str:
    if ms < 0.001:
        return f"{ms * 1000:.3f} ns"
    elif ms < 1:
        return f"{ms:.3f} µs"
    else:
        return f"{ms:.3f} ms"


def print_results(results: List[Dict[str, float]], title: str) -> None:
    print(f"\n{'=' * 100}")
    print(f"{title:^100}")
    print(f"{'=' * 100}")
    print(f"{'Operation':<30} {'Mimesis (avg)':<15} {'Faker (avg)':<15} {'Speedup':<15} {'Winner':<15}")
    print(f"{'-' * 100}")

    total_mimesis = 0
    total_faker = 0

    for result in results:
        op = result["operation"]
        mimesis_avg = result["mimesis_avg"]
        faker_avg = result["faker_avg"]
        speedup = result["speedup"]

        total_mimesis += mimesis_avg
        total_faker += faker_avg

        winner = "Mimesis" if speedup > 1 else "Faker"
        winner_symbol = "🏆 " if speedup > 1 else ""

        print(
            f"{op:<30} "
            f"{format_time(mimesis_avg):<15} "
            f"{format_time(faker_avg):<15} "
            f"{speedup:.2f}x{'':<10} "
            f"{winner_symbol}{winner:<15}"
        )

    print(f"{'-' * 100}")
    print(
        f"{'TOTAL':<30} "
        f"{format_time(total_mimesis):<15} "
        f"{format_time(total_faker):<15} "
        f"{(total_faker / total_mimesis):.2f}x{'':<10} "
        f"{'🏆 Mimesis' if total_faker > total_mimesis else 'Faker':<15}"
    )
    print(f"{'=' * 100}\n")


def benchmark_person_provider() -> List[Dict[str, float]]:
    print("\n📊 Benchmarking Person Provider...")

    fkr = Faker(LOCALE)
    mim_person = Person(locale=Locale.EN)

    results = [
        benchmark_provider(
            "full_name",
            lambda: mim_person.full_name(),
            lambda: fkr.name()
        ),
        benchmark_provider(
            "first_name",
            lambda: mim_person.first_name(),
            lambda: fkr.first_name()
        ),
        benchmark_provider(
            "last_name",
            lambda: mim_person.last_name(),
            lambda: fkr.last_name()
        ),
        benchmark_provider(
            "email",
            lambda: mim_person.email(),
            lambda: fkr.email()
        ),
        benchmark_provider(
            "phone_number",
            lambda: mim_person.phone_number(),
            lambda: fkr.phone_number()
        ),
        benchmark_provider(
            "username",
            lambda: mim_person.username(),
            lambda: fkr.user_name()
        ),
        benchmark_provider(
            "password",
            lambda: mim_person.password(),
            lambda: fkr.password()
        )
    ]

    return results


def benchmark_address_provider() -> List[Dict[str, float]]:
    print("\n📊 Benchmarking Address Provider...")

    mimesis_address = Address(locale=Locale.EN)
    faker_address = Faker(LOCALE)

    results = [
        benchmark_provider(
            "address",
            lambda: mimesis_address.address(),
            lambda: faker_address.address()
        ),
        benchmark_provider(
            "city",
            lambda: mimesis_address.city(),
            lambda: faker_address.city()
        ),
        benchmark_provider(
            "country",
            lambda: mimesis_address.country(),
            lambda: faker_address.country()
        ),
        benchmark_provider(
            "street_name",
            lambda: mimesis_address.street_name(),
            lambda: faker_address.street_name()
        ),
        benchmark_provider(
            "zip_code",
            lambda: mimesis_address.zip_code(),
            lambda: faker_address.zipcode()
        ),
        benchmark_provider(
            "state",
            lambda: mimesis_address.state(),
            lambda: faker_address.state()
        ),
    ]
    return results


def benchmark_internet_provider() -> List[Dict[str, float]]:
    print("\n📊 Benchmarking Internet Provider...")

    mimesis_internet = Internet()
    faker_internet = Faker(LOCALE)

    results = [
        benchmark_provider(
            "url",
            lambda: mimesis_internet.url(),
            lambda: faker_internet.url()
        ),
        benchmark_provider(
            "domain_name",
            lambda: mimesis_internet.hostname(),
            lambda: faker_internet.domain_name()
        ),
        benchmark_provider(
            "ipv4",
            lambda: mimesis_internet.ip_v4(),
            lambda: faker_internet.ipv4()
        ),
        benchmark_provider(
            "ipv6",
            lambda: mimesis_internet.ip_v6(),
            lambda: faker_internet.ipv6()
        ),
        benchmark_provider(
            "mac_address",
            lambda: mimesis_internet.mac_address(),
            lambda: faker_internet.mac_address()
        ),
        benchmark_provider(
            "user_agent",
            lambda: mimesis_internet.user_agent(),
            lambda: faker_internet.user_agent()
        ),
    ]
    return results


def benchmark_datetime_provider() -> List[Dict[str, float]]:
    print("\n📊 Benchmarking Datetime Provider...")

    mimesis_datetime = Datetime(locale=Locale.EN)
    faker_datetime = Faker(LOCALE)

    results = [
        benchmark_provider(
            "date",
            lambda: mimesis_datetime.date(),
            lambda: faker_datetime.date()
        ),
        benchmark_provider(
            "time",
            lambda: mimesis_datetime.time(),
            lambda: faker_datetime.time()
        ),
        benchmark_provider(
            "year",
            lambda: mimesis_datetime.year(),
            lambda: faker_datetime.year()
        ),
        benchmark_provider(
            "month",
            lambda: mimesis_datetime.month(),
            lambda: faker_datetime.month_name()
        ),
        benchmark_provider(
            "day_of_week",
            lambda: mimesis_datetime.day_of_week(),
            lambda: faker_datetime.day_of_week()
        ),
    ]
    return results


def benchmark_text_provider() -> List[Dict[str, float]]:
    print("\n📊 Benchmarking Text Provider...")

    mim_text = Text(locale=Locale.EN)
    fkr = Faker(LOCALE)

    results = [
        benchmark_provider(
            "word",
            lambda: mim_text.word(),
            lambda: fkr.word()
        ), benchmark_provider(
            "sentence",
            lambda: mim_text.sentence(),
            lambda: fkr.sentence()
        ), benchmark_provider(
            "text",
            lambda: mim_text.text(),
            lambda: fkr.text()
        ),
    ]
    return results


def benchmark_finance_provider() -> List[Dict[str, float]]:
    print("\n📊 Benchmarking Finance Provider...")

    mimesis_finance = Finance(locale=Locale.EN)
    faker_finance = Faker(LOCALE)

    results = [
        benchmark_provider(
            "currency_code",
            lambda: mimesis_finance.currency_iso_code(),
            lambda: faker_finance.currency_code()
        ), benchmark_provider(
            "company",
            lambda: mimesis_finance.company(),
            lambda: faker_finance.company()
        ), benchmark_provider(
            "stock_ticker",
            lambda: mimesis_finance.stock_ticker(),
            lambda: faker_finance.stock_ticker() if hasattr(faker_finance, 'stock_ticker') else None
        ),
    ]
    return results


def benchmark_payment_provider() -> List[Dict[str, float]]:
    print("\n📊 Benchmarking Payment Provider...")

    mim_payment = Payment()
    fkr = Faker(LOCALE)

    results = [
        benchmark_provider(
            "credit_card_number",
            lambda: mim_payment.credit_card_number(),
            lambda: fkr.credit_card_number()
        ), benchmark_provider(
            "credit_card_expiration_date",
            lambda: mim_payment.credit_card_expiration_date(),
            lambda: fkr.credit_card_expire()
        ), benchmark_provider(
            "cvv",
            lambda: mim_payment.cvv(),
            lambda: fkr.credit_card_security_code()
        ),
    ]
    return results


def benchmark_code_provider() -> List[Dict[str, float]]:
    print("\n📊 Benchmarking Code Provider...")

    mimesis_code = Code()
    faker_code = Faker(LOCALE)

    results = [
        benchmark_provider(
            "isbn",
            lambda: mimesis_code.isbn(),
            lambda: faker_code.isbn13()
        ), benchmark_provider(
            "ean",
            lambda: mimesis_code.ean(),
            lambda: faker_code.ean()
        ),
    ]
    return results


def benchmark_numeric_provider() -> List[Dict[str, float]]:
    print("\n📊 Benchmarking Numeric Provider...")

    mimesis_numeric = Numeric()
    faker_numeric = Faker(LOCALE)

    results = [
        benchmark_provider(
            "integer_number",
            lambda: mimesis_numeric.integer_number(0, 1000),
            lambda: faker_numeric.random_int(0, 1000)
        ), benchmark_provider(
            "float_number",
            lambda: mimesis_numeric.float_number(0, 100),
            lambda: faker_numeric.pyfloat(min_value=0, max_value=100)
        ),
    ]
    return results


def benchmark_generic_provider() -> List[Dict[str, float]]:
    print("\n📊 Benchmarking Generic Provider (All-in-One)...")

    mimesis_generic = Generic(locale=Locale.EN)
    faker_generic = Faker(LOCALE)

    results = [
        benchmark_provider(
            "generic_person_name",
            lambda: mimesis_generic.person.full_name(),
            lambda: faker_generic.name()
        ), benchmark_provider(
            "generic_address",
            lambda: mimesis_generic.address.address(),
            lambda: faker_generic.address()
        ), benchmark_provider(
            "generic_email",
            lambda: mimesis_generic.person.email(),
            lambda: faker_generic.email()
        ), benchmark_provider(
            "generic_date",
            lambda: mimesis_generic.datetime.date(),
            lambda: faker_generic.date()
        ), benchmark_provider(
            "generic_text",
            lambda: mimesis_generic.text.sentence(),
            lambda: faker_generic.sentence()
        ), benchmark_provider(
            "generic_company",
            lambda: mimesis_generic.finance.company(),
            lambda: faker_generic.company()
        ), benchmark_provider(
            "generic_phone",
            lambda: mimesis_generic.person.phone_number(),
            lambda: faker_generic.phone_number()
        ), benchmark_provider(
            "generic_ipv4",
            lambda: mimesis_generic.internet.ip_v4(),
            lambda: faker_generic.ipv4()
        ),
    ]
    return results


def benchmark_complex_operations() -> List[Dict[str, float]]:
    print("\n📊 Benchmarking Complex Operations...")

    mimesis_generic = Generic(locale=Locale.EN)
    faker_generic = Faker(LOCALE)

    results = []

    def mimesis_user_profile():
        return {
            "name": mimesis_generic.person.full_name(),
            "email": mimesis_generic.person.email(),
            "username": mimesis_generic.person.username(),
            "password": mimesis_generic.person.password(),
            "phone": mimesis_generic.person.phone_number(),
            "address": mimesis_generic.address.address(),
            "city": mimesis_generic.address.city(),
            "country": mimesis_generic.address.country(),
            "birthdate": mimesis_generic.datetime.date(),
            "company": mimesis_generic.finance.company(),
        }

    def faker_user_profile():
        return {
            "name": faker_generic.name(),
            "email": faker_generic.email(),
            "username": faker_generic.user_name(),
            "password": faker_generic.password(),
            "phone": faker_generic.phone_number(),
            "address": faker_generic.address(),
            "city": faker_generic.city(),
            "country": faker_generic.country(),
            "birthdate": faker_generic.date(),
            "company": faker_generic.company(),
        }

    results.append(benchmark_provider(
        "complete_user_profile",
        mimesis_user_profile,
        faker_user_profile
    ))

    def mimesis_list_generation():
        return [mimesis_generic.person.full_name() for _ in range(100)]

    def faker_list_generation():
        return [faker_generic.name() for _ in range(100)]

    results.append(benchmark_provider(
        "generate_100_names",
        mimesis_list_generation,
        faker_list_generation,
        iterations=100
    ))

    return results


def main():
    """Run all benchmarks."""
    print(f"\n{'=' * 100}")
    print(f"{'PERFORMANCE COMPARISON: MIMESIS VS FAKER':^100}")
    print(f"{'=' * 100}")
    print(f"\nIterations per test: {ITERATIONS:,}")
    print(f"Locale: {LOCALE}")
    print(f"\n{'=' * 100}")

    all_results = []

    # Individual provider benchmarks
    person_results = benchmark_person_provider()
    print_results(person_results, "PERSON PROVIDER")
    all_results.extend(person_results)

    address_results = benchmark_address_provider()
    print_results(address_results, "ADDRESS PROVIDER")
    all_results.extend(address_results)

    internet_results = benchmark_internet_provider()
    print_results(internet_results, "INTERNET PROVIDER")
    all_results.extend(internet_results)

    datetime_results = benchmark_datetime_provider()
    print_results(datetime_results, "DATETIME PROVIDER")
    all_results.extend(datetime_results)

    text_results = benchmark_text_provider()
    print_results(text_results, "TEXT PROVIDER")
    all_results.extend(text_results)

    finance_results = benchmark_finance_provider()
    print_results(finance_results, "FINANCE PROVIDER")
    all_results.extend(finance_results)

    payment_results = benchmark_payment_provider()
    print_results(payment_results, "PAYMENT PROVIDER")
    all_results.extend(payment_results)

    code_results = benchmark_code_provider()
    print_results(code_results, "CODE PROVIDER")
    all_results.extend(code_results)

    numeric_results = benchmark_numeric_provider()
    print_results(numeric_results, "NUMERIC PROVIDER")
    all_results.extend(numeric_results)

    # Generic provider benchmarks
    generic_results = benchmark_generic_provider()
    print_results(generic_results, "GENERIC PROVIDER")
    all_results.extend(generic_results)

    # Complex operations
    complex_results = benchmark_complex_operations()
    print_results(complex_results, "COMPLEX OPERATIONS")
    all_results.extend(complex_results)

    # Overall summary
    print(f"\n{'=' * 100}")
    print(f"{'OVERALL SUMMARY':^100}")
    print(f"{'=' * 100}")

    total_mimesis = sum(r["mimesis_avg"] for r in all_results)
    total_faker = sum(r["faker_avg"] for r in all_results)
    overall_speedup = total_faker / total_mimesis

    mimesis_wins = sum(1 for r in all_results if r["speedup"] > 1)
    faker_wins = len(all_results) - mimesis_wins

    print(f"\nTotal Operations Tested: {len(all_results)}")
    print(f"Mimesis Wins: {mimesis_wins} ({mimesis_wins / len(all_results) * 100:.1f}%)")
    print(f"Faker Wins: {faker_wins} ({faker_wins / len(all_results) * 100:.1f}%)")
    print(f"\nTotal Execution Time:")
    print(f"  Mimesis: {format_time(total_mimesis)}")
    print(f"  Faker:   {format_time(total_faker)}")
    print(f"\nOverall Speedup: {overall_speedup:.2f}x")
    print(f"\n{'🏆 ' if overall_speedup > 1 else ''}Overall Winner: {'Mimesis' if overall_speedup > 1 else 'Faker'}")
    print(f"\n{'=' * 100}\n")


if __name__ == "__main__":
    main()
