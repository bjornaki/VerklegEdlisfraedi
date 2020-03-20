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
    Current[i] = float(temp[0])*1e3
    Length[i] = float(temp[1])*1e3
    Current_error[i] = float(temp[2])*1e3

mu0 = 1.257e-6  # [T m / A]
n = 195  # turns
R = 0.103  # Radius [m]
h = 0.138  # Distance [m]

B = mu0 * n * Current * R ** 2 / (R ** 2 + (h / 2) ** 2) ** (3 / 2)
B_error = mu0 * n * Current_error * R ** 2 / (R ** 2 + (h / 2) ** 2) ** (3 / 2)

Length = Length * 0.01  # m
m = 1.36e-3  # kg
g = 9.82  # m/s^2

# check for gradient error
max_grad = (Length[-1] - Length[0]) / (B[-1] + B_error[-1] - (B[0] - B_error[0]))
min_grad = (Length[-1] - Length[0]) / (B[-1] - B_error[-1] - (B[0] + B_error[0]))


print('Gradient error: ', (min_grad-max_grad) * m * g)

# Fitting
p = np.polyfit(B, Length, 1)
x = np.linspace(min(B)-0.1, max(B)+0.1)
y = np.polyval(p, x)

# Plotting
fig, ax = plt.subplots()
plt.errorbar(B, Length, xerr=B_error, fmt='o')
ax.plot(x, y)
plt.xlabel("B [mT]", size=20)
plt.ylabel("r [mm]", size=20 )

plt.tick_params(right=True, top=True, direction='in', labelsize=24, size=14)
plt.grid(alpha=0.3)


print("Magnetic Moment", p[0] * m * g)

m_bar = 0.90e-3  # kg
l_bar = 3.91e-2  # m

print('shift from bar: ' + str(-0.5 * m_bar * l_bar / m))

plt.savefig('lidur1.png', format='png', dpi=300, bbox_inches='tight')
plt.show()
