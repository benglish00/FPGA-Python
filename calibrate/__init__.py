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
    AvgMatrix = np.zeros((65,3))
    maxValue = max(Matrix[:,0])
    i = m = n = 0
    while Matrix[i,0] <= maxValue:
        Tx = Matrix[i,0]
        index = np.where(Matrix[:,0]==Matrix[i,0])[0]
        print(index)
        for n in range(0,3):
            a = 2
            AvgMatrix[m,n] = np.mean(Matrix[index[0:],n])
        m = m + 1
        i = index[-1]+1
        print(AvgMatrix)
