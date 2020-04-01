import matplotlib.pyplot as plt 
import numpy as np 
import os 
from pathlib import Path
import pdb
from numba import jit, njit, vectorize
#Data analysis for MOKE measurements

#Function That reads in the txt file
def readMokeFile(filename):
    with open(filename) as f:
        content = f.readlines()

    f.close()
    return content

#Ath laga þannig að það finni automatically hvar maður byrjar ef ekki komment!!
def DataSetup(Data, filename, degrees):
    #First find the string Magnetic to know were to start
    for i in range(10):#10 chosen arbitrarily
        if Data[i].find("Magnetic") != -1:
            start = i#Index where table starts
            break

    Deg = int(degrees)
    Info = Data[start-1].split(" ")
    NumLoops = 1
    NumPoints = len(Data) - start - 1
    MagField = np.zeros([NumPoints,NumLoops])
    DiodeVolt = np.zeros([NumPoints,NumLoops])
    #CorrVolt = np.zeros([NumPoints,NumLoops])
    #LaserPower = np.zeros([NumPoints,NumLoops])

    #Putting all into temp variables
    MagTemp = np.zeros(NumLoops*NumPoints)
    DiodeVoldTemp = np.zeros(NumLoops*NumPoints)
    #CorrVoltTemp = np.zeros(NumLoops*NumPoints)
    #LaserPowerTemp = np.zeros(NumLoops*NumPoints)
    for i in range(NumLoops*NumPoints):
        Temp = Data[start+1+i].split("\t")
        MagTemp[i] = float(Temp[0])
        DiodeVoldTemp[i] = float(Temp[1])
        #CorrVoltTemp[i] = float(Temp[2])
        #LaserPowerTemp[i] = float(Temp[3])

    #Assigning each measurement
    N = NumPoints
    for i in range(NumLoops):
        #Taking out the data for the applied field
        MagField[0:N,i] = MagTemp[N*i:N*(i+1)]
        DiodeVolt[0:N,i] = DiodeVoldTemp[N*i:N*(i+1)]
        #CorrVolt[0:N,i] = CorrVoltTemp[N*i:N*(i+1)]
        #LaserPower[0:N,i] = LaserPowerTemp[N*i:N*(i+1)]


    #Putting all into a dictionary
    AllData = {"Magnetic Field [G]": MagField, "DiodeVoltage [V]": DiodeVolt, "Degrees": Deg, "Filename": filename, "NoInLoop": NumPoints}

    return Info, AllData


#Function that plots the raw data
def PlotLoop(Data,UseCorrectedVoltage):
    fig, ax = plt.subplots()
    #loading the data
    MagField = Data['Magnetic Field [G]']
    if UseCorrectedVoltage == True:
        Voltage = Data['Corrected Voltage [V]']
    else:
        Voltage = Data['DiodeVoltage [V]']
    #plotting the image
    n,m = np.shape(MagField)
    for i in range(m):
        ax.plot(MagField[0:n,i],Voltage[0:n,i])
    
    ax.set_xlabel("Applied field [Gauss]")
    ax.set_ylabel("Voltage [V]")
    ax.grid(alpha=0.3)
    #show the image
    plt.close('all')


#Function that linearly fits the saturation moment and normalizes the hysterisis loop
def MaxSatLinearFit(Data,FieldMin,FieldMax,UseCorrectedVoltage=False,plotting=False):
    MagField = Data['Magnetic Field [G]']
    n,m = np.shape(MagField)
    if UseCorrectedVoltage:
        Voltage = Data['Corrected Voltage [V]']
    else:
        Voltage = Data['DiodeVoltage [V]']
    
    #fitting a linear fit for each scan both upper and lower
    DataNormalized = np.zeros([n,m])
    for i in range(m):
        #First fitting upper
        upperValuesIndex = np.where(MagField[0:n,i] >= FieldMax)
        upperValuesIndex = upperValuesIndex[0]
        upperFit = np.polyfit(MagField[:,i][upperValuesIndex],Voltage[:,i][upperValuesIndex],1)
        #Lower fit
        lowerValuesIndex = np.where(MagField[0:n,i] <= FieldMin)
        lowerValuesIndex = lowerValuesIndex[0]
        lowerFit = np.polyfit(MagField[:,i][lowerValuesIndex],Voltage[:,i][lowerValuesIndex],1)
        x = np.linspace(min(MagField[:,i]),max(MagField[:,i]))
        yUpper = np.polyval(upperFit,x)
        yLower = np.polyval(lowerFit,x)
        #Plotting
        if plotting:
            fig,ax = plt.subplots()
            ax.plot(MagField[:,i],Voltage[:,i],'*')
            ax.plot(x,yUpper)
            ax.plot(x,yLower)
        #Normalizing - Older method
        #MaxUpper = max(yUpper)
        #MinLower = min(yLower)
        #MidPoint = (MaxUpper + MinLower)/2
        #yNew = (Voltage[:,i] - MidPoint)
        ##Amplitude
        #Amplitude = (np.polyval(upperFit,75) - np.polyval(lowerFit,-75))/2
        #yNew = yNew/Amplitude
        #DataNormalized[:,i] = yNew

        #Method Snorri
        UpperAve = np.average(Voltage[:,i][upperValuesIndex])
        LowerAve = np.average(Voltage[:,i][lowerValuesIndex])
        MidPoint = (UpperAve + LowerAve)/2
        Amplitude = (UpperAve - LowerAve)/2
        yNew = (Voltage[:,i] - MidPoint)
        yNew = yNew/Amplitude
        # fig1,ax1 = plt.subplots()
        # ax1.plot(MagField[:,i],yNew)
        if plotting:
            fig1,ax1 = plt.subplots()
            ax1.plot(MagField[:,i],yNew)
        DataNormalized[:,i] = yNew

    Data['VoltageNormalized'] = DataNormalized
    Data['VoltageAverage'] = np.average(DataNormalized,axis=1)

    plt.close()

    if plotting:
        fig2,ax2 = plt.subplots()
        ax2.plot(MagField[:,0],Data['VoltageNormalized'])
        plt.close('all')

    return Data

