"""The module **mimesis.keys** provides a set of key functions.

Key functions can be applied to fields and fieldsets using the **key** argument.
These functions are applied after the field's value is generated and before the
field is returned to the caller.
"""

import base64
import hashlib
import re
from collections.abc import Iterable
from typing import Any, Callable

from mimesis.datasets import COMMON_LETTERS, ROMANIZATION_DICT
from mimesis.locales import Locale, validate_locale
from mimesis.random import Random

__all__ = [
    "maybe",
    "romanize",
    "wrap",
    "reverse",
    "slugify",
    "snake_case",
    "camel_case",
    "kebab_case",
    "truncate",
    "remove_whitespace",
    "prefix",
    "suffix",
    "hash_with",
    "base64_encode",
    "urlsafe_base64_encode",
    "redact",
    "join",
    "take_first",
    "take_last",
    "apply_if",
    "pipe",
]


def romanize(locale: Locale) -> Callable[[str], str]:
    """Create a closure function to romanize a given string in the specified locale.

    Supported locales are:

    - Locale.RU (Russian)
    - Locale.UK (Ukrainian)
    - Locale.KK (Kazakh)

    :param locale: Locale.
    :return: A closure that takes a string and returns a romanized string.
    """
    locale = validate_locale(locale)

    if locale not in (Locale.RU, Locale.UK, Locale.KK):
        raise ValueError(f"Romanization is not available for: {locale}")

    table = str.maketrans({**ROMANIZATION_DICT[locale.value], **COMMON_LETTERS})

    def key(v: str) -> str:
        """Romanize a given string in the specified locale.

        :param v: Cyrillic string.
        :return: Romanized string.
        """
        if not isinstance(v, str):
            raise TypeError(f"romanize() requires a string, got {type(v).__name__}")

        return v.translate(table)

    return key


def maybe(value: Any, probability: float = 0.5) -> Callable[[Any, Random], Any]:
    """Return a closure (a key function).

    The returned closure itself returns either **value** or
    the first argument passed to closure with a certain probability (0.5 by default).

    :param value: The value that may be returned.
    :param probability: The probability of returning **value**.
    :return: A closure that takes two arguments.
    """

    def key(result: Any, random: Random) -> Any:
        if 0 < probability <= 1:
            value_weight = 1 - probability
            (result,) = random.choices(
                population=[result, value],
                weights=[value_weight, probability],
                k=1,
            )
        return result

    return key


def wrap(before: str = "<", after: str = ">") -> Callable[[str], str]:
    """Wrap result with before and after strings.

    Example:
        >>> field('word', key=wrap('[', ']'))
        '[dynamics]'

    :param before: String to prepend.
    :param after: String to append.
    :return: A closure that wraps a string.
    :raises TypeError: If the result is not a string.
    """

    def key(v: str) -> str:
        if not isinstance(v, str):
            raise TypeError(f"wrap() requires a string, got {type(v).__name__}")
        return f"{before}{v}{after}"

    return key


def reverse(value: str) -> str:
    """Reverse the string.

    :param value: Input string to reverse.
    :return: Reversed string.
    :raises TypeError: If result is not a string.

    Example:
        >>> field('word', key=reverse)
        'ebircsed'

    """
    if not isinstance(value, str):
        raise TypeError(f"reverse() requires a string, got {type(value).__name__}")
    return value[::-1]


def slugify(value: str) -> str:
    """Convert to URL-friendly slug.

    Example:
        >>> field('sentence', key=slugify)
        'where-are-my-pants'

    :param value: Input string to slugify.
    :return: URL-friendly slug.
    :raises TypeError: If result is not a string.
    """
    if not isinstance(value, str):
        raise TypeError(f"slugify() requires a string, got {type(value).__name__}")
    value = value.lower()
    value = re.sub(r"[^\w\s-]", "", value)
    value = re.sub(r"[-\s]+", "-", value)
    return value.strip("-")


def snake_case(value: str) -> str:
    """Convert to snake_case.

    Example:
        >>> field('full_name', key=snake_case)
        'michael_caldwell'

    :param value: Input string to convert.
    :return: snake_case string.
    :raises TypeError: If result is not a string.
    """
    if not isinstance(value, str):
        raise TypeError(f"snake_case() requires a string, got {type(value).__name__}")
    value = value.strip().replace(" ", "_")
    value = re.sub(r"[^\w_]", "", value)
    return value.lower()


def camel_case(value: str) -> str:
    """Convert to camelCase.

    Example:
        >>> field('sentence', key=camel_case)
        'makeMeASandwich.'

    :param value: Input string to convert.
    :return: camelCase string.
    :raises TypeError: If result is not a string.
    """
    if not isinstance(value, str):
        raise TypeError(f"camel_case() requires a string, got {type(value).__name__}")

    words = value.split()
    if not words:
        return ""

    return words[0].lower() + "".join(w.capitalize() for w in words[1:])


def kebab_case(value: str) -> str:
    """Convert to kebab-case.

    :param value: Input string to convert.
    :return: kebab-case string.
    :raises TypeError: If result is not a string.
    """
    return slugify(value)


def truncate(max_length: int, suffix: str = "...") -> Callable[[str], str]:
    """Truncate to maximum length.

    Example:
        >>> field('sentence', key=truncate(20))
        'Ports are created...'

    :param max_length: Maximum length of the result.
    :param suffix: Suffix to add when truncating.
    :return: A closure that truncates a string.
    :raises TypeError: If result is not a string.
    :raises ValueError: If max_length is not positive.
    """
    if max_length <= 0:
        raise ValueError(f"max_length must be positive, got {max_length}")

    def key(result: str) -> str:
        if not isinstance(result, str):
            raise TypeError(
                f"truncate() requires a string, got {type(result).__name__}"
            )
        if len(result) <= max_length:
            return result
        return result[: max_length - len(suffix)] + suffix

    return key


