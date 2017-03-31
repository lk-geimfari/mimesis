## Guidelines

- Add one change per one commit.

- Always comment your code (only in English!).

- Check your spelling and grammar.

- Check code with [pycodestyle](https://github.com/PyCQA/pycodestyle) or with any other similar tool.

- Run the tests after each commit.

- Make sure the tests pass.

- If you add any functionality, then you should add tests for it.

- Do not write bad code.

----

When you add new locale make sure, that you added following data:
- [Conftest](https://github.com/lk-geimfari/elizabeth/blob/master/tests/conftest.py#L4)
- [SUPPORTED_LOCALES](https://github.com/lk-geimfari/elizabeth/blob/master/elizabeth/settings.py#L4)
- [CURRENCY_SYMBOLS](https://github.com/lk-geimfari/elizabeth/blob/master/elizabeth/intd/bus.py#L183)
- [ISBN_GROUPS](https://github.com/lk-geimfari/elizabeth/blob/master/elizabeth/intd/code.py#L33)
