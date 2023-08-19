"""Mimesis is a Python library, which helps generate fake data.

Copyright (c) 2016 - 2023 Isaak Uchakaev (Likid Geimfari).
Website: https://mimesis.name
Email: <likid.geimfari@gmail.com>
Repository: https://github.com/lk-geimfari/mimesis
"""

from mimesis import keys
from mimesis.enums import (
    Algorithm,
    AudioFile,
    CardType,
    CompressedFile,
    CountryCode,
    DocumentFile,
    DSNType,
    EANFormat,
    FileType,
    Gender,
    ImageFile,
    ISBNFormat,
    MeasureUnit,
    MetricPrefixSign,
    MimeType,
    NumType,
    PortRange,
    TimestampFormat,
    TimezoneRegion,
    TitleType,
    TLDType,
    URLScheme,
    VideoFile,
)
from mimesis.exceptions import (
    FieldError,
    FieldsetError,
    LocaleError,
    NonEnumerableError,
    SchemaError,
)
from mimesis.locales import Locale
from mimesis.providers import (
    Address,
    BaseDataProvider,
    BaseProvider,
    BinaryFile,
    Choice,
    Code,
    Cryptographic,
    Datetime,
    Development,
    File,
    Finance,
    Food,
    Generic,
    Hardware,
    Internet,
    Numeric,
    Path,
    Payment,
    Person,
    Science,
    Text,
    Transport,
)
from mimesis.schema import Field, Fieldset, Schema

__all__ = [
    "Address",
    "BaseDataProvider",
    "BaseProvider",
    "BinaryFile",
    "Finance",
    "Code",
    "Choice",
    "Datetime",
    "Development",
    "File",
    "Food",
    "Hardware",
    "Internet",
    "Numeric",
    "Path",
    "Payment",
    "Person",
    "Science",
    "Text",
    "Transport",
    "Cryptographic",
    # Has all:
    "Generic",
    # Keys:
    "keys",
    # Schema:
    "Field",
    "Fieldset",
    "Schema",
    # Locale:
    "Locale",
    # Enums:
    "Algorithm",
    "AudioFile",
    "CardType",
    "CompressedFile",
    "CountryCode",
    "DocumentFile",
    "DSNType",
    "EANFormat",
    "FileType",
    "Gender",
    "ImageFile",
    "ISBNFormat",
    "MeasureUnit",
    "MetricPrefixSign",
    "MimeType",
    "NumType",
    "PortRange",
    "TimezoneRegion",
    "TimestampFormat",
    "TitleType",
    "TLDType",
    "URLScheme",
    "VideoFile",
    # Exceptions:
    "LocaleError",
    "SchemaError",
    "NonEnumerableError",
    "FieldError",
    "FieldsetError",
    # Meta:
    "__version__",
    "__title__",
    "__description__",
    "__url__",
    "__author__",
    "__author_email__",
    "__license__",
]

__version__ = "11.1.0"
__title__ = "mimesis"
__description__ = "Mimesis: Fake Data Generator."
__url__ = "https://github.com/lk-geimfari/mimesis"
__author__ = "Isaak Uchakaev (Likid Geimfari)"
__author_email__ = "likid.geimfari@gmail.com"
__license__ = "MIT License"
