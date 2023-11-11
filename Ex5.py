import numpy as np
import math
N,M=map(int,input().split())
a=np.zeros((N,M),int)
for i in range(N):
 for j in range(M):
  a[i,j]=np.sin(N*(i+1)+M*(j+1))
for i in range(N):
 a[i]=a[::,-1]
print(a)