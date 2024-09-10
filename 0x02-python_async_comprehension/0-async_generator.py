#!/usr/bin/env python3
"""
0. Async Generator that yields 10 random numbers between 0 and 10
"""

import random
import asyncio


async def async_generator():
    """Generator that yields 10 random numbers between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
