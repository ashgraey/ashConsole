# https://school.programmers.co.kr/learn/courses/30/lessons/12912
def solution(a, b):
    if a > b:
        temp = a
        a = b
        b = temp
    answer = 0
    while a <= b:
        answer += a
        a += 1

    return answer

a = 3
b = 5

c = solution(a , b)
print(c)