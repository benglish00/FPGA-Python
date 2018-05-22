import import_data
import calibrate
import process
import numpy as np
import matplotlib.pyplot as plt

# Get Calibration matrix
CalFile = import_data.pathname("RawCal1430.csv")
CalMatrix = import_data.csv_to_array(CalFile)
CalAvg = calibrate.average(CalMatrix)

# Get Raw Data Matrix
RawFile = import_data.pathname("Data1430.csv")
RawMatrix = import_data.csv_to_array(RawFile)

#Rectify Scan
RecMatrix = calibrate.rectify(CalAvg,RawMatrix)
Peaks = process.poly_max(RecMatrix)
print(Peaks)

meanFFT = process.FFTvInput(RecMatrix, 1)
#Plotting
polyfit = process.poly_data(RecMatrix)
# plt.plot(RecMatrix[:,0],RecMatrix[:,2],'ro', polyfit[:,0], polyfit[:,1],'b', linewidth=8)
plt.plot(RecMatrix[:,0],RecMatrix[:,1], 'ro', meanFFT[:,0], meanFFT[:,1], 'bo')
plt.ylabel('FFT Frequency [MHz]')
plt.xlabel('Tx Frequency [MHz]')
plt.show()