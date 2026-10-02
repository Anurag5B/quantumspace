# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 11:03:00 2026

@author: anuraag
"""
import numpy as np
import matplotlib.pyplot as plt

hbar = 1.05e-34
m = 0.511e6 * (1.602e-19) / (3e8)**2
e = 1.6e-19
epso = 8.85e-12

n = 1000
rmi = 1e-15
rma = 10e-10

for a in [3e-10, 5e-10, 7e-10]:
    r = np.linspace(rmi, rma, n)
    dr = r[1] - r[0]
    V = -e**2 / (4*np.pi*epso*r) * np.exp(-r/a)
    
    T = np.zeros((n, n))
    for i in range(n):
        T[i, i] = 2
        if i > 0:
            T[i, i-1] = -1
        if i < n-1:
            T[i, i+1] = -1
    T = T * hbar**2 / (2*m*dr**2)
    H = T + np.diag(V)

    E, psi = np.linalg.eigh(H)

    print("a =", a*1e10, "Angstrom")

    for j in range(3):
        E0 = E[j] / (1.602e-19)
        print("State", j+1, "Energy =", format(E0, ".3g"), "eV")

    for j in range(3):
        plt.plot(r*1e10, psi[:, j], label="State " + str(j+1))

    plt.xlabel("r (Angstrom)")
    plt.ylabel("Wavefunction")
    plt.title("Wavefunctions for a = " + str(a*1e10) + " Angstrom")
    plt.grid()
    plt.legend()
    plt.show()


    
    