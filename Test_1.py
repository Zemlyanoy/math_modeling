import numpy as np
from numpy import absolute as nabs
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def collision(x1, vx1, x2, vx2, x3, vx3, radius, mass1, mass2, mass3):
    """Аргументы функции:
    x1, vx1 - координата и скорость 1-ой частицы
    x2, vx2 - координата и скорость 2-ой частицы
    radius, mass1, mass2 - радиус частиц и их массы
    """

    # Расчет расстояния между центрами частиц
    r12 = np.sqrt((x1 - x2 - x3) ** 2)

    # Проверка условия на столкновение: расстояние
    # должно быть меньше 2-х радиусов
    if r12 <= 2 * radius:
        # Пересчет  скорости первой частицы
        VX1 = vx1 * (mass1 - mass2) / (mass1 + mass2) \
              + 2 * mass2 * vx2 / (mass1 + mass2)

        # Пересчет скорости второй частицы
        VX2 = vx2 * (mass2 - mass1) / (mass1 + mass2) \
              + 2 * mass1 * vx1 / (mass1 + mass2)
        
        VX3 = vx3 + (2 * mass2 * (vx2 - vx3)) / (mass2 + mass3)

    else:
        # Eсли условие столкновнеия не выполнено,
        # то скорости частиц не пересчитываются
        VX1, VX2, VX3 = vx1, vx2, vx3

    return VX1, VX2,VX3


def move_func(s, t):
    x1, v_x1, x2, v_x2, x3, v_x3= s

    dx1dt = v_x1
    dv_x1dt = 0

    dx2dt = v_x2
    dv_x2dt = 0

    dx3dt = v_x3
    dv_x3dt = 0

    return dx1dt, dv_x1dt, dx2dt, dv_x2dt, dx3dt, dv_x3dt


def calc(mass1, mass2, mass3, radius, x10, x20, v10, v20, x30, v30, T, N):
    # Массивы для записи итоговых координат объектов
    x1 = [x10]
    x2 = [x20]
    x3 = [x30]

    tau = np.linspace(0, T, N)

    # Цикл для расчета столкновений
    for k in range(N - 1):
        t = [tau[k], tau[k + 1]]
        s0 = x10, v10, x20, v20, x30, v30

        sol = odeint(move_func, s0, t)

        x10 = sol[1, 0]
        x20 = sol[1, 2]
        x30 = sol[1, 4]
        x1.append(x10)
        x2.append(x20)
        x3.append(x30)

        v10 = sol[1, 1]
        v20 = sol[1, 3]
        v30 = sol[1, 5]
        res = collision(x10, v10, x20, v20, x30, v30, radius, mass1, mass2, mass3)
        v10 = res[0]
        v20 = res[1]
        v30 = res[2]

    return x1, x2, x3


def animate(i):
    ball_1.set_data((x1[i], 0))
    ball_2.set_data((x2[i], 0))
    ball_3.set_data((x3[i], 0))


if __name__ == '__main__':

    # Парамаетры и условия тестового примера
    mass1 = 3
    mass2 = 1
    mass3 = 1
    radius = 0.5

    x10 = 0
    x20 = 3
    x30 = 5
    y30 = 0.25
    v10 = 0.5
    v20 = 0
    v30 = 0

    # Разбиение общего времени моделирования на интервалы
    T = 5
    N = 250

    x1, x2, x3 = calc(mass1, mass2, mass3, radius, x10, x20, x30, v10, v20, v30, T, N)

    fig, ax = plt.subplots()

    ball_1, = plt.plot([], [], 'o', color='r', ms=25)
    ball_2, = plt.plot([], [], 'o', color='g', ms=25)
    ball_3, = plt.plot([], [], 'o', color='y', ms=25)
    ax.set_xlim(-5, 10)
    ax.set_ylim(-1, 1)

    ani = FuncAnimation(fig, animate, frames=N, interval=30)
    plt.plot([-0.5, 8], [0.5, 0.5])
    plt.plot([-0.5, 8], [-0.5, -0.5])
    plt.grid()
    ani.save('collision.gif')