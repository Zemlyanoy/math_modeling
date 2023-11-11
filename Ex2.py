import math
import Ex1
B=30
h=100
E=300
a=math.pi
V = ((Ex1.g*h) * (math. tan(B)**2)) / ((2*math.cos(a)**2)*(1-math. tan(B) * math. tan(a)))
print(V**0.5)
N = (2 /( math.pi**0.5))*(Ex1.h/((Ex1.k*200)**3/2)) * (math.e**(-300*200*Ex1.k)) * 300**100
print(N)