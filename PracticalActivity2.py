from math import *

print("Практическая работа 2. Логические выражения. Квадратное уравнение.")

print("Часть 1.")
print("a)")

x = int(input("Введите значение x: "))

if (-1 <= x < 7):
    print("Входит")
else:
    print("Не входит")


print("b)")

x = int(input("Введите значение x: "))

if (-10 < x <= -3) or (0 <= x <= 13):
    print('Входит')
else:
    print('Не входит')