def remove_whitespace(value: str) -> str:
    """Remove all whitespace.

    :param value: Input string.
    :return: String with all whitespace removed.
    :raises TypeError: If result is not a string.
    """
    if not isinstance(value, str):
        raise TypeError(
            f"remove_whitespace() requires a string, got {type(value).__name__}"
        )
    return "".join(value.split())


def prefix(text: str) -> Callable[[str], str]:
    """Add prefix to result.

    Example:
        >>> field('word', key=prefix('user_'))
        'user_order'

    :param text: Prefix text to add.
    :return: A closure that adds a prefix.
    :raises TypeError: If result is not a string.
    """

    def key(v: str) -> str:
        if not isinstance(v, str):
            raise TypeError(f"prefix() requires a string, got {type(v).__name__}")
        return f"{text}{v}"

    return key


def suffix(text: str) -> Callable[[str], str]:
    """Add suffix to result.

    Example:
        >>> field('word', key=suffix('.io'))
        'ecipe.io'

    :param text: Suffix text to add.
    :return: A closure that adds a suffix.
    :raises TypeError: If result is not a string.
    """

    def key(v: str) -> str:
        if not isinstance(v, str):
            raise TypeError(f"suffix() requires a string, got {type(v).__name__}")
        return f"{v}{text}"

    return key


def hash_with(algorithm: str = "sha256") -> Callable[[str], str]:
    """Return a function that hashes a string using the given algorithm.

    Supported algorithms are those available in :mod:`hashlib.algorithms_available`.

    Example:
        >>> field('password', key=hash_with('sha1'))
        'd3e7130d657733468b10c1fd207c4d62b7180cda'

    :param algorithm: Hash algorithm name.
    :return: A closure that hashes a string.
    :raises ValueError: If algorithm is not supported.
    :raises TypeError: If result is not a string.
    """
    if algorithm not in hashlib.algorithms_available:
        raise ValueError(f"Unsupported hash algorithm: {algorithm}")

    def key(v: str) -> str:
        if not isinstance(v, str):
            raise TypeError(f"hash_with() requires a string, got {type(v).__name__}")
        hash_func = hashlib.new(algorithm)
        hash_func.update(v.encode())
        return hash_func.hexdigest()

    return key


def base64_encode(value: str) -> str:
    """Encode as base64.

    :param value: Input string to encode.
    :return: Base64 encoded string.
    :raises TypeError: If result is not a string.

    Example:
        >>> field('word', key=base64_encode)
        'cHJlcGFyZWQ='

    """
    if not isinstance(value, str):
        raise TypeError(
            f"base64_encode() requires a string, got {type(value).__name__}"
        )
    return base64.b64encode(value.encode()).decode()


def urlsafe_base64_encode(value: str) -> str:
    """Encode as URL-safe base64.

    :param value: Input string to encode.
    :return: URL-safe base64 encoded string.
    :raises TypeError: If result is not a string.

    Example:
        >>> field('word', key=urlsafe_base64_encode)
        'YXBwZWFscw=='
    """
    if not isinstance(value, str):
        raise TypeError(
            f"urlsafe_base64_encode() requires a string, got {type(value).__name__}"
        )
    return base64.urlsafe_b64encode(value.encode()).decode()


def redact(replacement: str = "[REDACTED]") -> Callable[[Any], str]:
    """Replace the entire value with redaction marker.

    Example:
        >>> field('password', key=redact('[CLASSIFIED]'))
        '[CLASSIFIED]'

    :param replacement: Replacement text.
    :return: A closure that returns the replacement text.
    """

    def key(_: Any) -> str:
        return replacement

    return key


def join(sep: str = ", ") -> Callable[[list[Any]], str]:
    """Join list items with separator.

    Example:
        >>> field('words', quantity=3, key=join(' | '))
        'pci | promise | excel'

    :param sep: Separator string.
    :return: A closure that joins items.
    :raises TypeError: If the result is not iterable.
    """

    def key(v: Iterable[Any]) -> str:
        if not isinstance(v, Iterable):
            raise TypeError(f"join() requires iterable, got {type(v).__name__}")
        return sep.join(str(item) for item in v)

    return key


def apply_if(
    condition: Callable[[Any], bool],
    transform: Callable[[Any], Any],
    otherwise: Callable[[Any], Any] | None = None,
) -> Callable[[Any], Any]:
    """Apply transform only if the condition is true.

    Example:
        >>> field('word', key=apply_if(lambda x: len(x) > 3, str.upper, str.lower))
        'FIELDS'

    :param condition: Condition function.
    :param transform: Transform function to apply if condition is True.
    :param otherwise: Optional transform to apply if condition is False.
    :return: A closure that conditionally transforms the result.
    """

    def key(v: Any) -> Any:
        if condition(v):
            return transform(v)
        elif otherwise:
            return otherwise(v)
        return v

    return key


Function = Callable[[Any], Any] | Callable[[Any, Random], Any]


def pipe(*functions: Function) -> Function:
    """Pipe multiple key functions together.

    Example:
        >>> field('full_name', key=pipe(str.lower, slugify, prefix('user-')))
        'user-john-doe'

    :param functions: Key functions to pipe together.
    :return: A closure that applies all functions in sequence.
    """

    def key(result: Any, random: Random | None = None) -> Any:
        for func in functions:
            try:
                result = func(result, random)
            except TypeError:
                result = func(result)
        return result

    return key
