'''
    [길이가 다른 이차원 리스트]
        이차원 리스트는 길이가 다르게도 구성할 수 있다.
'''
import random

a = [
    [1,2,3,4],
    [1,2],
    [1,2,3,4,5]
]			  
print(a)  
print("--------------------------")

b = []
c = [1,2,3]
d = [1,2]
e = [1,2,3,4,5]
b.append(c)
b.append(d)
b.append(e)
print(b)
print("--------------------------")

f = []
for i in range(3):
    r = random.randint(1,9)
    temp = []
    for j in range(r):
        temp.append(j)
    f.append(temp)
    
print(f)
print("--------------------------")