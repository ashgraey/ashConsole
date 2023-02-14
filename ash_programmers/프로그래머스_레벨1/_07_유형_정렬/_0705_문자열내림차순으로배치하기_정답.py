# https://school.programmers.co.kr/learn/courses/30/lessons/12917
def solution(s):
    a = sorted(s)
    a.reverse()
    a = "".join(a)

    return a

s = "Zbcdefg"

a = solution(s)
print(a)
