from math import *

print("Вариант 4")

print("Задание №1")
x = 2
z = 3
y = z**(3*x) + 3*(x**z) - 0,3
print("Ответ: " , y)

print("Задание №2")
x = 1
y = (log(abs(sin(x))**3)+1)**1/2 - e**(-x)
print("Ответ: " , y)

print("Задание №3")
x = 2
y = 2
z = (((0.3*(cos(x**2)**2)+1))/(2*x*y)) + 6
print("Ответ: ", z)

print("Задание №4")
x = 3
y = ((atan(2*x)+7)/(x+4.2)) + x**(1/3)
print("Ответ: ", y)

print("Часть 2. Программирование формул")\

u = 0
v2 = 6
w = u + 3*v2

t = int(input("Введите значение t: "))
g = int(input("Введите значение g: "))

p = v2*t*g*u

answer = ((w - 4*p)*(p^2 - w))/(3*w + 4*p)

print("Ответ:", answer)