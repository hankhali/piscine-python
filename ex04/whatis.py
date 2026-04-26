#!/usr/bin/env python3

import sys


def is_integer_string(s: str) -> bool:
    """True if s is an integer string (optional leading + or -)."""
    if s.startswith(("+", "-")):
        return len(s) > 1 and s[1:].isdigit()
    return s.isdigit()


def main() -> None:
    """Print whether the given integer is even or odd."""
    try:
        if len(sys.argv) == 1:
            return
        assert len(sys.argv) == 2, "more than one argument is provided"

        arg = sys.argv[1]
        assert is_integer_string(arg), "argument is not an integer"

        n = int(arg)
        if n % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except AssertionError as exc:
        print(f"AssertionError: {exc}")


if __name__ == "__main__":
    main()
