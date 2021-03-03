import dask
from innerscope import scoped_function


def task(func):
    sf = scoped_function(func)
    if not sf.missing:
        return (func,)
    deps = tuple(sf.missing)
    return ((lambda *args: sf.bind(**dict(zip(deps, args)))().return_value),) + deps


class Tube:
    """ Create a pipeline of functions to be executed with dask."""

    def __init__(self, *args, **kwargs):
        self.parameters = set(args)
        self.dsk = {}
        for key, val in kwargs.items():
            if callable(val):
                self.dsk[key] = task(val)
            else:
                raise TypeError(f"Bad type for keyword {key!r}: {type(val)}")

    def __call__(self, **kwargs):
        """Execute the pipeline with given input parameters"""
        missing = set(kwargs) - self.parameters
        if missing:
            raise TypeError("Missing keyword arguments:", ", ".join(sorted(missing)))
        kwargs.update(self.dsk)
        keys = list(kwargs)
        vals = dask.get(kwargs, keys)
        return dict(zip(keys, vals))
