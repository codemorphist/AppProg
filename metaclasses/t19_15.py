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


def trace_class(cls: type) -> type:
    methods = [
        method for method in dir(cls) 
        if callable(getattr(cls, method))
        and not method.startswith("__")
    ]

    for method in methods:
        func = getattr(cls, method)
        setattr(cls, method, trace(func))

    return cls 


class TraceMeta(type):
    _traced_cls = {}

    def __call__(cls, *args, **kwargs):
        try:
            TraceMeta._traced_cls[cls]
        except KeyError:
            trace_class(cls)
            TraceMeta._traced_cls[cls] = 1
        return type.__call__(cls, *args, **kwargs)


class A(metaclass=TraceMeta):
    def fac(self, n: int) -> int:
        if n <= 1: return 1
        return self.fac(n-1) + self.fac(n-2) 

    def greet(self):
        print("Hello!")


if __name__ == "__main__":
    a = A() 
    print(a.fac(5))
    a.greet()
