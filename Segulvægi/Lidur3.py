import numpy as np 
import matplotlib.pyplot as plt 

filename = "Lidur3.txt"
#Import data
with open(filename) as f:
    content =f.readlines()

    f.close

n = 7
Current = np.zeros(n)#Amperes
M = np.zeros(n)#cm
Current_error = np.zeros(n)#Amperes

massi_litil = 0.48#gr
massi_stor = 1.13#gr

for i in range(n):
    temp = content[i+13].split("\t")
    Current[i] = temp[1]
    Length[i] = temp[0]
    Current_error[i] = temp[2]

