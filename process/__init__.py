import numpy as np
import import_data as imp

def print_hello():
    print("hello from process")

def set_window(center, length):
    """
    Defines a window size and resets windows on edge
    :param length: int
    :param center: int
    :return: window (int1, int2)
    """
    winsize = length//8
    halfwin = winsize//2
    if center < halfwin:
        window = [0, winsize - 1]
    elif center > (length - halfwin):
        window = [-winsize, -1]
    else:
        window = [center - halfwin, center + halfwin]
    return window

def easy_max(Matrix, column=2):
    index = np.argmax(Matrix[:, column])
    amp_peak = Matrix[index, column]
    freq_peak = Matrix[index, 0]
    window = set_window(index, len(Matrix))
    fft_peak = np.mean(Matrix[window[0]:window[1], 1])
    return [freq_peak, fft_peak, amp_peak]

def write_scan(Matrix):
    """
    Writes a matrix to a file as a debug
    :param Matrix: (m x n) float
    :return: none
    """
    new_file = imp.pathname("RecScan1430.csv")
    np.savetxt(new_file, Matrix, delimiter=",")

def poly_max(Matrix, column=2):
    """
    Calculates peaks of column 1 based on windowed average
    Calculate peak of column 2 based on 2nd order poly
    Calculate peak of column 1 based on derivative of 2nd order poly
    :param Matrix: (m x n) float
    :param column: int
    :return: [3x1] float
    """
    index = np.argmax(Matrix[:, column])
    window = set_window(index, len(Matrix))
    fft_peak = np.mean(Matrix[window[0]:window[1], 1])
    #
    freq_slice = Matrix[window[0]:window[1],
                 0]
    amp_slice = Matrix[window[0]:window[1],
                2]
    amp_polyfit = np.polyfit(freq_slice,
                             amp_slice,
                             2)
    freq_peak = -amp_polyfit[1]/(2*amp_polyfit[0])
    amp_peak = amp_polyfit[0]*freq_peak**2 \
               + amp_polyfit[1]*freq_peak \
               + amp_polyfit[2]
    return [freq_peak, fft_peak, amp_peak]

def poly_coeff(Matrix, column=2):
    """
    windowed 2nd order fit
    :param Matrix: (m x n) float
    :param column: int
    :return: window indices and polyfit coefficients
    """
    index = np.argmax(Matrix[:, column])
    window = set_window(index, len(Matrix))
    freq_slice = Matrix[window[0]:window[1],
                 0]
    amp_slice = Matrix[window[0]:window[1],
                2]
    amp_polyfit = np.polyfit(freq_slice,
                             amp_slice,
                             2)
    return [window, amp_polyfit]

def poly_data(Matrix, column=2):
    index = np.argmax(Matrix[:, column])
    window = set_window(index, len(Matrix))
    coeff = poly_coeff(Matrix)[1]
    polyfit = np.zeros((window[1]-window[0],2))
    m=0
    for i in range (window[0],window[1]):
        x = Matrix[i,0]
        y = coeff[0]*x**2+coeff[1]*x+coeff[2]
        polyfit[m,0]=x
        polyfit[m,1]=y
        m +=1
    return polyfit


