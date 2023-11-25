m, h, v=map(int,input().split())
def energy(m, h, v):
    g=9.8
    Ek=(m*(v**2))/2
    Ep=m*g*h
    print(Ek+Ep)
energy(m, h, v)