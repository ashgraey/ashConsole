
# https://suhak.tistory.com/81

"""
피보나치 수열
    1 1 2 3 5 8 13 ... 
"""

n = 5
if n == 1 or n == 2:
    print(n)
else:
    a = 1
    b = 2
    c = a + b
    for i in range(3 , n):
        a = b
        b = c
        c = a + b
    print(c)