#!/usr/bin/env python3


def ft_filter(function, iterable):
    """
    filter(function or None, iterable) --> filter object

    Returns an iterator yielding those items of iterable for which function
    returns true. If function is None, returns the items that are true.
    """
    if function is None:
        return iter([item for item in iterable if item])
    return iter([item for item in iterable if function(item)])
