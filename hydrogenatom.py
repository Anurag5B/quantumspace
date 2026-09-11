# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 11:32:16 2026

@author: anuraag
"""
import numpy as np
import matplotlib.pyplot as plt

hb = 1.05e-34
m = 9.10e-31
e = 1.602e-19
eo = 8.85e-12

ao = 5.29e-11
l = 0
n = 100
rmi = 1e-15
rma = 10 * ao

r = np.linspace(rmi, rma, n)
dr = r[1] - r[0]

vc = (hb**2) * (l * (l + 1)) / (2 * m * r**2)
v = -e**2 / (4 * np.pi * eo * r)
veff = v + vc

t = np.zeros((n, n))

for i in range(n):
    t[i, i] = 2

    if i > 0:
        t[i, i-1] = -1

    if i < n-1:
        t[i, i+1] = -1

t *= hb**2 / (2 * m * dr**2)

print(t)

H = t + np.diag(veff)

energies, wfs = np.linalg.eigh(H)
energies = energies / e

print("\nFirst five energy levels:")
for i in range(5):
    print(i + 1, energies[i], "eV")

u = wfs[:, 0]


plt.plot(r / ao, u)
plt.xlabel("r / a₀")
plt.ylabel("u(r)")
plt.grid()
plt.show()
