# -*- coding: utf-8 -*-

"""This module provides constants for locale-dependent providers."""

from typing import Iterator, List

__all__ = ["Locale"]


class _Locale:
    """This class provides access to the supported locales from one place.

    You should not use this class directly, use ``mimesis.locales.Locale`` instead.
    """

    def __init__(self) -> None:
        """Initialize all the locales.
        """
        self.CS = "cs"
        self.DA = "da"
        self.DE = "de"
        self.DE_AT = "de-at"
        self.DE_CH = "de-ch"
        self.EL = "el"
        self.EN = "en"
        self.EN_AU = "en-au"
        self.EN_CA = "en-ca"
        self.EN_GB = "en-gb"
        self.ES = "es"
        self.ES_MX = "es-mx"
        self.ET = "et"
        self.FA = "fa"
        self.FI = "fi"
        self.FR = "fr"
        self.HU = "hu"
        self.IS = "is"
        self.IT = "it"
        self.JA = "ja"
        self.KK = "kk"
        self.KO = "ko"
        self.NL = "nl"
        self.NL_BE = "nl-be"
        self.NO = "no"
        self.PL = "pl"
        self.PT = "pt"
        self.PT_BR = "pt-br"
        self.RU = "ru"
        self.SK = "sk"
        self.SV = "sv"
        self.TR = "tr"
        self.UK = "uk"
        self.ZH = "zh"
        self.DEFAULT = self.EN

    def _get_all(self) -> List[str]:
        values = set()

        for name, code in self.__dict__.items():
            if name.isupper():
                values.add(code)

        return list(values)

    def __contains__(self, item: str) -> bool:
        return item in self._get_all()

    def __iter__(self) -> Iterator[str]:
        for item in self._get_all():
            yield item


Locale = _Locale()
