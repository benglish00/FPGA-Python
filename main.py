import import_data
import numpy

# Get Calibration matrix
CalFile = import_data.pathname("RawCal1430.csv")
CalMatrix = import_data.csv_to_array(CalFile)

# Get Raw Data Matrix
RawFile = import_data.pathname("Data1430.csv")
RawMatrix = import_data.csv_to_array(RawFile)
print(CalMatrix)

CalMatrix = CalMatrix[numpy.lexsort(numpy.fliplr(CalMatrix).T)]

print(CalMatrix)