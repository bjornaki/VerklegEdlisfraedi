import numpy as np
import matplotlib.pyplot as plt

from plot_osc_data_Au_DD import Au
from plot_osc_data_Cu_DD import Cu
from plot_osc_data_PtIr_DD import PtIr


# Góð gögn fyrir tímagraf
# ps = [37, 44, 49, 51, 52, 61, 73, 79, 86, 90, 92, 100, 108, 110]
# ps = [37]
# for i in ps:
#     print(i)
#     Au(fig=1, PlotSelect=i)
#     plt.show()


# Góð mæligögn fyrir tímagraf
# ps = [56, 57, 71, 83]
# ps = [71]
#
# for i in ps:
#     Cu(fig=1, PlotSelect=i)

# Góðar skrár fyrir tímagraf: 16, 25, Sérstaklega 25

# ps = [16, 25]
# ps = [25]
# for i in ps:
#     PtIr(fig=1, PlotSelect=i)


# Au(fig=1, PlotSelect=37)
# Cu(fig=1, PlotSelect=71)
# PtIr(fig=1, PlotSelect=25)
#
# plt.xlabel(r'Tími [$\mu s$]', size=24)
# plt.ylabel(r'Straumur [$ \mu A$]', size=24)
# plt.tick_params(right=True, top=True, direction='in', labelsize=24, size=14, which='major', bottom=True)
# plt.legend(fontsize=24, loc='upper right')
#
# plt.axis([0, 60, 0, 60])  # PtIr
# plt.axis([0, 30, 0, 60])  # Cu
# plt.axis([0, 50, 0, 60])  # Au
# plt.axis([0, 50, 0, 65])

# plt.savefig("Current_vs_Time_PtIr.png", format="png", bbox_inches="tight")
# plt.savefig("Current_vs_Time_Cu.png", format="png", bbox_inches="tight")
# plt.savefig("Current_vs_Time_Au.png", format="png", bbox_inches="tight")
# plt.savefig("Current_vs_Time_null.png", format="png", bbox_inches="tight")
#
# plt.show()
#
# Au(fig=2, PlotSelect=37)
# Cu(fig=2, PlotSelect=71)
# PtIr(fig=2, PlotSelect=25)
#
# plt.xlabel(r'Tími [$\mu s$]', size=24)
# plt.ylabel(r'Leiðni [$ 2e^2/h $]', size=24)
# plt.tick_params(right=True, top=True, direction='in', labelsize=24, size=14, which='major', bottom=True)
# plt.legend(fontsize=24, loc='upper right')
# plt.axis([0, 50, 0, 25])
#
# plt.savefig("Conductance_vs_Time_null.png", format="png", bbox_inches="tight")


# Test offset
#
# for Vz in np.linspace(-4e-4, -4e-3, 5):
#     print(Vz)
#     Au(fig=1, PlotSelect=37, Vz=Vz)
#
#     plt.xlabel(r'Tími [$\mu s$]', size=24)
#     plt.ylabel(r'Straumur [$ \mu A$]', size=24)
#     plt.tick_params(right=True, top=True, direction='in', labelsize=24, size=14, which='major', bottom=True)
#     plt.legend(fontsize=24, loc='lower left')
#
#     plt.axis([0, 50, 0, 60])

# plt.show()



# --------------------HIST---------------------------



TOT_G = Au()

TOT_G = np.append(TOT_G, Cu())
TOT_G = np.append(TOT_G, PtIr())

G0 = 7.7498e-5

# Select the bin width for the Current data and calculate number of bins
binrange = np.array([-1, 12])  # range of the bins
BW = 0.05  # Binwidth
bins = int((binrange[1] - binrange[0]) / BW)  # Defines how many lines are plotted in the histogram
plt.hist(TOT_G / G0, bins=bins, range=binrange, align='right', edgecolor='b', alpha=0.7)
plt.xlabel(r'Leiðni [2e$^2$/h]')
plt.ylabel('Tíðni [fjöldi]')

Height = np.array([710, 440, 420, 300, 310, 190, 280])
# Adding expected lines for the expected data
for n in range(1, 8):
    plt.plot([n, n], [0, Height[n - 1]], color='r')

plt.axis([-0.5, 8, 0, 1500])

plt.text(1.3, 800, "A", size=22)
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8])
plt.tick_params(right=True, top=True, direction='in', labelsize=20, size=14)


plt.show()