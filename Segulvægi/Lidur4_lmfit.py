import numpy as np 
import matplotlib.pyplot as plt 
import pdb
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from lmfit import Model

#Adjust axis size
plt.rcParams.update({'font.size': 18})

#Specifying type of model
def linear(x,a,b):
    return a*x + b

#Generating the model
gmodel = Model(linear)

filename = "Lidur4Data.txt"
#Import data
with open(filename) as f:
    content = f.readlines()

    f.close

#L = Iw
#Finna hverfitregdu
m = 141.55e-3#kg
R = 2.68e-2 #m
I = (2/5) * m * (R**2)
#Spola
R_spola = 0.103#meters
n_spola = 195
h_spola = 0.138#meters
mu0 = (4*np.pi)*1e-7

#Setup data
n = 19
Current = np.zeros(n)
Tidni = np.zeros(n)
Sveiflutimi = np.zeros(n)

for i in range(n):
    temp = content[i+5].split("\t")
    Current[i] = temp[0]
    Tidni[i] = temp[1]
    Sveiflutimi[i] = temp[3]

#Reikna naudsynlegar staerdir
#L = I*(Tidni*2*np.pi)#Hverfiþungi
L = 2*np.pi*I*Tidni#Hverfiþungi
VeltuTidni = (2*np.pi)/Sveiflutimi
#Segulsvid i spolu
B = (mu0*n_spola*Current*(R_spola**2))/((R_spola**2 + (h_spola/2)**2)**(3/2))
#Ovissa i Segulsvidi B
Current_error = 0.02
B_error = (mu0*n_spola*Current_error*(R_spola**2))/((R_spola**2 + (h_spola/2)**2)**(3/2))
print("Error i B:",B_error*1e3," [mT]")

#Error í B/L
B_L_error = (B/L)*(Current_error/Current + 0.004)
pdb.set_trace()
#Gera linulegt fit
#Fyrst fyrir I = 1A
result1 = gmodel.fit(VeltuTidni[0:4],x=B[0:4]/L[0:4],a=1,b=0)
print(result1.fit_report())
#Svo I = 2.0A
result2 = gmodel.fit(VeltuTidni[4:9],x=B[4:9]/L[4:9],a=1,b=0)
print(result2.fit_report())
#Svo I = 2.0A
result3 = gmodel.fit(VeltuTidni[9:14],x=B[9:14]/L[9:14],a=1,b=0)
print(result3.fit_report())
#Svo I = 2.0A
result4 = gmodel.fit(VeltuTidni[14:19],x=B[14:19]/L[14:19],a=1,b=0)
print(result4.fit_report())


#Trying different style
f, axs = plt.subplots(2, 2,figsize=(12,6.75))
#,gridspec_kw={'height_ratios': [3, 1]}
#I = 1A
label = "B = " + str(B[2]*1e-3)[0:4] + " [mT]"
axs[0,0].errorbar(B[0:4]/L[0:4],VeltuTidni[0:4],yerr=None,xerr=B_L_error[0:4],fmt='o',ms=8,label=label,c='#1f77b4')
axs[0,0].plot(B[0:4]/L[0:4], result1.best_fit, 'r-', label='_nolabel_')
#I = 2A
label = "B = " + str(2.73) + " [mT]"
axs[0,1].errorbar(B[4:9]/L[4:9],VeltuTidni[4:9],yerr=None,xerr=B_L_error[4:9],fmt='o',ms=8,label=label,c='#ff7f0e')
axs[0,1].plot(B[4:9]/L[4:9], result2.best_fit, 'r-', label='_nolabel_')
#I = 3A
label = "B = " + str(B[10]*1e-3)[0:4] + " [mT]"
axs[1,0].errorbar(B[9:14]/L[9:14],VeltuTidni[9:14],fmt='o',yerr=None,xerr=B_L_error[9:14],ms=8,label=label,c='#2ca02c')
axs[1,0].plot(B[9:14]/L[9:14], result3.best_fit, 'r-', label='_nolabel_')
#I = 3.5A
label = "B = " + str(4.78) + " [mT]"
axs[1,1].errorbar(B[14:19]/L[14:19],VeltuTidni[14:19],fmt='o',yerr=None,xerr=B_L_error[14:19],ms=8,label=label,c='#d62728')
axs[1,1].plot(B[14:19]/L[14:19], result4.best_fit, 'r-', label='_nolabel_')
axs[0,0].legend()
axs[0,1].legend()
axs[1,0].legend()
axs[1,1].legend()
axs[0,0].tick_params(right=True,top=True,direction='in',labelsize=24,size=14)
axs[0,1].tick_params(right=True,top=True,direction='in',labelsize=24,size=14)
axs[1,0].tick_params(right=True,top=True,direction='in',labelsize=24,size=14)
axs[1,1].tick_params(right=True,top=True,direction='in',labelsize=24,size=14)
#Residuals
#result1.plot_residuals(ax = ax2)
#result2.plot_residuals(ax = ax2)
#result3.plot_residuals(ax = ax2)
#result4.plot_residuals(ax = ax2)
#ax2legend = ax2.legend()
#ax2legend.remove()
#ax2.set_title("")
#ax2.set_ylabel("Leif")
#plt.xlabel(r"B/L [T$\cdot$s/kg$\cdot$m$^2$]")
#plt.ylabel(r"$\Omega_p$ [1/s]")
f.text(0.5, 0.005, r"B/L [T$\cdot$s/kg$\cdot$m$^2$]", ha='center',size=22)
f.text(0.04, 0.5, r"$\Omega_p$ [1/s]", va='center', rotation='vertical',size=22)
plt.savefig("Polvelta.png",dpi=300,bbox_inches="tight")
plt.show()