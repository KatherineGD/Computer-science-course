import numpy as np
import matplotlib.pyplot as plt

X = np.genfromtxt('13X.txt')
print('Исходный массив X')
print(X)

N = len(X)

Y = np.genfromtxt('13Y.txt')
print('Исходный массив Y')
print(Y)

Sx = sum(X)
Sy = sum(Y)
Sxx = np.dot(X,X)
Sxy = np.dot(X,Y)

a = (N * Sxy - Sx * Sy) / (N * Sxx - Sx * Sx)
b = (Sy - a * Sx) / N
print('y = ', a, '*x+', b)

YY = []

for x in X:
    YY.append(float(a * x + b))

Z = (np.array(Y) - np.array(YY))**2
SS = sum(Z)
print('SS = ', SS)

plt.title('MHK')
plt.xlabel('X')
plt.ylabel('Y')

plt.scatter(X,Y,c = 'r', marker = '*')

plt.plot(X, YY, 'b')

plt.show()