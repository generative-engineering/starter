Fabric Function Starter
========================


Setup and Use
-------------
- Follow the Setup guide in [our docs](https://docs.generative.vision/) to install everything you need
- Create a copy of the contents of this repository to a location where you want to develop your fabric functions
- Install the relevant python packages which can be done by running `poetry install`
- Create and use your new Fabric Functions following the Concepts guide in [our docs](https://docs.generative.vision/)

### Testing
Testing your fabric function can be a useful way of debugging.
Python comes with the [pytest framework](https://docs.pytest.org/en/stable/) for testing.
There's a simple existing test in the ['tests' directory](/tests).
Add your own tests as you like.

To run all tests in this directory, run:
```shell
poetry run pytest
```

### Linting
If you're typing your functions,
[mypy](https://mypy.readthedocs.io/en/stable/) is useful for checking for any errors before running.
To run mypy:
```shell
poetry run mypy
```
