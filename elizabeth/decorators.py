def romanize(func):
    """Cyrillic letter to latin converter. Romanization of the Russian alphabet
    is the process of transliterating the Russian language from the Cyrillic script
    into the Latin alphabet.

    .. note:: At this moment it's work only for Russian (http://bit.ly/2kjTEO4),
    but in future we can add support for all slavic languages or for all Cyrillic languages.

    :param func: Function.
    :return: Latinized text.
    """

    def romanized(*args, **kwargs):
        alphabet = {
            "А": "A", "а": "a",
            "Б": "B", "б": "b",
            "В": "V", "в": "v",
            "Г": "G", "г": "g",
            "Д": "D", "д": "d",
            "Е": "E", "е": "e",
            "Ё": "YO", "ё": "yo",
            "Ж": "ZH", "ж": "zh",
            "З": "Z", "з": "z",
            "И": "I", "и": "i",
            "Й": "YE", "й": "ye",
            "К": "K", "к": "k",
            "Л": "L", "л": "l",
            "М": "M", "м": "m",
            "Н": "N", "н": "n",
            "О": "O", "о": "o",
            "П": "P", "п": "p",
            "Р": "R", "р": "r",
            "С": "S", "с": "s",
            "Т": "T", "т": "t",
            "У": "U", "у": "у",
            "Ф": "F", "ф": "f",
            "Х": "KH", "х": "kh",
            "Ц": "TS", "ц": "ts",
            "Ч": "CH", "ч": "ch",
            "Ш": "SH", "ш": "sh",
            "Щ": "SHCH", "щ": "shch",
            "Ъ": "", "ъ": "",
            "Ы": "Y", "ы": "y",
            "Ь": "", "ь": "",
            "Э": "E", "э": "e",
            "Ю": "YU", "ю": "yu",
            "Я": "JA", "я": "ja",
            'ый': 'y', 'ЫЙ': 'Y',
            'ий': 'y', 'ИЙ': 'Y',
            'ые': 'ye', 'ЫЕ': 'YE',
            ' ': ' '
        }
        result = func(*args, **kwargs)
        return ''.join([alphabet[i] for i in result if i in alphabet])

    return romanized
