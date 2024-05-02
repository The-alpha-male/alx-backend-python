#!/usr/bin/env python3

"""type-annotated function that takes a float
as an arg and returns the string representation"""

__annotations__ = ["n": int, "return": str]


def to_str(n: float) -> str:
    """Convert number to a string"""
    return str(n)
