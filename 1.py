import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
 
t = np.arange(-5, 5, 0.01)


def diff_func(g, t): 
    y, z = g 
	
    dy_dt = y ** 2 * z
    
    dz_dt = (z / x) - y * z ** 2
    
    return dy_dt, dz_dt
 
y0 = 1
z0 = -3
g0 = y0, z0
x = 1.5
 
sol = odeint(diff_func, g0, t)
 
plt.plot(t, sol[:, 0], 'b', label='1')

plt.legend()
plt.savefig('anime')