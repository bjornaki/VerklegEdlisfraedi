import numpy as np 
import matplotlib.pyplot as plt 
import X_Ray_analysis as Xray
import pdb

#Adjust axis size
plt.rcParams.update({'font.size': 14})

#-----First comparing XRD-----#
#Import data - first XRD
filename008 = "KEN008_XRD_40_85deg.xy"
DataXRD008 = Xray.readDataFile(filename008)
filename009 = "KEN009_XRD_40_85deg.xy"
DataXRD009 = Xray.readDataFile(filename009)

#Setting up data
DataXRD008 = Xray.DataSetup(DataXRD008, filename008)
DataXRD009 = Xray.DataSetup(DataXRD009, filename009)

#Plotting Data
fig, ax = Xray.PlotData(DataXRD008,None,None, yaxis="log", shift=True,shiftVal=100)
fig, ax = Xray.PlotData(DataXRD009, fig, ax, yaxis="log")
#Adding in phase data from Fe and MgAlO
Fe = [44.62,64.932]#in 2Theta  - Iron - Fe (110) and (200)
MgAlO = [44.346]#in 2Theta - MgAlO (400)
Si = [69.242]#in 2Theta - Si (400)
ax.axvline(x = Fe[0],c="b",label = "Fe")
ax.axvline(x = Fe[1],c="b",label = "_nolegend_")
ax.axvline(x = MgAlO,c="g",label = "MgAlO")
ax.axvline(x = Si,c="y",label = "Si")
#Adding text
ax.text(41,10e7,"(110)",c="b",size = "large")#Iron
ax.text(63,10e7,"(200)",c="b",size = "large")#Iron
ax.text(45,10e7,"(400)",c="g",size = "large")#MgAlO
ax.text(67,10e7,"(400)",c="y",size = "large")#Si

#legend
ax.legend()
plt.savefig("KEN_XRD_Comparison.png",format="png",dpi=300,bbox_inches='tight')

#Figure of KEN008 with phi = 90, out of plane measurement
#Import data - first XRD
filename008 = "KEN008_XRD_65deg_phi180.xy"
DataXRD008 = Xray.readDataFile(filename008)

#Setting up data
DataXRD008 = Xray.DataSetup(DataXRD008, filename008)

#Plotting Data
fig0, ax0 = Xray.PlotData(DataXRD008,None,None, yaxis="linear", shift=False, scanAxis = "Phi")
ax0.legend()
plt.savefig("KEN008_phi180.png",format="png",dpi=300,bbox_inches='tight')

#-------Then comparing XRR------#
filename008 = "KEN008_XRR_0_5deg.xy"
DataXRR008 = Xray.readDataFile(filename008)
filename009 = "KEN009_XRR_0_5deg.xy"
DataXRR009 = Xray.readDataFile(filename009)

#Setting up data
DataXRR008 = Xray.DataSetup(DataXRR008, filename008)
DataXRR009 = Xray.DataSetup(DataXRR009, filename009)

#Finding the critical angle
Data008 = Xray.CriticalAngle(DataXRR008,[0.5,0.7])
Data009 = Xray.CriticalAngle(DataXRR009,[0.5,0.7])

#Finding peaks in XRR data
DataXRR008 = Xray.FilmThickness(DataXRR008,[0.9,4])
DataXRR009 = Xray.FilmThickness(DataXRR009,[0.9,4])

#Plotting Data
fig2, ax2 = Xray.PlotData(DataXRR008, None, None, yaxis="log", XRR=True, Filtered=False, ThetaCr = False, shift = True, shiftVal = 10)
fig2, ax2 = Xray.PlotData(DataXRR009, fig2, ax2, yaxis="log", XRR=True, Filtered=False, ThetaCr = False)
ax2.legend(["KEN008","KEN009"])
plt.savefig("KEN_XRR_Comparison.png",format="png",dpi=300,bbox_inches='tight')

#Fourier Thickness
fig3, ax3 = Xray.FourierThickness(DataXRR008,None,None)
fig3, ax3 = Xray.FourierThickness(DataXRR009,fig3,ax3)
ax3.legend(loc = 1)
plt.savefig("Fourier_Comparison.png",format="png",dpi=300,bbox_inches='tight')

#Density
print("Fyrir KEN008 er krítískt horn:",DataXRR008['2ThetaCritical']/2)
print("Fyrir KEN009 er krítískt horn:",DataXRR009['2ThetaCritical']/2)
r0 = 2.82e-15
A = 9.2733e-26
Z = 26
Na = 6.022e23
lamb = 0.15406e-9
ThetaC = np.deg2rad(0.35)
rho = ((ThetaC**2)*(np.pi*A)) / (r0*lamb**2*Na*Z)
print("Massaþéttleikinn er: ",rho)
