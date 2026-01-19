#!/usr/bin/env python3

import math


def NULL_not_found(object: any) -> int:
    """Identify and print 'null-like' values, else report not found."""
    if object is None:
        print(f"Nothing: {object} {type(object)}")
        return 0

    if isinstance(object, float) and math.isnan(object):
        print(f"Cheese: {object} {type(object)}")
        return 0

    # Must check False before int-zero because bool is a subclass of int
    if object is False:
        print(f"Fake: {object} {type(object)}")
        return 0

    if isinstance(object, int) and object == 0:
        print(f"Zero: {object} {type(object)}")
        return 0

    if isinstance(object, str) and object == "":
        print(f"Empty: {type(object)}")
        return 0

    print("Type not Found")
    return 1
