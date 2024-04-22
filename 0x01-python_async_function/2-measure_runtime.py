#!/usr/bin/env python3
import asyncio
from time import time
"""Function that the average time."""


def measure_time(n: int, max_delay: int) -> float:
    """Returns average time"""
    a = time()

    asyncio.run(wait_n(n, max_delay))

    return (time() - a) / n
