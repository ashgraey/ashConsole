# https://school.programmers.co.kr/learn/courses/30/lessons/92335?language=python3
import math

def getBinary(a , n):
    b = 1
    while True:
        if b > n:
            break
        b *= a
    st = ''
    while True:
        if b == 0:
            break

        st += str(n // b)
        n = n % b
        b = b // a
    st = st[1:]

    return st

def getPrime(n):
    if n <= 1:
        return False
    mx = math.sqrt(n)
    i = 2
    while i <= mx:
        if n % i == 0:
            return False
        i += 1
    return True

def solution(n, k):
    answer = 0
    temp = getBinary(k , n)
    arr = temp.split("0")
    #print(arr)
    for v in arr:
        if v == '':
            continue
        v = int(v)
        if getPrime(v):
            answer += 1
    return answer

n = 437674
k = 3
r = solution(n , k)
print(r)

"""
3~10진수로 형변을 한다. 이후 소수 검사한다.

"""