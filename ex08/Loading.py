#!/usr/bin/env python3

import os
import sys
import time


def _fmt_mmss(seconds: float) -> str:
    """Format seconds as MM:SS."""
    mins = int(seconds) // 60
    secs = int(seconds) % 60
    return f"{mins:02d}:{secs:02d}"


def ft_tqdm(lst: range):
    """A minimal tqdm-like progress bar using yield."""
    total = len(lst)
    if total == 0:
        return

    start = time.time()
    bar_min = 10

    for i, elem in enumerate(lst, start=1):
        yield elem

        elapsed = time.time() - start
        rate = i / elapsed if elapsed > 0 else 0.0
        eta = (total - i) / rate if rate > 0 else 0.0

        percent = int(i * 100 / total)
        prefix = f"{percent:3d}%|"

        elapsed_s = _fmt_mmss(elapsed)
        eta_s = _fmt_mmss(eta)
        rate_s = f"{rate:0.2f}it/s"
        suffix = f"| {i}/{total} [{elapsed_s}<{eta_s}, {rate_s}]"

        term_width = os.get_terminal_size().columns
        available = term_width - len(prefix) - len(suffix)
        bar_len = max(bar_min, available)

        filled = int(bar_len * i / total)
        if filled >= bar_len:
            bar = "=" * (bar_len - 1) + ">"
        else:
            bar = "=" * filled + " " * (bar_len - filled)

        line = prefix + bar + suffix
        sys.stdout.write("\r" + line)
        sys.stdout.flush()

    sys.stdout.write("\n")
    sys.stdout.flush()
