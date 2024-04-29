import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

g = 9.81  
dt = 0.01  

radius = 0.1  
mass = 1.0  

wall_thickness = 0.1 
restitution = 0.9 

angle = float(input("Введите угол соударения (в градусах): "))
angle_rad = np.radians(angle) 

x0 = 0.0 
y0 = 1.0 
vx0 = 5.0 * np.cos(angle_rad) 
vy0 = -5.0 * np.sin(angle_rad) 

x_list = []
y_list = []

def update(i):
    global x0, y0, vx0, vy0

    x0 += vx0 * dt
    y0 += vy0 * dt - 0.5 * g * dt**2

    if x0 < radius or x0 > 1 - radius:
        vx0 = -vx0 * restitution
    if y0 < radius or y0 > 1 - radius:
        vy0 = -vy0 * restitution

    x_list.append(x0)
    y_list.append(y0)

fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

ax.hlines(0.5, 0, 1, color='black', linewidth=wall_thickness)


circle = plt.Circle((x0, y0), radius, color='red')
ax.add_patch(circle)

anim = animation.FuncAnimation(fig, update, interval=dt * 10, frames=50)
anim.save('ball_bounce_angle.gif', fps=60)
plt.show()