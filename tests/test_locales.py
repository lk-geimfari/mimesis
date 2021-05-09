from mimesis.locales import Locale


def test_locales_count():
    assert len(list(Locale)) == 34


def test_locale_in():
    assert 'ru' in Locale
    assert 'en' in Locale
