# Innertube

[![Python Version](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%20PyPy-blue)](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%20PyPy-blue)
[![Version](https://img.shields.io/pypi/v/innertube.svg)](https://pypi.org/project/innertube/)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://github.com/eriknw/innertube/blob/master/LICENSE)
[![Build Status](https://travis-ci.org/eriknw/innertube.svg?branch=master)](https://travis-ci.org/eriknw/innertube)
[![Coverage Status](https://coveralls.io/repos/eriknw/innertube/badge.svg?branch=master)](https://coveralls.io/r/eriknw/innertube)
[![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

`innertube` provides a way to construct reusable, parameterized pipelines to be executed with `dask`.

For example:
```python
from innertube import Tube

tube = Tube(
    'a',
    b=lambda: a + 1,
    c=lambda: a + b,
)
assert tube(a=1) == {'a': 1, 'b': 2, 'c': 3}
```
Much more has been designed and is currently in the process of being implemented.  Stay tuned, and thanks for your patience!

**To install:** `pip install innertube`
