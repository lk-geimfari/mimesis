"""Mimesis: Fake Data Generator.

Copyright (c) 2016 - Present Isaak Uchakaev (Likid Geimfari).
Website: https://mimesis.name
Email: <hey@isaak.dev>
Repository: https://github.com/lk-geimfari/mimesis
License: MIT License.
"""

from . import keys
from .enums import (
    Algorithm,
    AudioFile,
    CardType,
    CompressedFile,
    CountryCode,
    DocumentFile,
    DSNType,
    DurationUnit,
    EANFormat,
    EmojiCategory,
    FileType,
    Gender,
    ImageFile,
    IPv4Purpose,
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
from .exceptions import (
    FieldArityError,
    FieldError,
    FieldNameError,
    FieldsetError,
    LocaleError,
    NonEnumerableError,
    SchemaError,
)
from .locales import Locale
from .providers import (
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
from .schema import Field, Fieldset, Schema

__all__ = [
    # Providers:
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
    # Generic provider:
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
    "DurationUnit",
    "CompressedFile",
    "CountryCode",
    "DocumentFile",
    "DSNType",
    "EANFormat",
    "FileType",
    "Gender",
    "ImageFile",
    "ISBNFormat",
    "IPv4Purpose",
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
    "EmojiCategory",
    # Exceptions:
    "LocaleError",
    "SchemaError",
    "NonEnumerableError",
    "FieldError",
    "FieldsetError",
    "FieldArityError",
    "FieldNameError",
    # Meta:
    "__version__",
    "__title__",
    "__description__",
    "__url__",
    "__author__",
    "__author_email__",
    "__license__",
]

__version__ = "19.0.0"
__title__ = "mimesis"
__description__ = "Mimesis: Fake Data Generator."
__url__ = "https://github.com/lk-geimfari/mimesis"
__author__ = "Isaak Uchakaev (Likid Geimfari)"
__author_email__ = "hey@isaak.dev"
__license__ = "MIT License"
