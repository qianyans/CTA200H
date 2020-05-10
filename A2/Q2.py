# -*- coding: utf-8 -*-
"""
Created on Sun May 10 11:36:11 2020

@author: 岩松
"""

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def sir(y, t, a, b):
    s, i, r = y
    n = 1000
    return [-a*s*i/n, a*s*i/n-b*i, b*i]

a = 0.1
b = 0.2
y0 = [999, 1, 0]
t = np.linspace(0, 200, 200)


sol = odeint(sir, y0, t, args=(a, b))



plt.plot(t, sol[:, 0], 'b', label='S')
plt.plot(t, sol[:, 1], 'r', label='I')
plt.plot(t, sol[:, 2], 'g', label='R')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()