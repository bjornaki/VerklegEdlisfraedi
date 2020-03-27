import numpy as np
import matplotlib.pyplot as plt
import pdb

#Adjust axis size
plt.rcParams.update({'font.size': 18})

def Au(fig=None, PlotSelect=None, Vz=None, axes=None, axesNo=0):
    Maeligogn = 'Maeligogn_Au_headon/'


    # Góð gögn fyrir tímagraf
    # 37, 44, 49, 51, 52, 61, 73, 79, 86, 90, 92, 100, 108, 110


    V0 = 0.1014  # power supply voltage
    R = 1000  # Resistor value
    Vz = -4e-4  # offset voltage on the scope, often different between measurements
    Iz = Vz/R  # offset current calculated form the resistance

    # Picking which datafile to load
    Number = np.arange(111)
    print(Number)
    # Picking which dataset to plot
    PlotSelect = 61

    # Select which data to include in histogram
    # Can be vector with the number of filenames
    # HistSelect = [1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 17, 18, 19, 21, 22, 24, 25];

    HistSelect = Number

    # Error checking that PlotSelect is a valid filename number
    if PlotSelect < min(Number) or max(Number) < PlotSelect:
        print('Please check that PlotSelect is a valid filename number')


    # Error checking that all HistSelect is a valid filename number

    for k in HistSelect:
        if k not in Number:
            print('Please check that all HistSelect correspond to a valid filename number')

    # Preallocate

    T = [np.array([])] * len(Number)
    VR = [np.array([])] * len(Number)
    I = [np.array([])] * len(Number)
    G = [np.array([])] * len(Number)



    # Load all datafiles
    for i in range(len(Number)):
        filename = Maeligogn + 'scope_' + str(Number[i]) + '.csv'

        f = open(filename, 'r')

        line = f.readline()

        while line:
            if 'axis' in line or 'second' in line:
                line = f.readline()
                continue

            line = line.split(',')

            T[i] = np.append(T[i], float(line[0]))
            VR[i] = np.append(VR[i], float(line[1]) - Vz)

            line = f.readline()

        I[i] = (1/R) * VR[i] - Iz
        G[i] = (VR[i]/R) / (V0 - VR[i])

    # Find index of filenumers we want to plot
    PS = np.where(Number == PlotSelect)[0][0]

    G0 = 7.7498e-5

    HS = np.arange(len(HistSelect))
    TOT = np.array([])
    TOT_G = np.array([])

    # Find index of filename number in HistSelect

    for i in range(len(HistSelect)):
        HS[i] = int(np.where(Number == HistSelect[i])[0][0])

    # All Current and Conductance values appended together

    for i in range(len(HS)):

        TOT = np.append(TOT, I[HS[i]])
        TOT_G = np.append(TOT_G, G[HS[i]])


    def fig1():
        # figure 1 is Current vs Time

        plt.plot(T[PS], I[PS])

        plt.xlabel('Time [s]')
        plt.ylabel('Current [A]')

        plt.axis([min(T[PS]), max(T[PS]), -2e-6, 8e-5])

        # Add expected lines

        for n in range(1, 25):
            In = V0 / (R + 12.9e3/n)  # E3 in matlab code???
            plt.plot([min(T[PS]), max(T[PS])], [In, In], 'r')

        In = V0 / (R + 12.9e3 / 24)
        plt.plot([min(T[PS]), max(T[PS])], [In, In], 'r', label=r'$G_n$')
        plt.legend()



    def fig2():
        # Plot using determined conductance values of the nanowire 2e^2/h (G0)

        plt.plot(T[PS], G[PS]/G0, 'b')

        plt.xlabel('Time [s]')
        plt.ylabel('Conductance [2e^2/h]')

        for n in range(1, 25):
            plt.plot([min(T[PS]), max(T[PS])], [n, n])

        plt.axis([min(T[PS]), max(T[PS]), -1, 20])



    def fig3():

        # Figure 3 is a histogram from the Current data

        binrange = np.array([-1e-5, 1e-4])
        # Select the bin width for the Current data and calculate number of bins
        BW = 8e-7
        bins = int((binrange[1]-binrange[0])/BW)
        
        plt.hist(TOT, bins=bins, range=(binrange[0], binrange[1]))

        plt.xlabel('Current [A]')
        plt.ylabel('Occurrence [Counts]')

        for n in range(1, 25):
            I = (V0/R) / (1 + (12.9e3/R)/n)
            plt.plot([I, I], [0, 100])


    def fig4(axes=axes,axSelect = axesNo):
        # Figure 4 is a histogram from the Conductance data
        if axes==None:
            fig4, (ax1, ax2, ax3) = plt.subplots(1,3,sharey=True, sharex=True,figsize=(16,5))
            fig4.add_subplot(111, frameon=False)
            plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
        # Select the bin width for the Current data and calculate number of bins
        binrange = np.array([-1, 12])#range of the bins
        BW = 0.1 #Binwidth
        bins = int((binrange[1]-binrange[0])/BW)#Defines how many lines are plotted in the histogram
        ax1.hist(TOT_G/G0, bins=bins, range=binrange, align='right',edgecolor='b',alpha=0.7)
        #ax1.set_xlabel(r'Leiðni [2e$^2$/h]')
        #ax1.set_ylabel('Tíðni [fjöldi]')

        Height = np.array([710,440,420,300,310,190,280])
        #Adding expected lines for the expected data
        for n in range(1, 8):
            ax1.plot([n, n], [0, 1000],'r--')

        ax1.axis([-0.5, 8, 0, 1000])

        ax1.text(1.1,800,"A",size=24)
        ax1.set_xticks([0,1,2,3,4,5,6,7,8])
        ax1.tick_params(right=True,top=True,direction='in',labelsize=20,size=14)

        return fig4, ax1, ax2, ax3


    #fig1()
    #plt.show()

    #fig2()
    #plt.show()

    #fig3()
    #plt.show()

    
    plt.savefig("Au_Cond_Histogram.png",format="png",dpi=300,bbox_inches="tight")


    if fig == 1:
        fig1()
    elif fig == 2:
        fig2()
    elif fig == 3:
        fig3()
    elif fig == 4:
        fig4, ax1, ax2, ax3 = fig4()


    return fig4, ax1, ax2, ax3

