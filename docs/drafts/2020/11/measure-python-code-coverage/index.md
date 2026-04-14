---
title: Measure Python Code Coverage
created: 2020-11-07 22:07:11
date: 2026-04-13 23:15:10.891656
authors:
  - bendu
label: measure-python-code-coverage
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Python
  - code coverage
  - coverage
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Measure Python Code Coverage using `coverage.py`

pip3 install coverage

poetry run coverage run -m pytest

poetry run coverage report -m

poetry run coverage html

## PyTest

$ pip install pytest-cov
$ py.test --cov-report=xml --cov=myproj tests/

## Tools

coverage

[CodeCov](https://github.com/codecov/codecov-python)

https://coveralls.io/

https://github.com/aconrad/pycobertura

## References

[Beginner’s guide to using Codecov with Python and Travis CI](https://medium.com/datadriveninvestor/beginners-guide-to-using-codecov-with-python-and-travis-ci-c17659bb711)

[CodeCov](https://codecov.io/gh)
