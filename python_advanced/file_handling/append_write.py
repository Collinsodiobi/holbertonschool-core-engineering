#!/usr/bin/env python3
"""Module that appends a string to a text file (UTF-8)"""


def append_write(filename="", text=""):
    """Appends a string to a UTF8 file and returns number of chars added"""

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
