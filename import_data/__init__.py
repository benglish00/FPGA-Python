import os
import csv

def print_hello():
    print("hello")

def pathname(filename):
    """
    return the filename
    :param filename: string
    :return:
    """
    return os.path.join("C:\\","Users", "Brian", "OneDrive", "Data", "FPGA_Sensor_Test", filename)

def importCSV(filename):
    """
    return csv data
    :param filename: string
    :return: csv data from file
    """
    r = list()
    with open(filename, "r") as f:
        r = r.append(csv.reader(f, delimiter=","))
        return r

def printCSV(csvData):
    """
    return None
    :param csvData: List
    :return: None
    """
    for row in csvData:
        print(",".join(row))