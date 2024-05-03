#!/usr/bin/env python3
"""Contains a func with annotated parameters"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns the list of tuples of length lst"""
    return [(i, len(i)) for i in lst]
