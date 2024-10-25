import numpy as np
from itertools import combinations


def perim(points):
    p1, p2, p3 = points
    return np.linalg.norm(p2-p1) + np.linalg.norm(p3-p2) + np.linalg.norm(p3-p1)


def largest_perimeter_triangle(points):
    n = points.shape[0]
    max_perimeter = 0
    best_triangle = None

    for i, j, k in combinations(range(n), 3):
        cur_points = (points[i], points[j], points[k])
        perimeter = perim(cur_points)
        if perimeter > max_perimeter:
            max_perimeter = perimeter
            best_triangle = cur_points
    return best_triangle, max_perimeter


if __name__ == "__main__":
    points = np.array([
        [0, 0],  
        [1, 0],  
        [0, 1],  
        [1, 1],  
        [0.5, 1.5]  
    ])

    max_triangle, max_perimeter = largest_perimeter_triangle(points)

    print(f"Max triangle is: ({max_triangle}) with perim {max_perimeter}")
