"""Provides with composition tools.
"""
from functools import reduce

__all__ = [
    "composite",
]


def composite(funcs):
    """Provides with functional composition.

    :param funcs: A list of callables.
    :return: A composite function.
    """

    def compose(g, f):  # pylint: disable=invalid-name
        def h(*args, **kwargs):  # pylint: disable=invalid-name
            return g(f(*args, **kwargs), **kwargs)

        return h

    return reduce(compose, funcs)
