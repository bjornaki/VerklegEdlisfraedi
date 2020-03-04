import numpy as np 
import matplotlib.pyplot as plt 

filename = "Lidur2.txt"

#Import data
with open(filename) as f:
    content = f.readlines()

    f.close

n = 10
Current = np.zeros(n)#Amperes
t_10 = np.zeros(n)#cm
Current_error = np.zeros(n)#Amperes
T = np.zeros(n)

m = 141.55 #g
m = m*10e-3 #kg
R = 2.68 #cm
R = R*10e-2 #m
#Reikna hverfitregdu, I = 2/5m*R**2
I = (2/5)*m*(R**2)

for i in range(n):
    temp = content[i+7].split("\t")
    Current[i] = temp[0]
    t_10[i] = temp[1]
    T[i] = t_10[i]/10
    Current_error[i] = temp[3]


#Plotting
fig, ax = plt.subplots()
ax.plot(I/Current,T**2,'+')
plt.show()
