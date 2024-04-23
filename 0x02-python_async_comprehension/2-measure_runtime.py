#!/usr/bin/env python3
"""
Coroutine that execute async_comprehension four times in parallel.
"""
from time import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime and return it."""
    start_time = time()

    coroutines = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*coroutines)

    end_time = time()
    execution_time = end_time - start_time
    return execution_time
