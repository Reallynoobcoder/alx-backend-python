#!/usr/bin/env python3
import random
"""Function that return a task"""

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """Return task"""
    return asyncio.create_task(wait_random(max_delay))