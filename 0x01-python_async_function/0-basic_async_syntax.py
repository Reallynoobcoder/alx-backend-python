#!/usr/bin/env python3
"""
Synchronous coroutine that takes in an integer argument
max_delay, and return a random delay between 0 and max_delay.
"""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """Return random delay between 0 and max_delay"""
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
