# -*- coding: utf-8 -*-
"""
Created on Fri May  8 14:19:21 2020

@author: 岩松
"""
import cmath
import numpy as np
import matplotlib.pyplot as plt

def z(c, n):
    if n == 0:
        return 0
    else:
        try:
            z1 = z(c,n-1)
        except:
            return [n]
        else:
            if isinstance(z1, list):
                return z1
            else:
                return abs(z1)**2 + c
            
x = np.linspace(-2,2,100)
y = np.linspace(-2,2,100)

X, Y = np.meshgrid(x, y)

U = np.full((100,100), 100)

i = 0
while i != 100:
    j = 0
    while j!= 100:
        c = complex(x[j], y[i])
        Ui = z(c, 100)
        if isinstance(Ui, list):
            U[i][j] = Ui[0]
        j += 1
    i += 1
    
plt.figure(dpi=100)
plt.contourf(X, Y, U, levels=30)
plt.xlabel("X")
plt.ylabel("Y")
plt.colorbar(label="number of iteration to diverge(100 means converge)")
plt.show()

x2 = np.linspace(0,0.5,100)
y2 = np.linspace(-1,1,100)

X2, Y2 = np.meshgrid(x2, y2)

U2 = np.full((100,100), 100)

i = 0
while i != 100:
    j = 0
    while j!= 100:
        c = complex(x2[j], y2[i])
        Ui = z(c, 100)
        if isinstance(Ui, list):
            U2[i][j] = Ui[0]
        j += 1
    i += 1
    
plt.figure(dpi=100)
plt.contourf(X2, Y2, U2, levels=30)
plt.xlabel("X")
plt.ylabel("Y")
plt.colorbar(label="number of iteration to diverge(100 means converge)")
plt.show()

        
        