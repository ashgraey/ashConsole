# https://school.programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    answer = 0
    a = 0
    b = 1
    c = a + b
    for i in range(2, n):
        a = b
        b = c
        c = a + b
    answer = c % 1234567

    return answer

n = 3
r = solution(n)

print(r)