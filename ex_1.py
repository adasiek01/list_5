import numpy as np
from scipy import linalg
import time
import random


def sol(a, b):
    start_time = time.time()
    x = linalg.solve(a, b)
    end_time = time.time()
    time_1 = end_time - start_time
    return x, np.dot(a, x) == b, time_1


if __name__ == "__main__":
    for i in range(10):
        c = np.array([[random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)], [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)], [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]])
        d = np.array([[random.randint(0, 100)], [random.randint(0, 100)], [random.randint(0, 100)]])
        print(sol(c, d))



