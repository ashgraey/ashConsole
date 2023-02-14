"""
최대공약수 구하는법 3가지 (3번이 가장적은 시간이 소요된다.)
[1] 전부 검사
"""
a = 24
b = 76
result = 0
i = 1
while i <= a:
    if a % i == 0 and b % i == 0:
        result = i
    i += 1
print(result)

"""
[2] 빼기
"""
a = 24
b = 76
result = 0
while True:
    if a > b:
        a -= b
    elif b > a:
        b -= a
    elif a == b:
        break
print(a)

"""
[3] 유클리드 호제법 
"""
a = 24
b = 76
if a < b:
    temp = a
    a = b
    b = temp
while True:
    if b == 0:
        break
    a = a % b
    temp = a
    a = b
    b = temp
print(a)






