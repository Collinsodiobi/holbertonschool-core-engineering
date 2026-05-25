#!/usr/bin/env python3
"""Module that writes a string to a text file (UTF-8)"""


def write_file(filename="", text=""):
    """Writes a string to a UTF8 file and returns number of chars"""

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
