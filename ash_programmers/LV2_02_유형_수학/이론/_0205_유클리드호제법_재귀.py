"""
[유클리드 호제법 재귀]
"""

def gcd(a , b):
    if b == 0:
        return a
    else:
        return gcd(b , a % b)

result = gcd(24, 76)
print(result)






