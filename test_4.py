n=int(input())
k=[0,1]
for i in range(2,n):
 k.append(k[i-1]+k[i-2])
print(*k)