
"""
    최소공배수 구하기 재귀
"""

def gcd(a , b):
    if b == 0:
        return a
    else:
        return gcd(b , a % b)

a = 24
b = 76

c = a * b // gcd(a , b)
print(c)







