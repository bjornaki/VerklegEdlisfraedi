import numpy as np 
import matplotlib.pyplot as plt 
import pdb

#Adjust axis size
plt.rcParams.update({'font.size': 22})

filename = "Lidur3.txt"
#Import data
with open(filename) as f:
    content = f.readlines()

    f.close

n = 9
Current = np.zeros(n)#Amperes
Massi = np.zeros(n)
Current_error = np.zeros(n)#Amperes
Length = np.zeros(n)
FjoldiLitlar = np.zeros(n)
FjoldiStorar = np.zeros(n)
massi_Kula = 141.55*1e-3


g = 9.82 #kg m/s^2
massi_litil = 0.48e-3#kg
massi_stor = 1.13e-3#kg

for i in range(n):
    temp = content[i+5].split("\t")
    Current[i] = temp[1]
    FjoldiLitlar[i] = temp[4]
    FjoldiStorar[i] = temp[6]
    Current_error[i] = temp[2]

Massi = FjoldiLitlar*massi_litil + FjoldiStorar*massi_stor + massi_Kula
dB_dz = 1.69e-2*Current
dB_dz_error = 1.69e-2*Current_error
pdb.set_trace()
#Fitting
p = np.polyfit(dB_dz[1:-1]/g,Massi[1:-1],1)
x = np.linspace(min(dB_dz/g),max(dB_dz/g))
y = np.polyval(p,x)
print(p[0], "Am^2")
#Evaluating error
maxUpper = np.polyfit(np.array([dB_dz[1]/g - dB_dz_error[1]/g,dB_dz[-1]/g + dB_dz_error[-1]/g]),np.array([Massi[1],Massi[-1]]),1)
print("Upper Max",maxUpper[0],"Am^2")
maxLower = np.polyfit(np.array([dB_dz[1]/g + dB_dz_error[1]/g,dB_dz[-1]/g - dB_dz_error[-1]/g]),np.array([Massi[1],Massi[-1]]),1)
print("Lower Max",maxLower[0],"Am^2")


#Plotting
fig, ax = plt.subplots(figsize=(12,6.75))
ax.errorbar(dB_dz[1:-1]/g,Massi[1:-1],yerr=None,xerr=dB_dz_error[1:-1]/g,fmt='o',ms=8)
ax.plot(x,y)
ax.set_xlabel(r"$\frac{dB/dz}{g}$ [T$\cdot$s$^2$/m$^2$]")
ax.set_ylabel("Massi [kg]")
ax.tick_params(right=True,top=True,direction='in',labelsize=24,size=14)
plt.ticklabel_format(scilimits=(-2,-2))
ax.grid(alpha=0.3)
plt.savefig("Heildarkraftur.png",format="png",dpi=300,bbox_inches="tight")
plt.show()
