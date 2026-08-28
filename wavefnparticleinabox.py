# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 11:58:34 2026

@author: anuraag
"""

import numpy as np 
import matplotlib.pyplot as plt

n = 100
a=np.zeros((n,n))
for i in range(n):
    for j in range(n):
        if i==j:
            a[i,j]=-2
        elif abs(i-j)==1 :
            a[i,j]=1            
print(a)

l=1.0
n=100
dx= l/ (n+1)
h_bar=1
m=1
c= (-1)*(1/2*(dx**2))
H =c*a
y=energies,wfs = np.linalg.eigh(H)
print(wfs)
print(energies)

x=np.linspace(0,l,n)

for j in range(1):
    plt.plot(x,wfs[:,j])
    
plt.legend()
plt.grid()



