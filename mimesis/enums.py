"""Implements enums for a lot of methods.

Enums from this module are used in a lot of methods.
You should always import enums from this module if you want
behavior for the methods that differ from the default behavior.

You should never use your own enums in methods because in this case,
there no guarantee that you will get the result which you actually expected.

Below you can see an example of usage enums in methods of data providers.
"""

import typing as t
from enum import Enum


class Locale(Enum):
    """This class provides access to the supported locales from one place.

    An argument for all locale-depend providers.
    """

    CS = "cs"
    DA = "da"
    DE = "de"
    DE_AT = "de-at"
    DE_CH = "de-ch"
    EL = "el"
    EN = "en"
    EN_AU = "en-au"
    EN_CA = "en-ca"
    EN_GB = "en-gb"
    ES = "es"
    ES_MX = "es-mx"
    ET = "et"
    FA = "fa"
    FI = "fi"
    FR = "fr"
    HU = "hu"
    IS = "is"
    IT = "it"
    JA = "ja"
    KK = "kk"
    KO = "ko"
    NL = "nl"
    NL_BE = "nl-be"
    NO = "no"
    PL = "pl"
    PT = "pt"
    PT_BR = "pt-br"
    RU = "ru"
    SK = "sk"
    SV = "sv"
    TR = "tr"
    UK = "uk"
    ZH = "zh"
    DEFAULT = EN

    @classmethod
    def values(cls) -> t.List[str]:
        return [i.value for i in cls.__members__.values()]


class PortRange(Enum):
    """Represents port ranges.

    An argument for :meth:`~mimesis.Internet.port()`.
    """

    ALL = (1, 65535)
    WELL_KNOWN = (1, 1023)
    EPHEMERAL = (49152, 65535)
    REGISTERED = (1024, 49151)


class Gender(Enum):
    """Represents genders.

    An argument for a lot of methods which are taking parameter ``gender``.
    """

    MALE = "male"
    FEMALE = "female"


class TitleType(Enum):
    """Represents title types.

    An argument for :meth:`~mimesis.Person.title()`.
    """

    TYPICAL = "typical"
    ACADEMIC = "academic"


class CardType(Enum):
    """Provides credit card types.

    An argument for :meth:`~mimesis.Payment.credit_card_number()`.
    """

    VISA = "Visa"
    MASTER_CARD = "MasterCard"
    AMERICAN_EXPRESS = "American Express"


class Algorithm(Enum):
    """Provides algorithms which available.

    An argument for :meth:`~mimesis.Cryptographic.hash()`.
    """

    MD5 = "md5"
    SHA1 = "sha1"
    SHA224 = "sha224"
    SHA256 = "sha256"
    SHA384 = "sha384"
    SHA512 = "sha512"
    BLAKE2B = "blake2b"
    BLAKE2S = "blake2s"


class TLDType(Enum):
    """Provides top level domain types.

    An argument for a few methods which are taking parameter **tld_type**.
    """

    CCTLD = "cctld"
    GTLD = "gtld"
    GEOTLD = "geotld"
    UTLD = "utld"
    STLD = "stld"


class FileType(Enum):
    """Provides file types.

    An argument for :meth:`~mimesis.File.extension()` and :meth:`~mimesis.File.file_name()`.
    """

    SOURCE = "source"
    TEXT = "text"
    DATA = "data"
    AUDIO = "audio"
    VIDEO = "video"
    IMAGE = "image"
    EXECUTABLE = "executable"
    COMPRESSED = "compressed"


class MimeType(Enum):
    """Provides common mime types.

    An argument for :meth:`~mimesis.File.mime_type()`.
    """

    APPLICATION = "application"
    AUDIO = "audio"
    IMAGE = "image"
    MESSAGE = "message"
    TEXT = "text"
    VIDEO = "video"


class MetricPrefixSign(Enum):
    """Provides prefix signs.

    An argument for :meth:`~mimesis.Science.metric_prefix()``.
    """

    POSITIVE = "positive"
    NEGATIVE = "negative"


class CountryCode(Enum):
    """Provides types of country codes.

    An argument for :meth:`~mimesis.Address.country_code()`.
    """

    A2 = "a2"
    A3 = "a3"
    NUMERIC = "numeric"
    IOC = "ioc"
    FIFA = "fifa"


