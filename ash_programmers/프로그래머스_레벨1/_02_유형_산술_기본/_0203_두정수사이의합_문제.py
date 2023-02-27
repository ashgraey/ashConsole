# https://school.programmers.co.kr/learn/courses/30/lessons/12912
def solution(a, b):

    if a > b :
        temp = a
        a = b
        b = temp

    tot = 0
    i = a 
    while i <= b :
        tot += i
        i += 1

    return tot
    


a, b = map(int, input().split())
c = solution(a , b)
print(c)