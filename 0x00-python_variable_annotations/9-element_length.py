#!/usr/bin/env python3
"""
ducky_typing: Annotate function parameters
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Annotate function parameters
    """
    return [(i, len(i)) for i in lst]
