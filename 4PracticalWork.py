import numpy as np
import matplotlib.pyplot as plt

a0 = 2
a1 = -10
a2 = 3
a3 = 8
a4 = 2

y = lambda x: a0+a1*x+a2*x**2+a3*x**3+a4*x**4
print("y:", y)

x = np.linspace(-5, 5, 42)
print(' x y(x)')
for temp in x :
    print ( temp, y(temp))

xmax = max(x,key=y)
print('Xmax = ',xmax,end=' ')

fmax = max(y(x))
print('Ymax = ',fmax)

xmin = min(x,key=y)
print('Xmin = ',xmin,end=' ')

fmin = min(y(x))
print('Ymin = ',fmin)

pic = plt.subplots()

plt.plot(x, y(x))

plt.show()