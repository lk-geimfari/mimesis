## Contributing Guidelines

### Development environment
Mimesis does not have any need for third-party tools, but we use a lot of tools in development stage,
which you should install on your system if you want to contribute.

We use `Pipenv` for managing development packages:
```
~ pip install pipenv
~ pipenv install --dev
```

### Code Style

Every contributor must follow the [PEP8](https://www.python.org/dev/peps/pep-0008/) code style.

### Annotating
We use optional static typing ([mypy](https://github.com/python/mypy)). Every function and method should be annotated.

Example of annotated function:

```python
def plus(a: int, b: int) -> int:
    """Get sum of a and b.

    :param a: First number.
    :param b: Second number.
    :return: Sum of a and b.
    """
    return a + b
```

### Documenting
Always add docstrings for your functions, methods, and classes:

```python
class Example(object):
    """Example class which was created to show how we
    document our classes, methods, and functions.
    """

    def foo(self) -> str:
        """This method always returns ``foo``.

        :return: String ``foo``
        """
        return 'foo'

def pi() -> float:
    """Get Pi with two digits after the decimal point.

    :return: Pi
    """
    return 3.14
```

Comment only things that are not obvious: hacks, optimizations, complex algorithms. Obvious code does not require any additional comments.

### Testing
You should write the test which shows that the bug was fixed or that the feature works as expected,
run test before you commit your changes to the branch and create PR.

To run tests, simply:
```
make test
```

Check out logs of Travis CI or AppVeyor if tests were failed on creating PR, there you can find useful information.

### Performance
It's good idea to run benchmark test, when you add your feature:

```
~ make benchmarks
```

Optimize the things which really must be optimized. There no need in using `C` or
other overheads to win 0.0000001 seconds of runtime.

### Type checking
After adding every feature you should run the type checking and make sure that everything is okay. You can do it using make:

```
~ make type-checking
```

### Code Review
Contributions will not be merged until they've been code reviewed by one of our reviewers.
In the event that you object to the code review feedback, you should make your case clearly and calmly.
If, after doing so, the feedback is judged to still apply, you must either apply the feedback
or withdraw your contribution.

### Questions
The GitHub issue tracker is for bug reports and feature requests.
Please do not create issue which does not related to features or bug reports.

### New Locale
We have created a directory with a real structure which you can use as great example `mimesis/data/locale_template` if you want to add a new locale.

### Releases
We use `Travis CI` for automatically creating releases.
The package will be published on PyPi after pushing the new `tag` to the master branch.
The new release can be approved or disapproved by maintainers of this project. If the new release was disapproved, then maintainer should justify why the new release cannot be created.

### Summary
- Add one change per one commit.
- Always comment your code (only in English!).
- Check your spelling and grammar.
- Run the tests after each commit.
- Make sure the tests pass.
- Make sure that type check is passed.
- If you add any functionality, then you should add tests for it.
- Annotate your code.
- Do not write bad code!
