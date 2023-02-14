# https://school.programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    answer = []
    a = 1
    b = n
    c = m
    if n > m:
        temp = n
        n = m
        m = temp
    while True:       
        check = False
        for i in range(2, n + 1):
            if m % i == 0 and n % i == 0:
                a *= i
                m //= i
                n //= i
                check = True
                #print("aa : " , a , " " , m , " " , n)
                break
        if check == False:
            break
    answer.append(a)
    i = b
    while True:
        if i % b == 0 and i % c == 0:
            break
        i += 1
    #print(i)
    answer.append(i)
    return answer

n = 2
m = 5
a = solution(n, m)
print(a)