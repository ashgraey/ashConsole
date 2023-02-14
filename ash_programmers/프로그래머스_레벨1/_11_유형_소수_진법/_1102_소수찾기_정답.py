# https://school.programmers.co.kr/learn/courses/30/lessons/12921

import math

def solution(n):
    count = 0
    for i in range(2, n + 1):
        c = 0
        a = math.sqrt(i)
        # print(a)
        # a = i
        # print(a)
        a = int(a)
        check = False
        for j in range(2 , a + 1):
            if i % j == 0:
                check = True
                break
        if check == False:
            count += 1
            # pass
    return count

n = 10
result = solution(n)
print(result)