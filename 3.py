import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 500
seconds_in_year = 365 * 24 * 60 * 60
years = 1
t = np.linspace(0, years*seconds_in_year, frames)

def move_func(s, t):
    (x1, v_x1, y1, v_y1,
     x2, v_x2, y2, v_y2,
     x3, v_x3, y3, v_y3,
     x4, v_x4, y4, v_y4) = s

    dxdt1 = v_x1
    dv_xdt1 = - G * M1 * x1 / (x1**2 + y1**2)**1.5
    dydt1 = v_y1
    dv_ydt1 = - G * M1 * y1 / (x1**2 + y1**2)**1.5 

    dxdt2 = v_x2
    dv_xdt2 = - G * M2 * x2 / (x2**2 + y2**2)**1.5
    dydt2 = v_y2
    dv_ydt2 = - G * M2 * y2 / (x2**2 + y2**2)**1.5

    dxdt3 = v_x3
    dv_xdt3 = - G * M3 * x3 / (x3**2 + y3**2)**1.5
    dydt3 = v_y3
    dv_ydt3 = - G * M3 * y3 / (x3**2 + y3**2)**1.5

    dxdt4 = v_x4
    dv_xdt4 = - G * M4 * x4 / (x4**2 + y4**2)**1.5
    dydt4 = v_y4
    dv_ydt4 = - G * M4 * y4 / (x4**2 + y4**2)**1.5

    return (dxdt1, dv_xdt1, dydt1, dv_ydt1,
            dxdt2, dv_xdt2, dydt2, dv_ydt2,
            dxdt3, dv_xdt3, dydt3, dv_ydt3,
            dxdt4, dv_xdt4, dydt4, dv_ydt4)

G = 6.67 * 10**(-11)
M1 = 3.285 * 10**(23)
M2 = 5.9736 * 10**(24)
M3 = 4.867 * 10**(23)
M4 = 6.39 * 10**(23)
M5 = 1.989 * 10**(30)

x10 = 149 * 10 **9 # Меркурий
v_x10 = 1
y10 = 1
v_y10 = 30000

x20 = - 149 * 10 **9 # Земля
v_x20 = 1
y20 = 1
v_y20 = - 30000

x30 = 1 # Венера
v_x30 = -149 * 10 **9
y30 = -30000
v_y30 = 1

x40 = 1 # Марс
v_x40 = 149 * 10 **9
y40 = 30000
v_y40 = 1


s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40)
sol = odeint(move_func, s0, t)

def solve_func(i, key):
    if key == 'point':
        x1 = sol[i, 0]
        y1 = sol[i, 2]
        x2 = sol[i, 4]
        y2 = sol[i, 6]
        x3 = sol[i, 8]
        y3 = sol[i, 8]
        x4 = sol[i, 10]
        y4 = sol[i, 10]
    else:
        x1 = sol[:i, 0]
        y1 = sol[:i, 2]
        x2 = sol[:i, 4]
        y2 = sol[:i, 6]
        x3 = sol[:i, 8]
        y3 = sol[:i, 8]
        x4 = sol[:i, 10]
        y4 = sol[:i, 10]
    
    return ((x1, y1), (x2, y2), (x3, y3), (x4, y4))


fig, ax = plt.subplots()

ball1, = plt.plot([], [], 'o', color='b')
ball_line1, = plt.plot([], [], '-', color='b')

ball2, = plt.plot([], [], 'o', color='c')
ball_line2, = plt.plot([], [], '-', color='c')

ball3, = plt.plot([], [], 'o', color='g')
ball_line3, = plt.plot([], [], '-', color='g')

ball4, = plt.plot([], [], 'o', color='r')
ball_line4, = plt.plot([], [], '-', color='r')

plt.plot([0], [0], 'o', color='y', ms=20)


def animate(i):
    ball1.set_data(solve_func(i, 'point')[0])
    ball_line1.set_data(solve_func(i, 'line')[0])

    ball2.set_data(solve_func(i, 'point')[1])
    ball_line2.set_data(solve_func(i, 'line')[1])

    ball3.set_data(solve_func(i, 'point')[2])
    ball_line3.set_data(solve_func(i, 'line')[2])

    ball4.set_data(solve_func(i, 'point')[3])
    ball_line4.set_data(solve_func(i, 'line')[3])


ani = FuncAnimation(fig, animate, frames=frames, interval=30)

plt.axis('equal')
edge = 2 * x10
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani.save('earth_mercury_mars_venera.gif')