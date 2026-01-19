#!/usr/bin/env python3

import sys


MORSE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}


def encode(text: str) -> str:
    """Encode text to Morse code, using '/' for spaces."""
    tokens = []
    for ch in text.upper():
        if ch == " ":
            tokens.append("/")
        elif ch in MORSE:
            tokens.append(MORSE[ch])
        else:
            raise AssertionError("the arguments are bad")
    return " ".join(tokens)


def main() -> None:
    """Parse argument and print Morse encoding."""
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        print(encode(sys.argv[1]))
    except AssertionError as exc:
        print(f"AssertionError: {exc}")


if __name__ == "__main__":
    main()
