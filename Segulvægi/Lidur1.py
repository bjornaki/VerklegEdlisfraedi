import numpy as np 
import matplotlib.pyplot as plt 

filename = "Lidur1.txt"
#Import data
with open(filename) as f:
    content =f.readlines()

    f.close

n = 7
Current = np.zeros(n)#Amperes
Length = np.zeros(n)#cm
Current_error = np.zeros(n)#Amperes

for i in range(n):
    temp = content[i+13].split("\t")
    Current[i] = temp[0]
    Length[i] = temp[1]
    Current_error[i] = temp[2]

#Fitting
p = np.polyfit(Current,Length,1)
x = np.linspace(min(Current),max(Current))
y = np.polyval(p,x)

#Plotting
fig, ax = plt.subplots()
plt.errorbar(Current,Length,yerr=Current_error,fmt='+')
ax.plot(x,y)
plt.show()

print("Magnetic Moment", p[0])