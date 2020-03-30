import numpy as np 
import matplotlib.pyplot as plt 
import pdb

from plot_osc_data_Histogram_Au import Au 
from plot_osc_data_Histogram_Cu import Cu
from plot_osc_data_Histogram_PtIr import PtIr


fig, ax1, ax2, ax3 = Au(fig=4,axesNo=1)
fig, ax1, ax2, ax3 = Cu(fig=4,axes1=ax1,axes2=ax2,axes3=ax3,axesNo=1)
fig, ax1, ax2, ax3 = PtIr(fig=4,axes1=ax1,axes2=ax2,axes3=ax3,axesNo=1)
#ax4_2 = Cu(fig=4)

plt.xlabel(r'Leiðni [2e$^2$/h]')
plt.ylabel('Tíðni [fjöldi]')
#pdb.set_trace()

#fig.text(0.5, 0.01, r'Leiðni [2e$^2$/h]', ha='center')
#fig.text(0.01, 0.5, 'Tíðni [fjöldi]', va='center', rotation='vertical')


plt.savefig("HistogramsAll.png",format="png",dpi=300,bbox_inches="tight")

#plt.close("all")

#fig, (ax1, ax2, ax3) = plt.subplots(1,3,sharey=True, sharex=True,figsize=(10,5))
#ax1 = Au(fig=4)
#plt.show(fig)
