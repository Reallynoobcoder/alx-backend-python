#!/usr/bin/env python3
"""
A coroutine called async_generator that
will loop 10 times, each time asynchronously wait 1 second.
"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Loop 10 for each second."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
