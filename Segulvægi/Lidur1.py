import numpy as np
import matplotlib.pyplot as plt

filename = "Lidur1.txt"
# Import data
with open(filename) as f:
    content = f.readlines()

    f.close

n = 7
Current = np.zeros(n)  # Amperes
Length = np.zeros(n)  # cm
Current_error = np.zeros(n)  # Amperes

for i in range(n):
    temp = content[i + 13].split("\t")
    Current[i] = temp[0]
    Length[i] = temp[1]
    Current_error[i] = temp[2]

mu0 = 1.257e-6  # [T m / A]
n = 195  # turns
R = 0.103  # Radius [m]
h = 0.138  # Distance [m]

B = mu0 * n * Current * R ** 2 / (R ** 2 + (h / 2) ** 2) ** (3 / 2)
Length = Length * 0.01  # m

# Fitting
p = np.polyfit(B, Length, 1)
x = np.linspace(0, max(B))
y = np.polyval(p, x)

# Plotting
fig, ax = plt.subplots()
plt.errorbar(B, Length, fmt='+')
ax.plot(x, y)
plt.xlabel("Segulsvið [T]", size=18)
plt.ylabel("Lengd [m]", size=18)

plt.tick_params(right=True, top=True, direction='in', labelsize=18, size=14)
plt.grid(alpha=0.3)

m = 1.36e-3  # kg
g = 9.82  # m/s^2
print("Magnetic Moment", p[0] * m * g)

m_bar = 0.90e-3  # kg
l_bar = 3.91e-2  # m

print(Current)
print(B)
print('shift from bar: ' + str(-0.5 * m_bar * l_bar / m))

plt.show()
