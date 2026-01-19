#!/usr/bin/env python3


def ft_filter(function, iterable):
    """
    filter(function or None, iterable) --> filter object

    Yield items from iterable for which function(item) is true.
    If function is None, yield items that are truthy.
    """
    if function is None:
        return iter([item for item in iterable if item])
    return iter([item for item in iterable if function(item)])
