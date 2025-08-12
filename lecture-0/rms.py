from random import random

n=1000
data=[]
for i in range(n):
    data.append(random())

print(f'El valor RMS es: {RMSValue(data)}')