from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

 
def animate(i):
    ball.set_data(circle_move(Vx0 = 0.005, time=i, R = 4))


def circle_move(R, Vx0, time):
    x0 = Vx0 * time
    x = x0 * R
    y = 0
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
 
    ani.save('anime.gif') 











