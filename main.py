#!/usr/bin/env python3
"""The Router Confesses - make.fun entry.

A home Wi-Fi router's first-person confession, printed as exactly one line.
Deterministic: no randomness, no network, no clock.
"""
import os

# The confession: the router was never broken, it was getting revenge.
ENTRY = "I confess: every time the Wi-Fi 'mysteriously' died, I wasn't broken \u2014 I was just getting revenge for being unplugged in the middle of your most important meeting."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
