import numpy as np 
import matplotlib.pyplot as plt 
import pdb 
#Import three samples
import CoAlZr as CAZ 
import PY_MgO_300C as PY300 
import PY_MgO_400C as PY400 

#Create master plot for Magnetic Remanence
fig = plt.figure(figsize=(15,5))
ax1 = plt.subplot(131, projection='polar')
ax2 = plt.subplot(132, projection='polar')
ax3 = plt.subplot(133, projection='polar')

#Adding to plot
fig, ax1 = CAZ.CoAlZr(fig,ax1,MagRemBool=True)
plt.show()