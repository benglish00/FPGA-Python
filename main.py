import import_data

import_data.print_hello()
CalFile = import_data.pathname("Cal1430.csv")
RawFile = import_data.pathname("Data1430.csv")
print(CalFile)
print(RawFile)
CalData = import_data.importCSV(CalFile)