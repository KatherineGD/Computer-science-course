from math import *

t = float(input("Введите значение t: "))

a = t - 3
b = -2 * (3*t - 4)
c = 7*t

if a == 0:
    x =- c/b
    print('x =', x)
else:
    D = b**2 - 4 * a * c
    print("D:", D)
    print("a:", a)
    print("b:", b)
    print("c:", c)
    if D >= 0:
        x1 = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)
        print('x1 =', x1, '\nx2 =', x2)
    else:
        print("D<0")