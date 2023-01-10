#!/usr/bin/env python3
"""
Defines concurrent execution function
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute multiple coroutines at the same time with async
    Args:
        n (int): number of times to spawn wait_random
        max_delay (int): delay value to be passed to wait_random
    Returns:
        List[float]: list of ordered delays
    """
    resolves = await asyncio.gather(
        *(task_wait_random(max_delay) for i in range(n)))
    return sorted(resolves)
