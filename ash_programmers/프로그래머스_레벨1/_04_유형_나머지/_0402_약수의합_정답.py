# https://school.programmers.co.kr/learn/courses/30/lessons/12928
def solution(n):
    if n == 0:
        return 0
    total = 0
    a = 1
    while True:
        if n % a == 0:
            total += a    
        if a == n:
            break
        a += 1
    return total


n = 0
a = solution(n)
print(a)