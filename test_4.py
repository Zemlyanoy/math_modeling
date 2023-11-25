a, b=map(int, input().split())
c=input().split()
def graphic(a, b, c):
    d=[]
    for i in range(len(c)):
                if int(c[i]) < a or int(c[i]) > b:
                    print("введите корректные числа")
                else:
                    d.append(int(c[i])**2)
                print(d)
graphic(a, b, c)