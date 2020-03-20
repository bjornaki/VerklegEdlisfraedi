import numpy as np 
import matplotlib.pyplot as plt 
import pdb

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


#Gera linulegt fit
#Straumur = 1A
p1 = np.polyfit(B[0:4]/L[0:4],VeltuTidni[0:4],1)
x1 = np.linspace(min(B/L)-1,max(B/L)+1)
y1 = np.polyval(p1,x1)
segulvaegi1 = p1[0]
print("Svið:", B[2],"segulvaegi:",segulvaegi1,"Am^2")
#Straumur = 2A
p2 = np.polyfit(B[4:9]/L[4:9],VeltuTidni[4:9],1)
x2 = np.linspace(min(B/L),max(B/L))
y2 = np.polyval(p2,x2)
segulvaegi2 = p2[0]
print("Svið:", B[5],"segulvaegi:",segulvaegi2,"Am^2")
#Straumur = 3A
p3 = np.polyfit(B[9:14]/L[9:14],VeltuTidni[9:14],1)
x3 = np.linspace(min(B/L),max(B/L))
y3 = np.polyval(p3,x3)
segulvaegi3 = p3[0]
print("Svið:", B[10],"segulvaegi:",segulvaegi3,"Am^2")
#Straumur = 3.5A
p4 = np.polyfit(B[14:19]/L[14:19],VeltuTidni[14:19],1)
x4 = np.linspace(min(B/L),max(B/L))
y4 = np.polyval(p4,x4)
segulvaegi4 = p4[0]
print("Svið:", B[15],"segulvaegi:",segulvaegi4,"Am^2")


#Plotting
fig, axs = plt.subplots(2,2)
#Straumur = 1A
label = "B = " + str(B[2])[0:8] + " [T]"
axs[0,0].plot(B[0:4]/L[0:4],VeltuTidni[0:4],'+',label=label,ms=15)
axs[0,0].plot(x1,y1,label="_nolabel_")
#Straumur = 2A
label = "B = " + str(B[5])[0:8] + " [T]"
axs[0,1].plot(B[4:9]/L[4:9],VeltuTidni[4:9],'+',label=label,ms=15)
axs[0,1].plot(x2,y2,label="_nolabel_")
#Straumur = 3A
label = "B = " + str(B[10])[0:8] + " [T]"
axs[1,0].plot(B[9:14]/L[9:14],VeltuTidni[9:14],'+',label=label,ms=15)
axs[1,0].plot(x3,y3,label="_nolabel_")
#Straumur = 3.5A
label = "B = " + str(B[15])[0:8] + " [T]"
axs[1,1].plot(B[14:19]/L[14:19],VeltuTidni[14:19],'+',label=label,ms=15)
axs[1,1].plot(x4,y4,label="_nolabel_")
#Stilla plot
axs[0,0].set_xlabel(r"$\frac{B}{L}$")
axs[0,0].set_ylabel(r"$\Omega_p [\frac{rad}{s}]$ [Eining]")
axs[0,0].legend()
#axs[0,0].set_xlim([0,4])
plt.show()