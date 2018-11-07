import contextlib
from typing import Generator

from mimesis import providers
from mimesis.utils import pull

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

DataProviderType = providers.BaseDataProvider


@contextlib.contextmanager
def override(provider: DataProviderType,
             locale: str = EN) -> Generator[DataProviderType, None, None]:
    """Context manager which allows overriding current locale.

    :param provider: Locale dependent data provider.
    :param locale: Locale.
    :return:
    """
    origin_locale = getattr(provider, 'locale', None)
    datafile = getattr(provider, '_datafile', None)

    if not datafile or not locale:
        raise ValueError('«{}» has not locale dependent'.format(
            provider.__class__.__name__))

    provider.locale = locale
    provider._data = pull(datafile, locale)

    try:
        yield provider
    finally:
        provider.locale = origin_locale
        provider._data = pull(datafile, origin_locale)
