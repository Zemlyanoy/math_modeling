import numpy as np
from Ex1 import g
a=np.zeros((6,3),int)
V,x0,y0=map(int,input().split())
for i in range(6):
 a[i,0]=i
 a[i,1]=x0+V*i
 a[i,2]=y0+V*i-((g*i**2)/2)
print(a)
