#!/usr/bin/env python3
"""
Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make_multiplier: takes a float multiplier as argument
    """
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
