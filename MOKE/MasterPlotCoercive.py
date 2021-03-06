import numpy as np 
import matplotlib.pyplot as plt 
import pdb 
#Import three samples
import CoAlZr as CAZ 
import PY_MgO_300C as PY300 
import PY_MgO_400C as PY400 
#Close all figures
plt.close("all")
#Adjust axis size
plt.rcParams.update({'font.size': 14})

#Create master plot for Magnetic Remanence
fig = plt.figure(figsize=(15,5))
ax1 = plt.subplot(131, projection='polar')
ax2 = plt.subplot(132, projection='polar')
ax3 = plt.subplot(133, projection='polar')

#Adding to plot
fig, ax1 = CAZ.CoAlZr(fig,ax1,CoercField=True)
fig, ax2 = PY300.PY300C(fig,ax2,CoercField=True)
fig, ax3 = PY400.PY400C(fig,ax3,CoercField=True)
fig.tight_layout()#lagar spacing milli subplot
plt.savefig("CoercFieldAllThree.png",format="png",dpi=300,bbox_inches="tight")
plt.show()