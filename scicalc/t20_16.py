import numpy as np


def min_of_max(M):
    return np.min([np.max(r) for r in M])


if __name__ == "__main__":
    M = np.array([
        [1, 2, 5, 6],
        [5, 7, 9, 1],
        [4, 5, 8, 8],
        [3, 4, 7, 9]
    ])

    print(f"Min of maximum: {min_of_max(M)}")
