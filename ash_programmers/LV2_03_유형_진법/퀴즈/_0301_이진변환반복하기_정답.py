
# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def getOneStr(s):
    st = ""
    for i in range(len(s)):
        if s[i] == '1':
            st += s[i]
    return st

def getBinary(n):
    a = 1
    while True:
        if a > n:
            break
        a *= 2
    st =''

    while True:
        if a == 0:
            break
        st += str(n // a)
        n = n % a
        a //= 2
    
    st = st[1:]
    return st


def solution(s):
    answer = [0,0]
    
    while True:
        if s == "1":
            break
        
        tempstr = s
        s = getOneStr(s)
        c = len(tempstr) - len(s)
        answer[1] += c
        answer[0] += 1
        s = getBinary(len(s))
       # print(s)
    return answer

s = "110010101001"

r = solution(s)
print(r)

"""
이진법 변환을 한다.

"""