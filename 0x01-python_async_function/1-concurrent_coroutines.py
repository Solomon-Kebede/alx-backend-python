#!/usr/bin/env python3

'''
Import `wait_random` from the previous python file that you’ve
written and write an async routine called `wait_n` that takes in
2 int arguments (in this order): `n` and `max_delay`. You will
spawn `wait_random` `n` times with the specified `max_delay`.

`wait_n` should return the list of all the delays (float values).
The list of the delays should be in ascending order without
using `sort()` because of concurrency.
'''


import asyncio
import random
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    '''wait n number of times with a randomly
    generated delay value b/n 0 and max_delay'''
    coroutines = []
    for i in range(n):
        coroutines.append(wait_random(max_delay))
    result = await asyncio.gather(*coroutines)
    return sorted(result)
