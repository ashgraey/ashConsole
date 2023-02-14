# https://school.programmers.co.kr/learn/courses/30/lessons/17687


def getArithmetic(a , b):
    temp = 1
    while True:
        if temp > b:
            break
        temp *= a
    st = ''
    while True:
        if temp == 0:
            break
        share = b // temp
        b = b % temp

        sample = "0123456789ABCDEF"    
        st += sample[share]
        temp //= a

    st = st[1:]
    return st

def solution(n, t, m, p):
    mx = t * m
    st = '0'
    num = 1
    while True:
        if len(st) >= mx:
            break
        ari = getArithmetic(n, num)
        st += str(ari)
        num += 1
    #print(st)
    answer = ''
    c = 0
    for  i  in range(len(st)):
        if c == t:
            break
        if i % m + 1== p:
            c += 1
            answer += st[i]
     
    return answer
n = 16
t = 16
m = 2
p = 1
r = solution(n , t , m , p)
print(r)



"""
[1] 2~ 16진법 변환을 해야한다.
[2] 변환된숫자들을 0~목표숫자까지 전부 더해서 연결해야한다. 
"""