# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 12:14:30 2026

@author: anuraag
"""

import numpy as np
import matplotlib.pyplot as plt

n = 100
hbar = 1973.0
m = 940e6
D = 0.755501
alpha = 1.44
r0 = 0.131349

r = np.linspace(0.01, 1.0, n)
dr = r[1] - r[0]

a = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        if i == j:
            a[i, j] = -2
        elif abs(i - j) == 1:
            a[i, j] = 1

V = D * (np.exp(-2 * alpha * (r-r0))
         - 2 * np.exp(-alpha * (r-r0)))

H = -(hbar**2 / (2 * m * dr**2)) * a + np.diag(V)
energy, wavefunction = np.linalg.eigh(H)

E0 = energy[0]
psi = wavefunction[:,0]
psi = psi / np.max(abs(psi))

print("Ground state energy =", format(E0, ".3g"), "eV")

plt.plot(r, psi)
plt.xlabel("r (Angstrom)")
plt.ylabel("Wavefunction")
plt.title("Morse Potential")
plt.grid()
plt.show()