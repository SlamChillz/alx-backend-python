#!/usr/bin/env python3
"""
Defines runtime of an asynchronous function
"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Takes two integers and returns the time it takes
    for the function to execute
    Args:
        int (int)
        max_delay (int)
    Returns:
        float
    """
    start: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end: float = time.time()
    return (end - start)
