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
def PlotData(Data, yaxis = "log", XRR = False, Filtered = False, ThetaCr = False):
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
    if ThetaCr == True:
        ax.axvline(x=Data['2ThetaCritical'])

    #specify xrange
    ax.set_xlim([min(Data['2Theta']),max(Data['2Theta'])])

    return fig, ax

# test

#Function to get the film thickness
def FilmThickness(Data, range):
    #Filter Data for reference
    FilteredIntens = savgol_filter(Data['Intensity'],7,3)
    #Finding peaks
    peaks = find_peaks_cwt(FilteredIntens,np.arange(0.1,0.5,0.1))

    Data['Peaks'] = peaks
    Data['IntensFiltered'] = FilteredIntens
    #Data['Peak properties'] = properties

    PeaksInRangeIndex = np.where((Data['2Theta'][peaks] <= range[1]) & (Data['2Theta'][peaks] >= range[0]))
    PeaksTrue = peaks[PeaksInRangeIndex[0]]#The peaks within the specified range
    m = np.arange(1,len(PeaksTrue)+1,1)#Number of peaks for use with thickness model
    m_2 = m**2#m squared
    Theta_m = Data['2Theta'][PeaksTrue]/2 #divide by two because of twoTheta
    Theta_m_2 = Theta_m**2
    Theta_Critical = Data['2ThetaCritical']/2
    #Doing a linear fit
    #def LinearModel(x,y,thetaCritical,slope):
    #    return 
    
    #Plotting
    fig, ax = plt.subplots()
    ax.plot(m_2,Theta_m_2,'+')
    #Simple linear fit
    p = np.polyfit(m_2,Theta_m_2,1)
    x = np.linspace(min(m_2),max(m_2))
    y = np.polyval(p,x)
    ax.plot(x,y)
    plt.show()

    #Evaluating the thickness
    Cu_alpha_1 = 1.5406#ångstrom
    thickness = Cu_alpha_1/(2*(p[0]**0.5))
    print(thickness)
    print(p)
    #Evaluating thickness from Fourier Transform
    index = np.where((Data['2Theta'] <= range[1]) & (Data['2Theta'] >= range[0]))
    fig2, ax2 = plt.subplots()
    fourier = np.fft.fft(Data['Intensity'][index])
    fourierFreq = np.fft.fftfreq(Data['2Theta'][index].shape[-1])
    ax2.plot(fourierFreq,fourier.real,fourierFreq,fourier.imag)


    return Data

#Function to find the crytical angle
def CriticalAngle(Data, Range):
    #Specify a certain range where the critical angle is
    Index = np.where((Data['2Theta'] <= Range[1]) & (Data['2Theta'] >= Range[0]))
    gradient = np.gradient(Data['Intensity'][Index])#Calculating the gradient
    MaxGrad = max(abs(gradient))#Finding the maximum in the gradient
    MaxGradIndex = np.where(abs(gradient) == MaxGrad)    
    FinalIndex = Index[0][MaxGradIndex[0][0]]
    #Assigning the critical angle
    ThetaCritical = Data['2Theta'][FinalIndex]

    Data['2ThetaCritical'] = ThetaCritical

    return Data

