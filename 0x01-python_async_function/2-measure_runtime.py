#!/usr/bin/env python3
"""Function that the average time."""
from time import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Returns average time"""
    a = time()
    asyncio.run(wait_n(n, max_delay))
    return (time() - a) / n
