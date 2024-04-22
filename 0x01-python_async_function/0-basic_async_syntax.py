#!/usr/bin/env python3
import random
import asyncio
"""
Synchronous coroutine that takes in an integer argument
max_delay, and return a random delay between 0 and max_delay.
"""


async def wait_random(max_delay: int = 10) -> float:
    """Return random delay between 0 and max_delay"""
    await asyncio.sleep(random.uniform(0, max_delay))
    return random.uniform(0, max_delay)
