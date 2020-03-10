import numpy as np 
import matplotlib.pyplot as plt 
import pdb

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


g = 9.82 #kg m/s^2
massi_litil = 0.48e-3#kg
massi_stor = 1.13e-3#kg

for i in range(n):
    temp = content[i+5].split("\t")
    Current[i] = temp[1]
    FjoldiLitlar[i] = temp[4]
    FjoldiStorar[i] = temp[6]
    Current_error[i] = temp[2]

Massi = FjoldiLitlar*massi_litil + FjoldiStorar*massi_stor
dB_dz = 1.69e-2*Current

#Fitting
p = np.polyfit(dB_dz[1:-1]/g,Massi[1:-1],1)
x = np.linspace(min(dB_dz/g),max(dB_dz/g))
y = np.polyval(p,x)
print(p, "Am^2")

#Plotting
fig, ax = plt.subplots()
ax.plot(dB_dz/g,Massi,'+',ms=15)
ax.plot(x,y)
plt.show()
