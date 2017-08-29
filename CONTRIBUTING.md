## Guidelines

- Add one change per one commit.

- Always comment your code (only in English!).

- Check your spelling and grammar.

- Check code with [pycodestyle](https://github.com/PyCQA/pycodestyle) or with any other similar tool.

- Run the tests after each commit.

- Make sure the tests pass.

- If you add any functionality, then you should add tests for it.

- Do not write bad code!

----

When you add new locale make sure, that you:
- Add your locale to `SUPPORTED_LOCALES` in `mimesis/settings.py`.
- Add symbol of currency of your locale to `CURRENCY_SYMBOLS` in `mimesis/data/int/business.py`.
- Add number of ISBN group of your locale to `ISBN_GROUPS` in `mimesis/data/int/code.py`.
- If it's sub locale (like `en-gb`) that you inherit data from base locale and do not duplicate data from base locale.
