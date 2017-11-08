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
    """

    :param Matrix:
    :return:
    """
    Matrix = sort(Matrix)
    AvgMatrix = np.zeros((65,3))
    maxValue = max(Matrix[:,0])
    i = m = n = 0
    while Matrix[i,0] <= maxValue:
        index = np.where(Matrix[:,0]==Matrix[i,0])[0]
        for n in range(0,3):
            AvgMatrix[m,n] = np.mean(Matrix[index[0:],n])
        m = m + 1
        if index[-1]+1 < len(Matrix):
            i = index[-1]+1
        else:
            break
    return AvgMatrix
