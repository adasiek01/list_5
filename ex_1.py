import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy import linalg
import time
import math


def mean_time_counting(n,repeating):
    """
    Function counts the mean time
    n: size of matrix
    repeating: number of repetitions
    """
    coef_matrix = np.random.randint(0, 5, (n, n))
    result_matrix = np.random.randint(0, 5, (n, 1))
   
    times = []

    if np.linalg.det(coef_matrix) != 0:     # simultaneous equations must be solvable
        for i in range(0, repeating):
            start = time.time()
            x = linalg.solve(coef_matrix, result_matrix)
            end = time.time()
            times.append(end-start)
        mean = sum(times)/len(times)
        return mean


def arg_and_val(repeating):
    """
    Function solves the equation and counts time
    repeating: number of repetitions
    """
    x_axis = [2**n for n in range(2, 12)]
    y_axis = []

    for i in range(0, len(x_axis)):
        y_axis.append(mean_time_counting(x_axis[i], repeating))
    return x_axis, y_axis


def function(x, a, b):
    """
    Auxiliary function.
    """
    return a*(x**b) 


def plotting(repeating):
    """
    Function draws the graph
    Args: repeating: number of repetitions
    """
    x_ax, y_ax = arg_and_val(repeating)
    plt.scatter(x_ax, y_ax)
    plt.title("Results")
    plt.xlabel("Amount of equations")
    plt.ylabel("Time of calculating")
    

    popt, pcov = curve_fit(function, x_ax, y_ax)
    a = popt[0]
    b = popt[1]
    x_fitting = np.arange(300, 2000)
    plt.plot(x_fitting, function(x_fitting, *popt))
    plt.show()
    return a,b


if __name__ == "__main__":
    print(plotting(5))
