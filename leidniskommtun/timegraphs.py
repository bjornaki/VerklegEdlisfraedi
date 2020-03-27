import numpy as np
import matplotlib.pyplot as plt

from plot_osc_data_Au import Au
from plot_osc_data_Cu import Cu
from plot_osc_data_PtIr import PtIr


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
# plt.legend(fontsize=24, loc='lower left')
#
# plt.axis([0, 60, 0, 60])  # PtIr
# plt.axis([0, 30, 0, 60])  # Cu
# plt.axis([0, 50, 0, 60])  # Au
# plt.axis([0, 50, 0, 60])
#
# plt.savefig("Current_vs_Time_PtIr.png", format="png", bbox_inches="tight")
# plt.savefig("Current_vs_Time_Cu.png", format="png", bbox_inches="tight")
# plt.savefig("Current_vs_Time_Au.png", format="png", bbox_inches="tight")
# plt.savefig("Current_vs_Time.png", format="png", bbox_inches="tight")



Au(fig=2, PlotSelect=37)
Cu(fig=2, PlotSelect=71)
PtIr(fig=2, PlotSelect=25)

plt.xlabel(r'Tími [$\mu s$]', size=24)
plt.ylabel(r'Leiðni [$ 2e^2/h $]', size=24)
plt.tick_params(right=True, top=True, direction='in', labelsize=24, size=14, which='major', bottom=True)
plt.legend(fontsize=24, loc='upper right')
plt.axis([0, 50, 0, 25])

plt.savefig("Conductance_vs_Time.png", format="png", bbox_inches="tight")


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

plt.show()
