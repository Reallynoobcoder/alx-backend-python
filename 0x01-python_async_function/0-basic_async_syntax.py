#!/usr/bin/env python3
import random
import asyncio
"""async coroutine"""


async def wait_random(max_delay: int = 10) -> float:
    """async function"""
    await asyncio.sleep(random.randint(0, max_delay))
    return random.uniform(0, max_delay)