class ISBNFormat(Enum):
    """Provides formats of ISBN.

    An argument for :meth:`~mimesis.Code.isbn()`.
    """

    ISBN13 = "isbn-13"
    ISBN10 = "isbn-10"


class EANFormat(Enum):
    """Provides formats of EAN.

    An argument for :meth:`~mimesis.Code.ean()`.
    """

    EAN8 = "ean-8"
    EAN13 = "ean-13"


class MeasureUnit(Enum):
    """Provide unit names.

    An argument for :meth:`~mimesis.Science.measure_unit()`.
    """

    MASS = ("gram", "gr")
    INFORMATION = ("byte", "b")
    THERMODYNAMIC_TEMPERATURE = ("kelvin", "K")
    AMOUNT_OF_SUBSTANCE = ("mole", "mol")
    ANGLE = ("radian", "r")
    SOLID_ANGLE = ("steradian", "㏛")
    FREQUENCY = ("hertz", "Hz")
    FORCE = ("newton", "N")
    PRESSURE = ("pascal", "P")
    ENERGY = ("joule", "J")
    POWER = ("watt", "W")
    FLUX = ("watt", "W")
    ELECTRIC_CHARGE = ("coulomb", "C")
    VOLTAGE = ("volt", "V")
    ELECTRIC_CAPACITANCE = ("farad", "F")
    ELECTRIC_RESISTANCE = ("ohm", "Ω")
    ELECTRICAL_CONDUCTANCE = ("siemens", "S")
    MAGNETIC_FLUX = ("weber", "Wb")
    MAGNETIC_FLUX_DENSITY = ("tesla", "T")
    INDUCTANCE = ("henry", "H")
    TEMPERATURE = ("Celsius", "°C")
    RADIOACTIVITY = ("becquerel", "Bq")


class NumType(Enum):
    """Provides the number types.

    An argument for :meth:`~mimesis.Numeric.matrix()`.
    """

    FLOAT = "floats"
    INTEGER = "integers"
    COMPLEX = "complexes"
    DECIMAL = "decimals"


class VideoFile(Enum):
    """Provides the vide file types.

    An argument for :meth:`~mimesis.BinaryFile.video()`
    """

    MP4 = "mp4"
    MOV = "mov"


class AudioFile(Enum):
    """Provides the audio file types.

    An argument for :meth:`~mimesis.BinaryFile.audio()`
    """

    MP3 = "mp3"
    AAC = "aac"


class ImageFile(Enum):
    """Provides the image file types.

    An argument for :meth:`~mimesis.BinaryFile.image()`
    """

    JPG = "jpg"
    PNG = "png"
    GIF = "gif"


class DocumentFile(Enum):
    """Provides the document file types.

    An argument for :meth:`~mimesis.BinaryFile.document()`
    """

    PDF = "pdf"
    DOCX = "docx"
    PPTX = "pptx"
    XLSX = "xlsx"


class CompressedFile(Enum):
    """Provides the compressed file types.

    An argument for :meth:`~mimesis.BinaryFile.compressed()`
    """

    ZIP = "zip"
    GZIP = "gz"


class URLScheme(Enum):
    """Provides URL schemes.

    An argument for some methods of :class:`~mimesis.Internet()`.
    """

    WS = "ws"
    WSS = "wss"
    FTP = "ftp"
    SFTP = "sftp"
    HTTP = "http"
    HTTPS = "https"


class TimezoneRegion(Enum):
    """Provides regions of timezones.

    An argument for :meth:`~mimesis.Datetime.timezone()`.
    """

    AFRICA = "Africa"
    AMERICA = "America"
    ANTARCTICA = "Antarctica"
    ARCTIC = "Arctic"
    ASIA = "Asia"
    ATLANTIC = "Atlantic"
    AUSTRALIA = "Australia"
    EUROPE = "Europe"
    INDIAN = "Indian"
    PACIFIC = "Pacific"


class DSNType(Enum):
    POSTGRES = ("postgres", 5432)
    MYSQL = ("mysql", 3306)
    MONGODB = ("mongodb", 27017)
    REDIS = ("redis", 6379)
    COUCHBASE = ("couchbase", 8092)
    MEMCACHED = ("memcached", 11211)
    RABBITMQ = ("rabbitmq", 5672)
