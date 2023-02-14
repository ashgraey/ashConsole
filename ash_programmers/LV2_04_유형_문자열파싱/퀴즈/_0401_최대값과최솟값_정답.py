# https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    answer = ''
    s = s.split(" ")
    a = list(map(int , s))
    mx = max(a)
    mn = min(a)
    st = ""
    st += str(mn)
    st += " "
    st += str(mx)

    return st

s = "1 2 3 4"
r = solution(s)
print(r)

# 음수도 인식해야하므로 형변환을 해서 저장하면된다. 