import numpy as np 
import matplotlib.pyplot as plt
import scipy as sp 

#Analysis for X-Ray data

#Function for reading in the file
def readDataFile(filename):
    with open(filename) as f:
        content = f.readlines()

    f.close()
    return content

#Setting up the data
def DataSetup(Data, filename):
    NoOfPoints = len(Data)
    TwoTheta = np.zeros(NoOfPoints)
    Intensity = np.zeros(NoOfPoints)
    for i in range(NoOfPoints):
        temp = Data[i].replace("\n","")
        temp = temp.split(" ")
        TwoTheta[i] = temp[0]
        Intensity[i] = temp[1]

    #Putting all into a dictionary
    AllData = {"Filename": filename, "2Theta": TwoTheta, "Intensity": Intensity}

    return AllData

#Plotting Data
def PlotData(Data, yaxis = "log"):
    fig, ax = plt.subplots()
    ax.plot(Data['2Theta'],Data['Intensity'])
    ax.grid(alpha=0.3)
    ax.set_xlabel(r"2$\theta$")
    ax.set_ylabel("cps")
    if yaxis == "log":
        plt.yscale("log")

    #specify xrange
    ax.set_xlim([min(Data['2Theta']),max(Data['2Theta'])])



    return fig, ax