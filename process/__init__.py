import numpy as np
import scipy

def print_hello():
    print("hello from process")

def set_window(center, length):
    """
    Defines a window size and resets windows on edge
    :param length: int
    :param center: int
    :return: window (int1, int2)
    """
    winsize = 21
    halfwin = winsize // 2
    if center < halfwin:
        window = [0,winsize-1]
    elif center > (length - halfwin):
        window = [-winsize,-1]
    else:
        window = [center-halfwin, center+halfwin]
    return window

def easy_max(Matrix,column=2):
    index = np.argmax(Matrix[:,column])
    amp_peak = Matrix[index,column]
    freq_peak = Matrix[index,0]
    window = set_window(index, len(Matrix))
    fft_peak = np.mean(Matrix[window[0]:window[1],1])
    return [freq_peak, fft_peak, amp_peak]
