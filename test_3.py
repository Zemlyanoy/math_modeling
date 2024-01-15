import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 
fig, ax = plt.subplots() # Создание пространства и подпространства
 
anim_object, = plt.plot([], [], '-', lw=2) # Объект анимации
 
xdata, ydata = [], [] # Координаты объекта анимации
 
ax.set_xlim(-20, 20) # Пределы изменения переменной Х
ax.set_ylim(-20, 20) # Пределы изменения переменной У
 
# Функция подстановки координат в объект анимации
def update(frame):
    xdata.append(16 * np.sin(frame) ** 3) # Рассщет координаты Х
    ydata.append(13 * np.cos(frame) - 5 * np.cos(frame * 2) - 2 * np.cos(frame * 3) - np.cos(frame * 4)) # Рассщет координаты У
    anim_object.set_data(xdata, ydata) # Передача координат
    return anim_object,
 
ani = FuncAnimation(fig, # Стандартный вызов пространства
                    update, # Вызов функции подстановки координат
                    frames=np.arange(0, 2*np.pi, 0.1),
                    interval=15 # Интервал между кадрами,
                    )            # по умолчанию 200 милисекунд
	
ani.save('<3.gif')