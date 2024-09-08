#!/usr/bin/env python3
"""
duck_typing : more involved type annotations
"""
from typing import Union, Any, Sequence


def safely_get_value(dct: dict, key: Any, default: Union[Any, None]=None) -> Union[Any, None]:
    """
    Annotate function parameters
    """
    if key in dct:
        return dct[key]
    else:
        return default
