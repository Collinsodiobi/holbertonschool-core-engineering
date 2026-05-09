#!/usr/bin/env python3

def pow(a, b):
    if b == 0:
        return 1

    result = 1

    if b > 0:
        for i in range(b):
            result *= a
        return result

    # negative exponent
    for i in range(-b):
        result *= a
    return 1 / result
