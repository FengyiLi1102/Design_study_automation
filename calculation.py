import math as ma
import numpy as np

x1, x2, h, H, L, W, vi, mu, m, d, g, banked_ang = 0.05, 0.05, 0.15, 0.30, 0.30, 0.15, \
                                                  0.5, 0.001, 0.0055, 0.0016,\
                                                  9.81, 30

r = d / 2
I = 2/5 * m * r**2
s1 = ma.sqrt(h**2 + (L-x1)**2)
s2 = ma.sqrt((H-h)**2 + (L-x2)**2)
theta = np.arctan(h / (L-x1))
beta = np.arctan((H-h) / (L-x2))

print("Input speed: ", vi)
vf1 = ma.sqrt((7*(vi**2) - 10*mu*g*x1) / 7)
a1 = (vf1**2 - vi**2) / 2 / x1
if mu != 0:
    t1 = (vf1 - vi) / a1
else:
    t1 = x1 / vf1
print("T1: ", t1)

a2 = g*np.sin(theta) / (1 + (I / r**2 / m))
vf2 = ma.sqrt(vf1**2 + 2*a2*s1)
t2 = (vf2 - vf1) / a2
print("T2: ", t2)

a3 = g*np.sin(beta) / (1 + (I / r**2 / m))
vf3 = ma.sqrt(vf2**2 + 2*a3*s2)
t3 = (vf3 - vf2) / a3
print("T3: ", t3)

vo = ma.sqrt((7*vf3**2- 10*mu*g*x2) / 7)
a4 = (vo**2 - vf3**2) / 2 / x2
t4 = (vo - vf3) / a4
print("T4: ", t4)
print("Output speed: ", vo)


t_tot = t1 + t2 + t3 + t4
print("The total passage time is: ", t_tot)