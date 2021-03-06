import matplotlib.pyplot as plt 
import numpy as np 
import os 
from pathlib import Path
import pdb
import MokeDataAnalysisVerklegt as MK
import time
#Data analysis for MOKE measurements
#Adjust axis size
plt.rcParams.update({'font.size': 14})

def CoAlZr(Figure, Axes, MagRemBool = False, CoercField = False):

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

        if degrees == 10:
            DataDeg10 = AllData.copy()
        if degrees == 100:
            DataDeg100 = AllData.copy()



    #Plotting
    fig = plt.figure()
    ax = plt.subplot(111, projection='polar')
    ax.plot(np.deg2rad(Deg), CoercivityAll,'*--')
    ax.set_rmax(10)
    ax.set_rmin(0)
    #ax.set_rticks([0.5, 1, 1.5, 2])  # less radial ticks
    #ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
    ax.grid(True)
    ax.set_title("Coercivity for CoAlZr")
    plt.savefig("CoAlZr_Coercivity.png",format="png",dpi=300)

    #Plotting certain loops for Report
    fig0 = plt.figure()
    ax0 = plt.subplot(111)
    ax0.plot(DataDeg10["Magnetic Field [G]"],DataDeg10['VoltageAverage'],'-',label="10 gráður")
    ax0.plot(DataDeg100["Magnetic Field [G]"],DataDeg100['VoltageAverage'],'-',label="100 gráður")
    ax0.legend()
    ax0.set_xlabel("Álagt segulsvið [G]")
    ax0.set_ylabel(r"M/M$_{sat}$")
    ax0.tick_params(right=True,top=True,direction='in',labelsize=22,size=12)
    plt.savefig("HystLoopExample.png", format="png", dpi=300, bbox_inches="tight")

    #Plotting relative Magnetic remanance - with skewed axis for clearer viewing
    fig1 = plt.figure()
    ax1 = plt.subplot(111, projection='polar')
    ax1.plot(np.deg2rad(Deg),MagRemAll,'*--')
    ax1.set_xlabel("Degrees")
    #ax2.set_ylabel("Relative Magnetic Remanence")
    #ax2.grid(alpha=0.3)
    ax1.set_rmax(1)
    ax1.set_rmin(0)
    ax1.set_title("Magnetic Remanence for CoAlZr")
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
    ax3.set_rmax(10)
    ax3.plot(np.deg2rad(Deg), rightSwitchAll,'*--', label = "right switch")
    ax3.plot(np.deg2rad(Deg), abs(leftSwitchAll),'*--', label = "left switch")
    #ax3.set_xlabel("Degrees")
    #ax3.set_ylabel("Coercive field")
    #ax3.legend()
    plt.savefig("CoAlZr_CoerciveFieldLeftRight.png",format="png",dpi=300)
    plt.close(fig)
    plt.close(fig0)
    plt.close(fig1)
    plt.close(fig2)
    plt.close(fig3)

    end = time.time()
    
    #Plot to desired axis
    if MagRemBool:
        print("búhh")
        Axes.plot(np.deg2rad(Deg),MagRemAll,'*--')
        Axes.set_rmax(1.1)
        Axes.set_rmin(0)

    if CoercField:
        Axes.plot(np.deg2rad(Deg),CoercivityAll,'*--')
        #Axes.set_rmax(1.1)
        #Axes.set_rmin(0)

    return Figure, Axes
