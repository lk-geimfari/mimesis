from elizabeth.core.intd import ROMANIZATION_ALPHABETS


def romanized_russian(func):
    """Cyrillic letter to latin converter. Romanization of the Russian alphabet
    is the process of transliterating the Russian language from the Cyrillic script
    into the Latin alphabet.

    .. note:: At this moment it's work only for Russian (http://bit.ly/2kjTEO4),
    but in future we can add support for all slavic languages or for all Cyrillic languages.

    :param func: Function.
    :return: Latinized text.
    """
    alphabet = ROMANIZATION_ALPHABETS['ru']

    def romanized(*args, **kwargs):
        result = func(*args, **kwargs)
        return ''.join([alphabet[i] for i in result if i in alphabet])

    return romanized
