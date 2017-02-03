from unittest import TestCase

from tests.test_generic import LocaleBase


class DanishTest(LocaleBase, TestCase):
    LANG = 'da'


class GermanTest(LocaleBase, TestCase):
    LANG = 'de'


class EnglishTest(LocaleBase, TestCase):
    LANG = 'en'


class EnglishGreatBritainTest(LocaleBase, TestCase):
    LANG = 'en-gb'


class SpanishTest(LocaleBase, TestCase):
    LANG = 'es'


class FarsiTest(LocaleBase, TestCase):
    LANG = 'fa'


class FinnishTest(LocaleBase, TestCase):
    LANG = 'fi'


class FrenchTest(LocaleBase, TestCase):
    LANG = 'fr'


class IcelandicTest(LocaleBase, TestCase):
    LANG = 'is'


class ItalianTest(LocaleBase, TestCase):
    LANG = 'it'


class DutchTest(LocaleBase, TestCase):
    LANG = 'nl'


class NorwegianTest(LocaleBase, TestCase):
    LANG = 'no'


class PolishTest(LocaleBase, TestCase):
    LANG = 'pl'


class PortugueseTest(LocaleBase, TestCase):
    LANG = 'pt'


class BrazilianTest(LocaleBase, TestCase):
    LANG = 'pt-br'


class RussianTest(LocaleBase, TestCase):
    LANG = 'ru'


class SwedishTest(LocaleBase, TestCase):
    LANG = 'sv'


class HungarianTest(LocaleBase, TestCase):
    LANG = 'hu'


class KoreanTest(LocaleBase, TestCase):
    LANG = 'ko'


class CzechTest(LocaleBase, TestCase):
    LANG = 'cs'


class JapaneseTest(LocaleBase, TestCase):
    LANG = 'jp'


class TurkishTest(LocaleBase, TestCase):
    LANG = 'tr'
