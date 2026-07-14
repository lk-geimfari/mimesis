"""Mimesis: Fake Data Generator.

Copyright (c) 2016 - Present Isaak Uchakaev (Likid Geimfari).
Website: https://mimesis.name
Email: <hey@isaak.dev>
Repository: https://github.com/lk-geimfari/mimesis
License: MIT License.
"""

from . import keys
from .builder import SchemaBuilder, SchemaRef
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
    # Enums:
    "Algorithm",
    "AudioFile",
    "BaseDataProvider",
    "BaseProvider",
    "BinaryFile",
    "CardType",
    "Choice",
    "Code",
    "CompressedFile",
    "CountryCode",
    "Cryptographic",
    "DSNType",
    "Datetime",
    "Development",
    "DocumentFile",
    "DurationUnit",
    "EANFormat",
    "EmojiCategory",
    "Field",
    "FieldArityError",
    "FieldError",
    "FieldNameError",
    "Fieldset",
    "FieldsetError",
    "File",
    "FileType",
    "Finance",
    "Food",
    "Gender",
    # Generic provider:
    "Generic",
    "Hardware",
    "IPv4Purpose",
    "ISBNFormat",
    "ImageFile",
    "Internet",
    # Locale:
    "Locale",
    # Exceptions:
    "LocaleError",
    "MeasureUnit",
    "MetricPrefixSign",
    "MimeType",
    "NonEnumerableError",
    "NumType",
    "Numeric",
    "Path",
    "Payment",
    "Person",
    "PortRange",
    "Schema",
    # Schema:
    "SchemaBuilder",
    "SchemaError",
    "SchemaRef",
    "Science",
    "TLDType",
    "Text",
    "TimestampFormat",
    "TimezoneRegion",
    "TitleType",
    "Transport",
    "URLScheme",
    "VideoFile",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    # Meta:
    "__version__",
    # Keys:
    "keys",
]

__version__ = "20.0.0"
__title__ = "mimesis"
__description__ = "Mimesis: Fake Data Generator."
__url__ = "https://github.com/lk-geimfari/mimesis"
__author__ = "Isaak Uchakaev (Likid Geimfari)"
__author_email__ = "hey@isaak.dev"
__license__ = "MIT License"
