import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
 
t = np.arange(-1, 1, 0.01)


def diff_func(g, t): 
    y, x = g 
	
    dy_dt = 3 * x - 2 * y + (e ** 3 * t/ e ** t + 1 )
    
    dz_dt = x - (e ** 3 * t/ e ** t + 1 )
    
    return dy_dt, dz_dt
e = np.e
y0 = -7
x0 = 5 
g0 = y0, x0
 
sol = odeint(diff_func, g0, t)
 
plt.plot(t, sol[:, 0], 'b', label='1')

plt.legend()
plt.savefig('e')