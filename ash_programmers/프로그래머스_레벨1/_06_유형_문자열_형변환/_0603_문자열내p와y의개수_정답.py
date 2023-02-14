# https://school.programmers.co.kr/learn/courses/30/lessons/12916
def solution(s):
    s = s.upper()

    a = 0
    b = 0
    for i in range(len(s)):
        if s[i] == 'P':
            a += 1
        if s[i] == 'Y':
            b += 1
    return a == b

s = "pPoooyY"
a = solution(s)
print(a)