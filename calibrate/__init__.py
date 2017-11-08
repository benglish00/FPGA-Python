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
    The input matrix is includes multiple (x,y1,y2) data sets.
    The function averages y1 and y2 for each x and returns a
    reduced Matrix. It is currently exactly [65,3]
    :param Matrix: [m x 3] array
    :return: AvgMatrx: exactly [65,3]
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

def rectify(CalMatrix,RawMatrix):
    """
    This rectifies the RawMatrix based on the CalMatrix
    :param CalMatrix: Reduced calibration Matrix (65x3)
    :param RawMatrix: n x 3 array, all column 1 values should be in CalMatrix column 1
    :return: sorted RectifyMatrix
    """
    NumPoints = len(RawMatrix)
    RectifyMatrix = np.zeros((NumPoints,3))
    RectifyMatrix[:,0:2]=RawMatrix[:,0:2]
    for i in range (NumPoints):
        Tx = RawMatrix[i,0]
        index = np.where(CalMatrix[:,0]==Tx)[0]
        RectifyMatrix[i,2] = RawMatrix[i,2] - CalMatrix[index,2]
    return sort(RectifyMatrix)

