# Why did I make this?

The goal of this example is to showcase the different tooling that are typical in local software development, while providing an implementation suited for local python development.

# The example

The code is pretty straightforward. `./development_example/my_functions` contains a function that we do parameterized testing against in `./test/test_my_functions.py`.

## local setup

Follow the installation instructions for:

1. [chocolatey](https://chocolatey.org/install#individual) - windows package manager
2. [python3.10 interpreter via chocolatey](https://community.chocolatey.org/packages/python310)
3. [python3.11 interpreter via chocolatey](https://community.chocolatey.org/packages/python311)
4. [python3.12 interpreter via chocolatey](https://community.chocolatey.org/packages/python312)
5. [GNU make via chocolatey](https://community.chocolatey.org/packages/make)
5. [scoop](https://scoop.sh/) - windows package manager (this is the only windows package manager that has pipx for whatever reason)
6. [pipx](https://pipx.pypa.io/stable/installation/#on-windows) - an "improved" python package manager
7. [poetry](https://python-poetry.org/docs/#installing-with-pipx) - dependency management tool

### If you use the git bash terminal for Windows

The bash shell probably won't know where to find any of the tooling when you invoke them in the terminal.

In that case, create a file named `.profile` in your home directory - i.e. `~/.profile` - and put the following code in there. Make sure to put your actual user directory name in the last command.

```
export PATH=$PATH:/c/Python312
export PATH=$PATH:/c/Python312/Scripts
export PATH=$PATH:/c/Python311
export PATH=$PATH:/c/Python311/Scripts
export PATH=$PATH:/c/Python310
export PATH=$PATH:/c/Python310/Scripts
export PATH=$PATH:/c/users/YOUR_USERNAME_DIR/.local/bin
```

You'll need to restart your pc before it takes effect, but if you don't want to restart your pc, then execute each line individually in your terminal.

After that, you should be able to use the tooling.

## local usage

After local setup is completed, this sections shows what you can do.

### Executing tests

To run all tests, execute `make test`. This executes `tox` via `poetry` to execute all tests against the python3.10, 3.11, and 3.12 interpreters. Code coverage results are generated during these tests.

### Code coverage

To view code coverage results directly in your terminal, execute `make cov`.

#### XML code coverage report generation

To create a code coverage report in XML, execute `make cov-xml`. This is useful when your IDE or text editing tooling needs a code coverage report in xml to be able to display results directly in your IDE or text editing tooling.

# Local software development tooling

There are a lot of tools that exist specifically tailored to improving the development experience, which is especially true in the python community. If you've ever needed to deploy anything built with python - like a bot, website, or any web API - you'll have quickly noticed that it quickly becomes devops hell without any local software development tooling.

For this example implementation, I chose tools that, from their github profiles, look relatively well-maintained and appear to be well-adopted by the python community. FYI, Python isn't the language I typically use to build projects, so I probably won't know about other tooling options.

## Dependency management tooling

When doing any kind of software development, we need to be able to effectively manage:

1. the direct dependencies of our software
2. the indirect dependencies of our software (i.e. the dependencies of our dependencies)

Managing these dependencies includes things such as:

- adding new dependencies at either specific versions or the latest version
- updating existing dependencies to specific versions or the latest version
- removing dependencies
- adding and updating dependencies only meant for testing purposes

We need this kind of tooling because it simplifies managing our dependencies.

For dependency management in this example, I chose [poetry](https://github.com/python-poetry/poetry) because it seems relatively simple to use, it doesn't seem very opinionated on how it thinks people should do development, it does everything that I think I need, and everything is controlled by a single config file.

## Test tooling

To engineer software, it's a requirement that the software be tested against some criteria. Test tooling simplifies the code needed to write tests and saves you from creating your own test tooling, which would then require you to test your own tooling, which takes a fair amount of time to do.

With test tooling, you can more quickly build tests in your codebase and then execute all of the tests with the test runner that comes with the tooling.

For test tooling, I chose the following tools for the following reasons:

- [pytest](https://github.com/pytest-dev/pytest): test writing and execution
- [tox](https://github.com/tox-dev/tox): test automation
- [coverage](https://github.com/nedbat/coveragepy): code coverage

This test tooling stack has everything that I think I need:

- simplifying building tests
- executing our tests with multiple python interpreters to easily scale tests across interpreter versions
- showing me which lines are being missed by the test suite

### Code coverage

The test tooling that we use should be able to produce code coverage results so that we can analyze those results based on our own opinions regarding the code coverage of whatever we're developing.