#Function that finds the coercive field
def MokeCoercivity(Data,subfolder,plotting=True):
    #lowLow, highLow represent were the field is switching!
    MagneticField = Data['Magnetic Field [G]']
    Voltage = Data['VoltageAverage']
    gradient = np.gradient(Data['VoltageAverage'])
    #New way of fitting n points arround zero crossing
    counter = 0
    for i in range(Data['NoInLoop']-1):
        if (np.sign(Voltage[i]) != np.sign(Voltage[i+1])):
            if counter == 0:
                lowerSwitchPosition = i
                counter += 1
            else:
                higherSwitchPosition = i 

    #Fitting lower switch with a linear fit -> 2 points around switching position
    polyLower = np.polyfit(MagneticField[:,0][lowerSwitchPosition-2:lowerSwitchPosition+2],Voltage[lowerSwitchPosition-2:lowerSwitchPosition+2],1)
    #Fitting upper switch with a linear fit -> 2 points around switching position
    polyUpper = np.polyfit(MagneticField[:,0][higherSwitchPosition-2:higherSwitchPosition+2],Voltage[higherSwitchPosition-2:higherSwitchPosition+2],1)
    #Older method - kept for reference
    #Fitting lower switch
    #lowerValuesMagField = np.where((MagneticField[:,0] < lowHigh) & (MagneticField[:,0] > lowLow))
    #lowerValuesMoment = np.where((Voltage > -0.9) & (Voltage < 0.9))
    #commonLowerValues = np.intersect1d(lowerValuesMagField,lowerValuesMoment)
    #Linear fit
    #polyLower = np.polyfit(MagneticField[:,0][commonLowerValues],Voltage[commonLowerValues],1)
    #Fitting upper switch
    #upperValuesMagField = np.where((MagneticField[:,0] < highHigh) & (MagneticField[:,0] > highLow))
    #upperValuesMoment = np.where((Voltage > -0.9) & (Voltage < 0.9))
    #commonUpperValues = np.intersect1d(upperValuesMagField,upperValuesMoment)
    #Linear fit
    #polyUpper = np.polyfit(MagneticField[:,0][commonUpperValues],Voltage[commonUpperValues],1)

    #Calculating the Coercivity
    rightSwitch = -polyUpper[1]/polyUpper[0]
    leftSwitch = -polyLower[1]/polyLower[0]
    Coercivity = (rightSwitch - leftSwitch)/2

    #Plotting
    x = np.linspace(min(MagneticField[:,0]),max(MagneticField[:,0]))
    yLower = np.polyval(polyLower,x)
    yUpper = np.polyval(polyUpper,x)
    #Figure
    if plotting:
        fig, ax = plt.subplots()
        ax.plot(MagneticField[:,0],Voltage,'*--')
        ax.plot(x,yLower)
        ax.plot(x,yUpper)
        ax.set_xlabel("Applied field [Gauss]")
        ax.set_ylabel("Moment [arb. un.]")
        ax.grid(alpha=0.3)
        ax.set_ylim(-1.3,1.3)
        ax.set_title(Data['Filename'] + ", " + str(Data['Degrees']) + " deg")
        #plotting vertical line to show the coercive field
        ax.axvline(x=leftSwitch,color='k')#left switch
        ax.axvline(x=rightSwitch,color='k')#right switch
        #saving and/or showing the plot
        name = Data['Filename']
        deg = str(Data['Degrees'])
        stringName = subfolder + "\\" + name + " " + deg + " degrees.png"
        plt.savefig(stringName,dpi=300,format="png")
    

    return leftSwitch, rightSwitch, Coercivity


#Function that calculates the relative magnetic remanance
def MokeMagneticRemanence(Data):
    MagField = Data['Magnetic Field [G]'][:,0]
    Location = np.where(MagField == 0)
    Moment = Data['VoltageAverage']
    UpperValue = Moment[Location[0][0]]
    LowerValue = Moment[Location[0][1]]
    MagRem = (UpperValue - LowerValue)/2

    return MagRem




