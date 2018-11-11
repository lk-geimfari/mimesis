# import contextlib
# from typing import Generator
#
# from mimesis import providers
# from mimesis.utils import pull

CS = 'cs'
DA = 'da'
DE = 'de'
DE_AT = 'de-at'
DE_CH = 'de-ch'
EL = 'el'
EN = 'en'
EN_AU = 'en-au'
EN_CA = 'en-ca'
EN_GB = 'en-gb'
ES = 'es'
ES_MX = 'es-mx'
ET = 'et'
FA = 'fa'
FI = 'fi'
FR = 'fr'
HU = 'hu'
IS = 'is'
IT = 'it'
JA = 'ja'
KK = 'kk'
KO = 'ko'
NL = 'nl'
NL_BE = 'nl-be'
NO = 'no'
PL = 'pl'
PT = 'pt'
PT_BR = 'pt-br'
RU = 'ru'
SV = 'sv'
TR = 'tr'
UK = 'uk'
ZH = 'zh'

DEFAULT_LOCALE = EN

SUPPORTED_LOCALES = {
    'cs': {
        'name': 'Czech',
        'name_local': 'česky',
    },
    'da': {
        'name': 'Danish',
        'name_local': 'Dansk',
    },
    'de': {
        'name': 'German',
        'name_local': 'Deutsch',
    },
    'de-at': {
        'name': 'Austrian German',
        'name_local': 'Deutsch',
    },
    'de-ch': {
        'name': 'Swiss German',
        'name_local': 'Deutsch',
    },
    'el': {
        'name': 'Greek',
        'name_local': 'Ελληνικά',
    },
    'en': {
        'name': 'English',
        'name_local': 'English',
    },
    'en-gb': {
        'name': 'British English',
        'name_local': 'English',
    },
    'en-au': {
        'name': 'Australian English',
        'name_local': 'English',
    },
    'en-ca': {
        'name': 'Canadian English',
        'name_local': 'English',
    },
    'es': {
        'name': 'Spanish',
        'name_local': 'Español',
    },
    'es-mx': {
        'name': 'Mexican Spanish',
        'name_local': 'Español',
    },
    'et': {
        'name': 'Estonian',
        'name_local': 'Eesti',
    },
    'fa': {
        'name': 'Farsi',
        'name_local': 'فارسی',
    },
    'fi': {
        'name': 'Finnish',
        'name_local': 'Suomi',
    },
    'fr': {
        'name': 'French',
        'name_local': 'Français',
    },
    'hu': {
        'name': 'Hungarian',
        'name_local': 'Magyar',
    },
    'is': {
        'name': 'Icelandic',
        'name_local': 'Íslenska',
    },
    'it': {
        'name': 'Italian',
        'name_local': 'Italiano',
    },
    'ja': {
        'name': 'Japanese',
        'name_local': '日本語',
    },
    'kk': {
        'name': 'Kazakh',
        'name_local': 'Қазақша',
    },
    'ko': {
        'name': 'Korean',
        'name_local': '한국어',
    },
    'nl': {
        'name': 'Dutch',
        'name_local': 'Nederlands',
    },
    'nl-be': {
        'name': 'Belgium Dutch',
        'name_local': 'Nederlands',
    },
    'no': {
        'name': 'Norwegian',
        'name_local': 'Norsk',
    },
    'pl': {
        'name': 'Polish',
        'name_local': 'Polski',
    },
    'pt': {
        'name': 'Portuguese',
        'name_local': 'Português',
    },
    'pt-br': {
        'name': 'Brazilian Portuguese',
        'name_local': 'Português Brasileiro',
    },
    'ru': {
        'name': 'Russian',
        'name_local': 'Русский',
    },
    'sv': {
        'name': 'Swedish',
        'name_local': 'Svenska',
    },
    'tr': {
        'name': 'Turkish',
        'name_local': 'Türkçe',
    },
    'uk': {
        'name': 'Ukrainian',
        'name_local': 'Українська',
    },
    'zh': {
        'name': 'Chinese',
        'name_local': '汉语',
    },
}

LIST_OF_LOCALES = list(SUPPORTED_LOCALES)

# DataProviderType = providers.BaseDataProvider
#
#
# @contextlib.contextmanager
# def override(provider: DataProviderType,
#              locale: str = EN) -> Generator[DataProviderType, None, None]:
#     """Context manager which allows overriding current locale.
#
#     :param provider: Locale dependent data provider.
#     :param locale: Locale.
#     :return:
#     """
#     origin_locale = getattr(provider, 'locale', None)
#     datafile = getattr(provider, '_datafile', None)
#
#     if not datafile or not locale:
#         raise ValueError('«{}» has not locale dependent'.format(
#             provider.__class__.__name__))
#
#     provider.locale = locale
#     provider._data = pull(datafile, locale)
#
#     try:
#         yield provider
#     finally:
#         provider.locale = origin_locale
#         provider._data = pull(datafile, origin_locale)
