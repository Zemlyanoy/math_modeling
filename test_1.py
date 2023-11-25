a="1"
b=[]
while a!=0:
    a=int(input())
    b.append(a)
def average(b):
    e=0
    for i in range(len(b)-1):
        e+=b[i]
    return e/(len(b)-1)
print(average(b))