a,b,c=map(int,input().split())
k=[a]
for i in range(1,c):
 k.append(k[i-1]*b)
print(*k)