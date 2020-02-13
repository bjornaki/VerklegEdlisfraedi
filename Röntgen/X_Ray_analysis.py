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
def PlotData(Data, fig, ax, yaxis = "log", XRR = False, Filtered = False, ThetaCr = False, showPeaks = False, shift = False,shiftVal = 0,scanAxis = "2Theta"):
    if fig == None:
        fig, ax = plt.subplots()
    if shift:
        ax.plot(Data['2Theta'],Data['Intensity']*shiftVal,label=Data['Filename'][0:6])
    else:
        ax.plot(Data['2Theta'],Data['Intensity'],label=Data['Filename'][0:6])
    ax.grid(alpha=0.3)
    if scanAxis == "2Theta":
        ax.set_xlabel(r"2$\theta$ [deg]")
    elif scanAxis == "Phi":
        ax.set_xlabel(r"$\phi$ [deg]")
    ax.set_ylabel("cps")
    if yaxis == "log":
        plt.yscale("log")

    if showPeaks == True:
        ax.plot(Data['2Theta'][Data['Peaks']],Data['Intensity'][Data['Peaks']],'*')
    if Filtered == True:
        ax.plot(Data['2Theta'],Data['IntensFiltered'])
    if ThetaCr == True:
        ax.axvline(x=Data['2ThetaCritical'])

    #specify xrange
    ax.set_xlim([min(Data['2Theta']),max(Data['2Theta'])])

    #Specify ticks
    plt.tick_params(right=True, top=True, direction='in', labelsize=18, size=14)

    return fig, ax

# test

#Function to get the film thickness
def FilmThickness(Data, range):
    #Filter Data for reference
    FilteredIntens = savgol_filter(Data['Intensity'],7,3)
    #Finding peaks
    peaks = find_peaks_cwt(FilteredIntens,np.arange(0.1,0.5,0.1))

    Data['IntensFiltered'] = FilteredIntens#Appending filtered intensity
    #Data['Peak properties'] = properties

    PeaksInRangeIndex = np.where((Data['2Theta'][peaks] <= range[1]) & (Data['2Theta'][peaks] >= range[0]))
    PeaksTrue = peaks[PeaksInRangeIndex[0]]#The peaks within the specified range
    m = np.arange(1,len(PeaksTrue)+1,1)#Number of peaks for use with thickness model
    m_2 = m**2#m squared
    TwoTheta_m = Data['2Theta'][PeaksTrue]
    Theta_m = TwoTheta_m/2
    Theta_m = np.deg2rad(Theta_m)
    #divide by two because of twoTheta
    Theta_m_2 = Theta_m**2
    Theta_Critical = Data['2ThetaCritical']/2
    #Doing a linear fit
    #def LinearModel(x,y,thetaCritical,slope):
    #    return 
    Data['Peaks'] = PeaksTrue
    
    #Plotting
    fig, ax = plt.subplots()
    ax.plot(m_2,Theta_m_2,'+')
    #Simple linear fit
    p = np.polyfit(m_2,Theta_m_2,1)
    x = np.linspace(min(m_2),max(m_2))
    y = np.polyval(p,x)
    ax.plot(x,y)
    ax.set_xlabel(r"$m^2$")
    ax.set_ylabel(r"$\theta_m^2$")
    plt.show()

    #Evaluating the thickness
    Cu_alpha_1 = 0.15406#nm
    slope = p[0]
    thickness = Cu_alpha_1/(2*(np.sqrt(slope)))
    print(thickness, "[nm]")
    #Evaluating thickness from Fourier Transform
    index = np.where((Data['2Theta'] >= Theta_Critical))
    Theta_use = Data['2Theta'][index]
    q_s = 4*np.pi/Cu_alpha_1*(np.cos(Theta_Critical*np.pi/180)**2-np.cos(Theta_use*np.pi/180)**2)**0.5
    fourier = np.fft.fft(Data['Intensity'][index])
    fourierFreq = np.fft.fftfreq(Data['2Theta'][index].shape[-1])
    #ax2.plot(fourierFreq,fourier.real,fourierFreq,fourier.imag)


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

