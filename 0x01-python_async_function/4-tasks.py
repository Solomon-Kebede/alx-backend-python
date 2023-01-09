#!/usr/bin/env python3

'''
Take the code from `wait_n` and alter it into a new
function `task_wait_n`. The code is nearly identical
to `wait_n` except  `task_wait_random` is being called.
'''


import asyncio
import random
import typing
# wait_n = __import__('1-concurrent_coroutines').wait_n
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    '''wait n number of times with a randomly
    generated delay value b/n 0 and max_delay
    (using asyncio.Task)'''
    coroutines = []
    for i in range(n):
        coroutines.append(task_wait_random(max_delay))
    result = await asyncio.gather(*coroutines)
    return sorted(result)
