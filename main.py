import import_data
import numpy
import calibrate

# Get Calibration matrix
CalFile = import_data.pathname("RawCal1430.csv")
CalMatrix = import_data.csv_to_array(CalFile)
CalAvg = calibrate.average(CalMatrix)

# Get Raw Data Matrix
RawFile = import_data.pathname("Data1430.csv")
RawMatrix = import_data.csv_to_array(RawFile)

#Rectify Scan
RecData = calibrate.rectfiy(CalAvg,RawMatrix)
print(RecData)