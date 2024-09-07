from functools import wraps


def trace(func):
    @wraps(func)
    def _func(*args, **kwargs):
        if _func.depth == -1:
            print(f"\nStart tracing {func.__name__}:")

        _func.depth += 1
        res = func(*args, **kwargs)

        ar = ", ".join(map(str, args))
        print(f"\t[depth: {_func.depth}]\t{func.__name__}({ar})\t=\t{res}")

        _func.depth -= 1
        return res

    _func.depth = -1
    return _func


@trace
def fib(n: int) -> int:
    if n <= 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


@trace
def fac(n: int) -> int:
    if n < 0:
        raise ValueError("Value of n must be greater of equal to zero")
    if n <= 1:
        return 1
    return n * fac(n-1)


if __name__ == "__main__":
    fib(3)
    fib(2)
    fac(2) 
    fac(10)

