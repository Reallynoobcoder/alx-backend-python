#!/usr/bin/env python3
"""Update wait_n to task_wait_n"""
import random
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Wait for n random delays."""
    new_list: List[float] = []

    for _ in range(n):
        if len(new_list) >= n:
            break
        delay = await task_wait_random(max_delay)
        new_list.append(delay)

    return sorted(new_list)
