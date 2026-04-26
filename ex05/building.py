#!/usr/bin/env python3

import string
import sys


def analyze_text(text: str) -> dict[str, int]:
    """Count upper/lower/punct/spaces/digits in text."""
    counts = {"upper": 0, "lower": 0, "punct": 0, "space": 0, "digit": 0}

    for ch in text:
        if ch.isupper():
            counts["upper"] += 1
        elif ch.islower():
            counts["lower"] += 1
        elif ch in string.punctuation:
            counts["punct"] += 1
        elif ch.isdigit():
            counts["digit"] += 1
        elif ch.isspace():
            counts["space"] += 1

    return counts


def main() -> None:
    """Standalone program: count character categories."""
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"

        if len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            print("What is the text to count?")
            text = sys.stdin.read()

        counts = analyze_text(text)
        print(f"The text contains {len(text)} characters:")
        print(f"{counts['upper']} upper letters")
        print(f"{counts['lower']} lower letters")
        print(f"{counts['punct']} punctuation marks")
        print(f"{counts['space']} spaces")
        print(f"{counts['digit']} digits")
    except AssertionError as exc:
        print(f"AssertionError: {exc}")


if __name__ == "__main__":
    main()
