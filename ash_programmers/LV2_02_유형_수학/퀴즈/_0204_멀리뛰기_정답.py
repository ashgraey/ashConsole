# https://school.programmers.co.kr/learn/courses/30/lessons/12914

def solution(n):
    answer = 0
    if n == 1 or n == 2:
        return n

    a = 1
    b = 2
    c = a + b
    for i in range(3, n):
        a = b
        b = c
        c = a + b
    answer = c % 1234567

    return answer

n = 4
r = solution(n)
print(r)



"""
피보나치 수열이다. 

"""