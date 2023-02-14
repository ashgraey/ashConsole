# https://school.programmers.co.kr/learn/courses/30/lessons/12918
def solution(s):

    sample = "0123456789"
    for i in range(len(s)):
        if s[i] not in sample:
            return False
    if len(s) == 4 or len(s) == 6:
        return True
    return False

s = "3e10"

a = solution(s)
print(a)