import numpy as np


def sol():
    counter = 0
    a = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])
    b = np.array([2, 4, -1])
    from scipy import linalg
    x = linalg.solve(a, b)
    counter = counter + len(a)*3
    return x, np.dot(a, x) == b, counter


if __name__ == "__main__":
    print(sol())
