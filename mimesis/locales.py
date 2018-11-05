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


class override(object):  # noqa
    """Context manager which allows overriding current locale.

     .. note:: This feature does not works with :class:`~mimesis.Generic()`.
        Usually, you don't need data from other locales,
        when you use :class:`~mimesis.Generic()`.
    """

    def __init__(self, provider, locale: str = EN) -> None:
        """Initialize attributes.

        :param provider: Provider's instance.
        :param locale: Locale code.
        """
        self.instance = provider
        self.locale = locale
        self.origin_locale = getattr(provider, 'locale', None)
        self.datafile = getattr(self.instance, '_datafile', None)

    def __enter__(self) -> None:
        if not self.datafile or not self.locale:
            raise ValueError('«{}» has not locale dependent'.format(
                self.instance.__class__.__name__))

        self.instance.locale = self.locale
        self.instance._data = pull(self.datafile, self.locale)

    def __exit__(self, *args) -> None:
        self.instance.locale = self.origin_locale
        self.instance._data = pull(self.datafile, self.origin_locale)
