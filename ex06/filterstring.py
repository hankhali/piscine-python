#!/usr/bin/env python3

import sys

from ft_filter import ft_filter


def is_int_string(s: str) -> bool:
    """True if s is an integer string, optional leading + or -."""
    if s.startswith(("+", "-")):
        return len(s) > 1 and s[1:].isdigit()
    return s.isdigit()


def main() -> None:
    """Print words longer than N from a space-separated string."""
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        s = sys.argv[1]
        n_str = sys.argv[2]
        if not is_int_string(n_str):
            raise AssertionError("the arguments are bad")

        n = int(n_str)
        words = s.split(" ")
        result = list(ft_filter(lambda w: len(w) > n, words))
        print(result)
    except AssertionError as exc:
        print(f"AssertionError: {exc}")


if __name__ == "__main__":
    main()
