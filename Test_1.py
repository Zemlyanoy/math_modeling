from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

import tkinter as tk
import time
from random import randint, choice
 
window = tk.Tk()
window.geometry("500x250")
window.resizable(False, False)
window.title("Billiards Simulation")
 
canvas = tk.Canvas(window, width=500, height=250, bg="springgreen", highlightthickness=0)
canvas.pack()
 
ball_x = randint(50, 450)
ball_y = randint(50, 200)
 
ball = canvas.create_oval(ball_x, ball_y, 20 + ball_x, 20 + ball_y, fill="yellow")
step_x = choice([-1., 1.])
step_y = choice([-1., 1.])
 
while True:
    window.update()
    canvas.move(ball, step_x, step_y)
    ball_coords = canvas.coords(ball)
    if ball_coords[0] <= 0 or ball_coords[2] >= 500:
        step_x *= -1
    if ball_coords[1] <= 0 or ball_coords[3] >= 250:
        step_y*= -1
    step_x *= 0.999
    step_y *= 0.999
    sqr_mag = step_x**2+step_y**2
    canvas.create_oval(ball_coords[0]+10,ball_coords[1]+10,ball_coords[0]+10,ball_coords[1]+10)
    canvas.tag_raise(ball)
    if sqr_mag < 0.0001:
        break
    time.sleep(0.001)
    
window.mainloop()