import import_data
import csv
import numpy

# Get Calibration matrix
CalFile = import_data.pathname("Cal1430.csv")
CalMatrix = import_data.csv_to_array(CalFile)

# Get Raw Data Matrix
RawFile = import_data.pathname("Data1430.csv")
RawMatrix = import_data.csv_to_array(RawFile)
print(RawMatrix)
