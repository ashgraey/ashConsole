# https://school.programmers.co.kr/learn/courses/30/lessons/12925
def solution(s):
    if s[0] == "-":
        a = int(s[1:])
        return -a
    else:
        a = int(s)
        return a


s = "1234"
a = solution(s)
print(a)