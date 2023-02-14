# https://school.programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    answer = 0
    a = ""
    temp = n
    b = 1
    while True:
        # print(temp)
        a += str(temp % 3)
        temp = temp // 3
        if temp == 0:
            break
        b *= 3
    #print("b : " , b)
    #print("a : " , a)
    for i in range(len(a)):
        c = int(a[i]) * b
        answer += c
        b //= 3
    return answer
n = 45
result = solution(n)
print(result)