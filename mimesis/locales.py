# -*- coding: utf-8 -*-

"""This module provides constants for locale-dependent providers."""

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
SK = 'sk'
SV = 'sv'
TR = 'tr'
UK = 'uk'
ZH = 'zh'

DEFAULT_LOCALE = EN

SUPPORTED_LOCALES = {
    CS: {
        'name': 'Czech',
        'name_local': 'česky',
    },
    DA: {
        'name': 'Danish',
        'name_local': 'Dansk',
    },
    DE: {
        'name': 'German',
        'name_local': 'Deutsch',
    },
    DE_AT: {
        'name': 'Austrian German',
        'name_local': 'Deutsch',
    },
    DE_CH: {
        'name': 'Swiss German',
        'name_local': 'Deutsch',
    },
    EL: {
        'name': 'Greek',
        'name_local': 'Ελληνικά',
    },
    EN: {
        'name': 'English',
        'name_local': 'English',
    },
    EN_GB: {
        'name': 'British English',
        'name_local': 'English',
    },
    EN_AU: {
        'name': 'Australian English',
        'name_local': 'English',
    },
    EN_CA: {
        'name': 'Canadian English',
        'name_local': 'English',
    },
    ES: {
        'name': 'Spanish',
        'name_local': 'Español',
    },
    ES_MX: {
        'name': 'Mexican Spanish',
        'name_local': 'Español',
    },
    ET: {
        'name': 'Estonian',
        'name_local': 'Eesti',
    },
    FA: {
        'name': 'Farsi',
        'name_local': 'فارسی',
    },
    FI: {
        'name': 'Finnish',
        'name_local': 'Suomi',
    },
    FR: {
        'name': 'French',
        'name_local': 'Français',
    },
    HU: {
        'name': 'Hungarian',
        'name_local': 'Magyar',
    },
    IS: {
        'name': 'Icelandic',
        'name_local': 'Íslenska',
    },
    IT: {
        'name': 'Italian',
        'name_local': 'Italiano',
    },
    JA: {
        'name': 'Japanese',
        'name_local': '日本語',
    },
    KK: {
        'name': 'Kazakh',
        'name_local': 'Қазақша',
    },
    KO: {
        'name': 'Korean',
        'name_local': '한국어',
    },
    NL: {
        'name': 'Dutch',
        'name_local': 'Nederlands',
    },
    NL_BE: {
        'name': 'Belgium Dutch',
        'name_local': 'Nederlands',
    },
    NO: {
        'name': 'Norwegian',
        'name_local': 'Norsk',
    },
    PL: {
        'name': 'Polish',
        'name_local': 'Polski',
    },
    PT: {
        'name': 'Portuguese',
        'name_local': 'Português',
    },
    PT_BR: {
        'name': 'Brazilian Portuguese',
        'name_local': 'Português Brasileiro',
    },
    RU: {
        'name': 'Russian',
        'name_local': 'Русский',
    },
    SK: {
        'name': 'Slovak',
        'name_local': 'slovensky',
    },
    SV: {
        'name': 'Swedish',
        'name_local': 'Svenska',
    },
    TR: {
        'name': 'Turkish',
        'name_local': 'Türkçe',
    },
    UK: {
        'name': 'Ukrainian',
        'name_local': 'Українська',
    },
    ZH: {
        'name': 'Chinese',
        'name_local': '汉语',
    },
}

LIST_OF_LOCALES = list(SUPPORTED_LOCALES)
LOCALE_SEPARATOR = '-'
