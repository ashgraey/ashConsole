"""
    [최소공배수구하는법 3가지]
    [1] 전부 비교    
"""
a = 24
b = 76
i = 1
while True:
    if i % a == 0 and i % b == 0:
        break
    i += 1
print(i)

"""
    [2] 더하기  
"""
a = 24
b = 76
ta = a
tb = b
while True:
    if ta == tb:
        break 
    elif ta < tb:
        ta += a
    elif tb < ta:
        tb += b
print(ta)

"""
    [최소공배수3]
    [3] 수학공식
        [3-0] a * b // (a와b의 최대공약수)
        [3-1] 24 * 76 // (24와76의 최대공약수)
        [3-2] 24 * 76 // 4
"""
print(24 * 76 // 4)






