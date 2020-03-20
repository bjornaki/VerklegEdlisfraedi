import numpy as np
import matplotlib.pyplot as plt


def get_data(name):
    f = open(name, 'r')

    line = f.readline()

    bias = []
    cap1 = []
    cond1 = []

    while line:
        if '%' in line:
            line = f.readline()
            continue
        line = line.split()
        bias.append(float(line[0]))
        cap1.append(float(line[2]))
        cond1.append(float(line[3]))
        line = f.readline()

    return np.array(bias), np.array(cap1), np.array(cond1)


def plot(name, which='both'):
    bias, cap1, cond1 = get_data(name)

    if which in ['both', 'cond']:
        plt.plot(bias, cond1)
        plt.tick_params(right=True, top=True, direction='in', labelsize=18,
                        size=14, axis='y', bottom=False)
        plt.xlabel('Bias [V]')
        plt.ylabel('Conductance [S/Hz]')
        plt.grid(alpha=0.3)

        plt.show()

    if which in ['both', 'cap']:
        plt.plot(bias, cap1)
        plt.xlabel('Bias [V]')
        plt.ylabel('Capacitance [F]')
        plt.tick_params(right=True, top=True, direction='in', labelsize=18,
                        size=14, axis='y', bottom=False)

        plt.grid(alpha=0.3)
        plt.show()


def get_depth(name):

    V, C, cond = get_data(name)

    q = 1.60217662e-19  # C
    e_0 = 8.85418782e-12  # m-3 kg-1 s4 A2
    e_r = 11.68  # Si

    N_A = np.zeros(len(C)-2)
    for i in range(len(C)-2):
        deriv = (1/C[i+2]**2 - 1/C[i]**2)/(V[i+2] - V[i])
        N_A[i] = 2 / (q * e_r * e_0 ** 2 * deriv)

    A = np.pi*1.5e-3**2
    x = e_r * e_0 * A / C[1:-1]

    # plt.plot(x*10e6, -N_D*10e-6, "*")
    # plt.xlabel('x [$\mu m$]')
    # plt.ylabel('$-N_D$ [$cm^{-3}$]')
    # plt.show()
    # plt.plot(V, 1 / C ** 2)
    # plt.xlabel('Bias [V]')
    # plt.ylabel('$C^{-2}$ $[F^{-2}]$')
    # plt.show()
    return x*10e6, -N_A*10e-6

plot('data1.txt')

x1, y1 = get_depth('data1.txt')
x2, y2 = get_depth('data2.txt')
x3, y3 = get_depth('data3.txt')

plt.plot(x1, y1, '*', label='Fyrir bökun')
plt.plot(x2, y2, '^', label='Eftir fyrstu bökun')
plt.plot(x3, y3, 's', label='Eftir aðra bökun')
plt.xlabel('x [$\mu m$]', fontsize=18)
plt.ylabel('$N_A-N_D$ [$cm^{-3}$]', fontsize=18)

plt.tick_params(right=True, top=True, direction='in', labelsize=22, size=14, which='major', bottom=True)
plt.legend(fontsize=18)
plt.savefig("profile.png", format="png", bbox_inches="tight")
plt.show()
