import numpy as np 
import matplotlib.pyplot as plt
import scipy as sp 
from scipy.signal import find_peaks, find_peaks_cwt, savgol_filter
import pdb

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
def PlotData(Data, yaxis = "log", XRR = False, Filtered = False):
    fig, ax = plt.subplots()
    ax.plot(Data['2Theta'],Data['Intensity'])
    ax.grid(alpha=0.3)
    ax.set_xlabel(r"2$\theta$")
    ax.set_ylabel("cps")
    if yaxis == "log":
        plt.yscale("log")

    if XRR == True:
        ax.plot(Data['2Theta'][Data['Peaks']],Data['Intensity'][Data['Peaks']],'*')
    if Filtered == True:
        ax.plot(Data['2Theta'],Data['IntensFiltered'])

    #specify xrange
    ax.set_xlim([min(Data['2Theta']),max(Data['2Theta'])])

    return fig, ax

# test

#Function to get the film thickness
def FilmThickness(Data):
    #Filter Data for reference
    FilteredIntens = savgol_filter(Data['Intensity'],7,3)
    #Finding peaks
    peaks = find_peaks_cwt(FilteredIntens,np.arange(0.1,0.5,0.1))

    Data['Peaks'] = peaks
    Data['IntensFiltered'] = FilteredIntens
    #Data['Peak properties'] = properties

    return Data
