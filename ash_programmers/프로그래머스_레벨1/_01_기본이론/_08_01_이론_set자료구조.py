"""
    set() 자료구조 
    파이썬에서 set은 중복되는 값을 허용하지않는다.
"""

import random

myset = set()

for i in range(100):
    r = random.randint(1,20)
    print(r , end=" ")
    myset.add(r) # 무려 100번을 저장했지만 중복된값은 저장되지않는다. 
print()
print("---------------------")
for v in myset:
    print(v , end=" ")
