#!/usr/bin/env python3

'''
Given the parameters and the return values, add
type annotations to the function
*Hint: look into TypeVar*
'''


import typing
from typing import TypeVar, Optional
T = TypeVar('T')


def safely_get_value(
        dct: typing.Mapping,
        key: typing.Any,
        default: typing.Union[Optional[T], None] = None
        ) -> typing.Union[typing.Any, Optional[T]]:
    '''Safely retrieve value from dict
    using key'''
    if key in dct:
        return dct[key]
    else:
        return default