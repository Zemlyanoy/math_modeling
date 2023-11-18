'''
типы данных 
числовые
кортежи
символы
'''

	
def changer(a, b):
    a = 2
    b[0] = 'Good'
 
x = 10
L = [1, 2]
 
changer(x, L)
 
print(x)
print(L)
 
L = [1, 2]
changer(x, L[:])
 
print(L)


# Coplex numbers
x = 3
y = 4

z = complex(x,y)
print(z)

w = complex(y, x)

print(z + w)

# Strings
s = 'hello'
print(s[0])

s[0] = 'H'

# Tuple
t = (1, 4, 9)
print(t)
print(t[0])
t[0] = 3

# list
l = [1, 4, 9]
l[0] = 3
print(l)

# Dict
d = {'a1':4, 4:'a1', 'str':'Hello'}
print(d['a1'])
print(d[4])
print(d['str'])

d['str'] = 'Good'
print(d)

	
def my_func(a, b):
    x = 3 * a - b
    return x
 
tmp = my_func()
 
def my_func(a=1, b=0):
    x = 3 * a - b
    return x
 
print(my_func())
print(my_func(3, 4))
print(my_func(3))
print(my_func(b=3))
print(my_func(b=3, a=9))

def my_func(a, b=0):
    x = 3 * a - b
    return x

# Так НЕЛЬЗЯ!
# def my_func(a=0, b):
#     x = 3 * a - b
#     return x

def my_func(*args):
    x = 3 * args[0] - args[1]
    return x

print(my_func(3, 4))
print(my_func(3, 4, 8))

def my_func(**kwrgs):
    x = 3 * kwrgs['obj_1'] - kwrgs['obj_2']
    return x

print(my_func(obj_1=3, obj_2=4))
print(my_func(obj_1=3, obj_2=4, obj_3=8))

	
def my_func(a, b):
    x1 = 3*a - 2*b
    x2 = 5*b - 4*a
    return x1, x2
 
tmp = my_func(3, 2)
 
print(tmp)
print(tmp[0])
print(tmp[1])
 
print(my_func(3, 2)[1])

def crutoi_chuvak(a=1, b=1, c=1):
    ''' Мотивирующая функция, возвращаюая всегда значение
        "Крутой чувак", независимо от того какие аргументы
        Вы в нее запихали
    '''
    a = 'Pofig'
    b = 'Pofig'
 
    print('Куртой чувак')
 
 
crutoi_chuvak()
 
help(crutoi_chuvak)