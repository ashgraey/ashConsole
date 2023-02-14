# https://school.programmers.co.kr/learn/courses/30/lessons/12953

def gcd(a , b):
    if b == 0:
        return a
    else:
        return gcd(b , a % b)

def solution(arr):
    a = arr[0]
    for i in range(1 , len(arr)):
        b = arr[i]
        a = a * b // gcd(a , b)   
    return a

arr =[2,6,8,14]

r = solution(arr)

print(r)

"""
[1] a , b의 최대공약수 구하기 [유클리드 호제법] 
=============================
def gcd(a , b):
    if b == 0:
        return a
    else:
        return gcd(b , a % b)
=============================
[2] a와 b의 최소공배수
    [정답] a * b // a와b의 최대공약수

[3] a , b , c , d의 최소공배수 구하기
    a와b의 최소공배수를 구하고 그값이 a1이면
    a1과c의 최소공배수를 구하고 그값이 a2이면
    a2와 d의 최소공배수를 구한다. a3가 정답 

"""