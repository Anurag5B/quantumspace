# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 11:21:03 2026

@author:anuraag
"""
import numpy as np
import matplotlib.pyplot as plt

n = 100

xmin = -5
xmax = 5

x = np.linspace(xmin, xmax, n)
dx = x[1] - x[0]

V = 0.5 * x**2
a = np.zeros((n, n))

for i in range(n):
    for j in range(n):

        if i == j:
            a[i, j] = -2
        elif abs(i - j) == 1:
            a[i, j] = 1

H = -(1 / (2 * dx**2)) * a + np.diag(V)

energy, wavefunction = np.linalg.eigh(H)

print("Energy levels:")

for i in range(5):
    print("E", i+1, "=", energy[i])

for i in range(3):
    psi = wavefunction[:, i]
    plt.plot(x, psi, label="n = " + str(i))
    
plt.xlabel("x")
plt.ylabel("Wavefunction")
plt.legend()
plt.grid()
plt.show()

