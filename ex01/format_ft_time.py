#!/usr/bin/env python3

from datetime import datetime


def main() -> None:
    """Display the current time in the required formats."""
    now = datetime.now()
    timestamp = now.timestamp()

    part1 = f"Seconds since January 1, 1970: {timestamp:,.4f}"
    part2 = f" or {timestamp:.2e} in scientific notation"
    print(part1 + part2)
    print(now.strftime("%b %d %Y"))


if __name__ == "__main__":
    main()
