#!/usr/bin/env python3
"""
Defines a basic asynchronous routine
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    An asynchronous coroutine that waits for a random delay
    between 0 and max_delay (included and float value) seconds
    Args:
        max_delay (int): nteger argument with a default value of 10
    Return:
        (int or float): the random delay time
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
