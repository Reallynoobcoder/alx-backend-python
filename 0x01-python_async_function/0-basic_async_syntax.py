#!/usr/bin/env python3
from random import uniform, randint
import asyncio
"""
Synchronous coroutine that takes in an integer argument
max_delay, and return a random delay between 0 and max_delay.
"""


async def wait_random(max_delay: int = 10) -> float:
    """Return random delay between 0 and max_delay"""
    await asyncio.sleep(uniform(0, max_delay))
    return uniform(0, max_delay)
