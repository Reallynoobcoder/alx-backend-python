#!/usr/bin/env python3
"""Coroutine that collect 10 random numbers."""


import asyncio
import random
from typing import List


async def async_comprehension() -> List[float]:
    """Return 10 random numbers."""
    return [i async for i in async_generator()]
