#!/usr/bin/env python3
"""Concurrent coroutine"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return the list of delays"""
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
    return [await delay for delay in asyncio.as_completed(delays)]
