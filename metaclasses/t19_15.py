from t19_6 import trace_class

class TraceMeta(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "__traced__"):
            trace_class(cls)
            setattr(cls, "__traced__", True)
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
