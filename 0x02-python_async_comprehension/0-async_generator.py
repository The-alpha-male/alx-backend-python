#!/usr/bin/env python3
"""Asynchronous generator function"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Asynchronous generator function"""
    for count in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
