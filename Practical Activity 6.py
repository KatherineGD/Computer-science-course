f=open('6-8B.txt', 'r')
line = f.read()
B=[]

for x in line.split():
    B.append(int(x))

print('Начальный массив A')
print(B)

N=len(B)
f.close()

f=open('6-8C.txt', 'r')
line = f.read()
C=[]

for x in line.split():
    C.append(int(x))

print('Начальный массив C')
print(C)

M=len(C)
f.close()
N=min(N,M)
D=[]

for i in range(0,N):
    D.append(B[i])
    D.append(C[i])

print('Начальный массив D')
print(D)