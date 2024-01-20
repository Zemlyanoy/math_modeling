from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

z = int(input())
a = z * np.pi / 4
 
def animate(i):
    ball.set_data(circle_move(Vy0 = 0.005, Vx0 = 0.005, time=i, R = 4, alpha = a))


def circle_move(R, Vx0, time, Vy0, alpha):
    y0 = Vy0 * np.sin(alpha)
    x0 = Vx0 * time
    x = x0 * R
    y = y0
    return x, y


if __name__ == '__main__':
 
    fig, ax = plt.subplots()
    ball, = plt.plot([], [], '+', color='g', label='Ball')
 
    
    plt.axis('equal')
    ax.set_xlim(-6, 6)
    ax.set_ylim(-3, 3)
    
    ani = FuncAnimation(fig,
                        animate,
                        frames=180,
                        interval=30)
 
    plt.plot([-100, 100], [0, 0])
    plt.plot([-100, 100], [2, 2])
    plt.grid()


    ani.save('anime.gif') 











