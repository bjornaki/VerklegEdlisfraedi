import numpy as np 
import matplotlib.pyplot as plt 
import X_Ray_analysis as Xray
import pdb
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

#Import data - first XRD
filename = "KEN008_XRD_40_85deg.xy"
DataXRD = Xray.readDataFile(filename)

#Setting up data
DataXRD = Xray.DataSetup(DataXRD, filename)

#Plotting Data
fig, ax = Xray.PlotData(DataXRD, None, None, yaxis="log")
plt.show()

#Then XRR data
filename = "KEN008_XRR_0_5deg.xy"
DataXRR = Xray.readDataFile(filename)

#Setting up data
DataXRR = Xray.DataSetup(DataXRR, filename)

#Finding the critical angle
Data = Xray.CriticalAngle(DataXRR,[0.5,0.7])

#Finding peaks in XRR data
DataXRR = Xray.FilmThickness(DataXRR,[0.9,4])

#Plotting Data
fig2, ax2 = Xray.PlotData(DataXRR, None, None, yaxis="log", XRR=True, Filtered=False, ThetaCr = True, showPeaks=True)
ax2_inlet = inset_axes(ax2, width="50%", height=0.7, loc=1,borderpad=1.5)
ax2_inlet.plot(Data['m**2'],Data['Residue'],'*')
ax2_inlet.set_xlabel(r"m$^2$")
ax2_inlet.set_ylabel("Leif")
ax2_inlet.set_ylim([-0.00003,0.00003])
ax2_inlet.ticklabel_format(style='sci',scilimits=(0,-7))
ax2_inlet.axhline(y=0)
plt.savefig("KEN008_XRR.png",format="png",dpi=300,bbox_inches='tight')#Saving file
plt.show()

#Fourier Thickness
fig3, ax3 = Xray.FourierThickness(DataXRR, None, None)
plt.show()
