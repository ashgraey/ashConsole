# https://school.programmers.co.kr/learn/courses/30/lessons/12941

def solution(a, b):
    answer = 0
    a.sort()
    b.sort()
    b.reverse()
    for i in range(len(a)):
        c = a[i] * b[i]
        answer += c
    return answer


a = [1,4,2]
b = [5,4,4]
a = [1,2]
b = [3,4]
r = solution(a , b)
print(r)