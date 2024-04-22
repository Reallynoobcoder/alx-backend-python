#!/usr/bin/env python3
import asyncio
from time import time
"""Function that the average time."""


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Returns average time"""
    a = time()

    asyncio.run(wait_n(n, max_delay))

    return (time() - a) / n
