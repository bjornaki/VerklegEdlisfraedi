import numpy as np
import matplotlib.pyplot as plt

Maeligogn = 'Maeligogn_Cu_headon/'

V0 = 0.1014  # power supply voltage
R = 1000  # Resistor value
Vz = -4e-4  # offset voltage on the scope, often different between measurements
Iz = Vz/R  # offset current calculated form the resistance

# Picking which datafile to load
Number = np.arange(41)

# Picking which dataset to plot
PlotSelect = 25

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


def fig2():
    # Plot using determined conductance values of the nanowire 2e^2/h (G0)

    plt.plot(T[PS], G[PS]/G0, 'b')

    plt.xlabel('Time [s]')
    plt.ylabel('Conductance [2e^2/h]')

    for n in range(1, 25):
        plt.plot([min(T[PS]), max(T[PS])], [n, n])


def fig3():

    # Figure 3 is a histogram from the Current data

    binrange = np.array([-1e-5, 1e-4])
    # Select the bin width for the Current data and calculate number of bins
    BW = 8e-7
    bins = int((binrange[1]-binrange[0])/BW)
    print(bins)

    plt.hist(TOT, bins=bins, range=(binrange[0], binrange[1]))

    plt.xlabel('Current [A]')
    plt.ylabel('Occurrence [Counts]')

    for n in range(1, 25):
        I = (V0/R) / (1 + 12.9e3/R)
        plt.plot([I, I], [0, 100])


def fig4():
    # Figure 4 is a histogram from the Conductance data

    # Select the bin width for the Current data and calculate number of bins
    binrange = np.array([-1, 12])
    BW = 0.1
    bins = int((binrange[1]-binrange[0])/BW)

    plt.hist(TOT_G/G0, bins=bins, range=binrange)
    plt.xlabel('Conductance [2e^2/h]')
    plt.ylabel('Occurrence [Counts]')

    for n in range(1, 25):
        plt.plot([n, n], [0, 100])

    plt.axis([-0.5, 8, 0, 1000])


fig1()
plt.show()

fig2()
plt.show()

fig3()
plt.show()

fig4()
plt.show()




