# https://school.programmers.co.kr/learn/courses/30/lessons/12911

def get1Count(st):
    c = 0
    for v in st:
        if v == "1":
            c += 1
    return c

def getBinary(num):
    st = ''
    a = 1
    while True:
        if a > num:
            break
        a *= 2
    #print("a : " , a , num)
    while True:
        if a == 0:
            break
        st += str(num // a)
        num = num % a
        a //= 2

    st = st[1:]
    #print(st)
    return st


def solution(n):
    answer = 0
    a = getBinary(n)
    c1 = get1Count(a)
    while True:
        n += 1
        b = getBinary(n)
        c2 = get1Count(b)
        if c1 == c2:
            break
    return n

n = 78
r = solution(n)
print(r)