import numpy as np
b=np.zeros((1,1))
b=(input().split())
def multiply(b):
    e=1
    for i in range(len(b)):
        e*=int(b[i])
    print(e)
multiply(b)
