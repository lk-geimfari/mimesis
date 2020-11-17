IP_V6_REGEX = r'(([0-9a-fA-F]{1,4}:)' \
              r'{7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:)' \
              r'{1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]' \
              r'{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4})' \
              r'{1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}' \
              r'|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|' \
              r'([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|' \
              r'[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|' \
              r':((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]' \
              r'{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:)' \
              r'{0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.)' \
              r'{3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|' \
              r'([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|' \
              r'1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|' \
              r'(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))'

MAC_ADDRESS_REGEX = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'

IP_V4_REGEX = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'

EMAIL_REGEX = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'

CREDIT_CARD_REGEX = r'[\d]+((-|\s)?[\d]+)+'

PROVIDER_STR_REGEX = r'^(Business|Clothing|Code|Development' \
                     r'|File|Games|Hardware|Internet|Numbers|Path|Payment|' \
                     r'Structure|Transport|UnitSystem|Cryptographic)'

DATA_PROVIDER_STR_REGEX = r'^(Address|Business|Datetime|Food|' \
                          r'Person|Science|Text|Generic|' \
                          r'BaseDataProvider|AbstractField) <([a-z-]+)>$'

_EN_GB_POST_CODE = \
    r'((([A-PR-UWYZ][0-9])|([A-PR-UWYZ][0-9][0-9])' \
    r'|([A-PR-UWYZ][A-HK-Y][0-9])|([A-PR-UWYZ][A-HK-Y][0-9][0-9])|' \
    r'([A-PR-UWYZ][0-9][A-HJKSTUW])|([A-PR-UWYZ][A-HK-Y][0-9]' \
    r'[ABEHMNPRVWXY]))) ' \
    r'|| ((GIR)[ ]?(0AA))|(([A-PR-UWYZ][0-9])[ ]?([0-9]' \
    r'[ABD-HJLNPQ-UW-Z]{0,2}))' \
    r'|(([A-PR-UWYZ][0-9][0-9])[ ]?([0-9][ABD-HJLNPQ-UW-Z]{0,2}))' \
    r'|(([A-PR-UWYZ]' \
    r'[A-HK-Y0-9][0-9])[ ]?([0-9][ABD-HJLNPQ-UW-Z]{0,2}))' \
    r'|(([A-PR-UWYZ][A-HK-Y0-9]' \
    r'[0-9][0-9])[ ]?([0-9][ABD-HJLNPQ-UW-Z]{0,2}))' \
    r'|(([A-PR-UWYZ][0-9][A-HJKS-UW0-9])' \
    r'[ ]?([0-9][ABD-HJLNPQ-UW-Z]{0,2}))' \
    r'|(([A-PR-UWYZ][A-HK-Y0-9][0-9][ABEHMNPRVWXY0-9])' \
    r'[ ]?([0-9][ABD-HJLNPQ-UW-Z]{0,2}))'

POSTAL_CODE_REGEX = {
    'ru': r'[0-9]{6}$',
    'is': r'[0-9]{3}$',
    'nl': r'^[1-9][0-9]{3}\s?[a-zA-Z]{2}$',
    'nl-be': r'[0-9]{4}$',
    'pl': r'\d{2}-\d{3}',
    'pt': r'[0-9]{4}$',
    'no': r'[0-9]{4}$',
    'da': r'DK-[0-9]{4}$',
    'de-at': r'[0-9]{4}$',
    'de-ch': r'[0-9]{4}$',
    'en-ca': r'^(\d{5}|[A-Z]\d[A-Z] ?\d[A-Z]\d)$',
    'en-au': r'[0-9]{4}$',
    'en-gb': _EN_GB_POST_CODE,
    'et': r'[0-9]{5}$',
    'fa': r'\d{5}-\d{5}',
    'el': r'[0-9]{5}$',
    'hu': r'[0-9]{4}$',
    'cs': r'\d{3}[ ]?\d{2}',
    'sk': r'\d{3}[ ]?\d{2}',
    'sv': r'^(s-|S-){0,1}[0-9]{3}\s?[0-9]{2}$',
    'ja': r'[0-9]{3}-[0-9]{4}$',
    'pt-br': r'[0-9]{5}-[0-9]{3}$',
    'zh': r'[0-9]{6}$',
    'uk': r'[0-9]{6}$',
    'kk': r'[0-9]{6}$',
    'default': r'[0-9]{5}$',
}

STOCK_IMAGE = r'http[s]?://.*/\d+x\d+\?.*$'

HOME_PAGE = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$_@.&+-]' \
            r'|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

UUID_REGEX = r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'

HEX_COLOR = r'#(?:[a-fA-F0-9]{3}|[a-fA-F0-9]{6})\b'
