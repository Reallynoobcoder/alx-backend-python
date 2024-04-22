#!/usr/bin/env python3
"""Async routine."""

from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Wait for n random delays."""
    new_list: List[float] = []

    for _ in range(n):
        if len(new_list) >= n:
            break
        delay = await wait_random(max_delay)
        new_list.append(delay)

    return sorted(new_list)
