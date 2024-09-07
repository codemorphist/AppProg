from typing import Callable, Any
from functools import wraps


def to_range(a: int | float, b: int | float): 
    """
    This decorator casts the value of 
    the function to the range [a, b],
    dynamicaly update max and min value 
    that was already returned

    :param a: int  
    :param b: int
    """
    def _decorator(func: Callable[[Any], int | float]):
        nonlocal a, b

        if "return" in func.__annotations__:
            ann = func.__annotations__["return"]
            if ann is not int and ann is not float:
                raise TypeError("Return type of function must be int of float")

        if a == 0 and b == 0:
            raise ValueError("Values a or b must be greater than zero")

        if a >= b: 
            a, b = b, a

        mx: int | float = b # max value
        mn: int | float = a # min value

        @wraps(func)
        def _func(*args, **kwargs):
            nonlocal mx, mn, a, b

            res = func(*args, **kwargs)

            if not isinstance(res, (int, float)):
                raise TypeError(f"Invalid type of return value: {type(res)}")
            
            if res > mx:
                mx = res
            elif res < mn:
                mn = res

            return res / (mx - mn) * (b - a)

        return _func
    return _decorator


@to_range(0, 1)
def func(x: int) -> int:
    return x * 2


if __name__ == "__main__":
    print(func(4))
    print(func(5))
    print(func(4))
    print(func(3))
    print(func(5))
    print(func(1))

