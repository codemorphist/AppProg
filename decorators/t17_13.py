from typing import TypeAlias, Callable, Any
from pprint import pp, pprint
from functools import wraps



MatrixTable: TypeAlias = list[list[int]]
MatrixDict: TypeAlias = dict[int, list[int]]
Matrix: TypeAlias = MatrixTable | MatrixDict


def conver_to_mt(m: Matrix) -> MatrixTable:
    """
    Convert Matrix to MatrixTable
    
    :param m: Matrix to convert
    """
    if type(m) is list:
        return m

    keys = sorted(m.keys(), reverse=True)
    mt = [m[k] for k in keys]
    return mt


def matrixtable_params(func: Callable[[Matrix, Matrix], Any]):
    @wraps(func)
    def _func(m1: Matrix, m2: Matrix):
        m1 = conver_to_mt(m1)
        m2 = conver_to_mt(m2)
        return func(m1, m2)

    return _func


@matrixtable_params
def print_matrix(m1: Matrix, m2: Matrix):
    print(m1)
    print(m2)


if __name__ == "__main__":
    # matrix like list of list
    m1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # matrix like dict of list
    m2 = {
        0: [3, 2, 1],
        1: [6, 5, 4],
        2: [9, 7, 8]
    }

    print_matrix(m1, m2)
