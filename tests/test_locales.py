from unittest import TestCase

from tests.test_generic import LocaleBase


class DanishTestCase(LocaleBase, TestCase):
    LANG = 'da'


class GermanTestCase(LocaleBase, TestCase):
    LANG = 'de'


class EnglishTestCase(LocaleBase, TestCase):
    LANG = 'en'


class SpanishTestCase(LocaleBase, TestCase):
    LANG = 'es'


class FarsiTestCase(LocaleBase, TestCase):
    LANG = 'fa'


class FinnishTestCase(LocaleBase, TestCase):
    LANG = 'fi'


class FrenchTestCase(LocaleBase, TestCase):
    LANG = 'fr'


class IcelandicTestCase(LocaleBase, TestCase):
    LANG = 'is'


class ItalianTestCase(LocaleBase, TestCase):
    LANG = 'it'


class DutchTestCase(LocaleBase, TestCase):
    LANG = 'nl'


class NorwegianTestCase(LocaleBase, TestCase):
    LANG = 'no'


class PolishTestCase(LocaleBase, TestCase):
    LANG = 'pl'


class PortugueseTestCase(LocaleBase, TestCase):
    LANG = 'pt'


class BrazilianTestCase(LocaleBase, TestCase):
    LANG = 'pt-br'


class RussianTestCase(LocaleBase, TestCase):
    LANG = 'ru'


class SwedishTestCase(LocaleBase, TestCase):
    LANG = 'sv'
