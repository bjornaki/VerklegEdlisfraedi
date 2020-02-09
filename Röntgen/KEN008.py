import numpy as np 
import matplotlib.pyplot as plt 
import X_Ray_analysis as Xray
import pdb

#Import data - first XRD
filename = "KEN008_XRD_40_85deg.xy"
DataXRD = Xray.readDataFile(filename)

#Setting up data
DataXRD = Xray.DataSetup(DataXRD, filename)
pdb.set_trace()

#Plotting Data
fig, ax = Xray.PlotData(DataXRD, yaxis="log")
plt.show()

#Then XRR data
filename = "KEN008_XRR_0_5deg.xy"
DataXRR = Xray.readDataFile(filename)

#Setting up data
DataXRR = Xray.DataSetup(DataXRR, filename)
pdb.set_trace()

#Plotting Data
fig2, ax2 = Xray.PlotData(DataXRR, yaxis="log")
plt.show()
