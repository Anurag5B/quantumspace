# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 10:57:37 2026

@author: anuraag
"""
import numpy as np
import matplotlib.pyplot as plt

n = 100
hbar = 1.0
m = 1.0
L = 2.0         
V0 = 10.0        

x = np.linspace(-3, 3, n)
dx = x[1] - x[0]

a = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        if i == j:
            a[i, j] = -2
        elif abs(i - j) == 1:
            a[i, j] = 1

V = np.zeros((n, n))

for i in range(n):
    if abs(x[i]) > L/2:
        V[i, i] = V0

H = -(hbar**2 / (2*m*dx**2)) * a + V
energy, wavefunction = np.linalg.eigh(H)

print("Energy levels:")

for i in range(5):
    print("E", i+1, "=", energy[i])

plt.plot(x, np.diag(V), 'k', label='Potential')

for i in range(3):
    psi = wavefunction[:, i]
    psi = psi / np.max(abs(psi))
    plt.plot(x, energy[i] + psi,
             label="n = " + str(i+1))
    
plt.xlabel("x")
plt.ylabel("Energy")
plt.title("Particle in Finite Well")
plt.legend()
plt.grid()
plt.show()


