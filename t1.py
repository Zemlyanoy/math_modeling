import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
 
t = np.arange(0, 50, 0.2)

def radio_function(m, t):
    dmdt = k * m
    return dmdt 

m_0 = 5
k = 0.1

m_t = odeint(radio_function, m_0, t)

plt.plot(t, m_t[:,0], label='Распад Висмута 210')

 
plt.savefig('anim')