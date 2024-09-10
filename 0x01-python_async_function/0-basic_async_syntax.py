#!/usr/bin/env python3
"""
Asychronous coroutine that takes an integers args(max_delay)
with a default of 10 named wait random that waits for a random
delay btw 0 and max_delay(included and float vale) seconds and
eventually returns it
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    function that return random float numbers
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
