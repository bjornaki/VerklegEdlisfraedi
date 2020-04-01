import matplotlib.pyplot as plt 
import numpy as np 
import os 
from pathlib import Path
import pdb
import MokeDataAnalysisVerklegt as MK
import time
#Data analysis for MOKE measurements

#Measurements taken at the following degrees
Deg = np.arange(0,370,10)
CoercivityAll = np.zeros(len(Deg))
leftSwitchAll = np.zeros(len(Deg))
rightSwitchAll = np.zeros(len(Deg))
MagRemAll = np.zeros(len(Deg))

#------Going through the data------#
#specify the folder path
data_folder = Path("C:\\Users\\lenovo\\Documents\\Verkfræðileg eðlisfræði HÍ\\Vorönn 2020\\Verklegt\\MOKE\\CoAlZr")

start = time.time()
counter = 0
for degrees in Deg:
    #specify the name of the file
    string1 = "CAZ_14_"
    string2 = str(degrees)
    string3 = "-Deg_avg.txt"
    string4 = string1 + string2 + string3
    tempFile = data_folder / string4

    #Reading the data
    Content = MK.readMokeFile(tempFile)

    #Setting up the data into a dictionary
    Info, AllData = MK.DataSetup(Content, "CoAlZr", degrees)

    #Plotting to chech the loops
    MK.PlotLoop(AllData,False)

    #Fitting the saturation linearly and normalizing 
    AllData = MK.MaxSatLinearFit(AllData,-100,100)

    #Evaluating the Coercivity
    leftSwitch, rightSwitch, Coercivity = MK.MokeCoercivity(AllData,"CoAlZr",plotting=True)
    CoercivityAll[counter] = Coercivity
    leftSwitchAll[counter] = leftSwitch
    rightSwitchAll[counter] = rightSwitch

    #Evaluating the relative magnetic remanence
    MagRem = MK.MokeMagneticRemanence(AllData)
    MagRemAll[counter] = MagRem
    counter += 1



#Plotting
fig = plt.figure()
ax = plt.subplot(111, projection='polar')
ax.plot(np.deg2rad(Deg), CoercivityAll,'*--')
ax.set_rmax(100)
ax.set_rmin(0)
#ax.set_rticks([0.5, 1, 1.5, 2])  # less radial ticks
#ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
ax.grid(True)

ax.set_title("Coercivity for CoAlZr")
plt.savefig("CoAlZr_Coercivity.png",format="png",dpi=300)

#Plotting relative Magnetic remanance - with skewed axis for clearer viewing
fig2 = plt.figure()
ax2 = plt.subplot(111, projection='polar')
ax2.plot(np.deg2rad(Deg),MagRemAll,'*--')
ax2.set_xlabel("Degrees")
#ax2.set_ylabel("Relative Magnetic Remanence")
#ax2.grid(alpha=0.3)
ax2.set_rmax(1)
ax2.set_rmin(0.82)
ax2.set_title("Magnetic Remanence for CoAlZr")
plt.savefig("CoAlZr_MagRem.png",format="png",dpi=300)

#Plotting relative Magnetic remanance - with non-skewed axis 
fig2 = plt.figure()
ax2 = plt.subplot(111, projection='polar')
ax2.plot(np.deg2rad(Deg),MagRemAll,'*--')
ax2.set_xlabel("Degrees")
#ax2.set_ylabel("Relative Magnetic Remanence")
#ax2.grid(alpha=0.3)
ax2.set_rmax(1.1)
ax2.set_rmin(0)
ax2.set_title("Magnetic Remanence for CoAlZr")
plt.savefig("CoAlZr_MagRem_ZeroToOne.png",format="png",dpi=300)


#Plotting right and left Coercive field to see if the curve is shifted(bias)
fig3 = plt.figure()
ax3 = plt.subplot(111, projection='polar')
ax3.set_rmin(0)
ax3.set_rmax(100)
ax3.plot(np.deg2rad(Deg), rightSwitchAll,'*--', label = "right switch")
ax3.plot(np.deg2rad(Deg), abs(leftSwitchAll),'*--', label = "left switch")
#ax3.set_xlabel("Degrees")
#ax3.set_ylabel("Coercive field")
#ax3.legend()
plt.savefig("CoAlZr_CoerciveFieldLeftRight.png",format="png",dpi=300)
plt.show()

end = time.time()
print("took: ",end-start," seconds")
