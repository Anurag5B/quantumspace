# -*- coding: utf-8 -*-
"""
Created on Thu Oct 8 10:24:50 2026

@author: anuraag
"""
import numpy as np
import matplotlib.pyplot as plt

n = 100
hbar = 197.3
m = 940.0
k = 100.0

r = np.linspace(0, 10, n)
dr = r[1] - r[0]

a = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        if i == j:
            a[i, j] = -2
        elif abs(i - j) == 1:
            a[i, j] = 1
            
r = r[1:-1]
a = a[1:-1, 1:-1]

for b in [0, 10, 30]:
    V = 0.5 * k * r**2 + (b / 3) * r**3
    H = -(hbar**2 / (2 * m * dr**2)) * a + np.diag(V)
    energy, wavefunction = np.linalg.eigh(H)

    E0 = energy[0]
    psi = wavefunction[:, 0] 
    psi = psi / np.sqrt(np.sum(psi**2) * dr)

    print("b =", b, "MeV")
    print("ground state energy =", round(E0, 3), "MeV")

    plt.plot(r, psi, label="b = " + str(b))

plt.xlabel("r (fm)")
plt.ylabel("wavefunction u(r)")
plt.title("anharmonic oscillator")
plt.legend()
plt.grid()
plt.show()
