import numpy as np

def print_hello():
    print("hello from calibrate")

def sort(Matrix):
    """
    Returns an (m x n) array with rows sorted by column 1
    :param Matrix: (m x n)
    :return: SortedMatrix (m x n)
    """
    SortedMatrix = Matrix[
        np.lexsort(
            np.fliplr(Matrix).T)]  # flip then transpose for quick, default lexsort
    return SortedMatrix

def average(Matrix):
    Matrix = sort(Matrix)
    NumberRows = len(Matrix)
    print("Number rows = {}".format(NumberRows))


