import import_data
import csv
import numpy

import_data.print_hello()


CalFile = import_data.pathname("Cal1430.csv")
RawFile = import_data.pathname("Data1430.csv")
print(CalFile)
print(RawFile)
CalMatrix = import_data.csv_to_array(CalFile)
RawMatrix = import_data.csv_to_array(RawFile)
print(RawMatrix)
