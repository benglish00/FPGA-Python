import os
import csv
import numpy

def print_hello():
    print("hello")

def pathname(filename):
    """
    return the filename
    :param filename: string
    :return:
    """
    return os.path.join("C:\\","Users", "Brian", "OneDrive", "Data", "FPGA_Sensor_Test", filename)

def csv_to_array(filename):
    return numpy.genfromtxt(filename, delimiter=",")