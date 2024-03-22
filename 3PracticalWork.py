from math import *
x = float(input("Введите x: "))
y = float(input("Введите y: "))
z = float(input("Введите z: "))

u1 = 1/max(x,y,z)
u2 = min(y/x, 2*y+z, z)

if x<0:
    print("Ответ: ", u1)
else:
    print("Ответ: ", u2)