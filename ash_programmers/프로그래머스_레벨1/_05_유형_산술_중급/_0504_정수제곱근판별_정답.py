# https://school.programmers.co.kr/learn/courses/30/lessons/12934

import math
def solution(n):
    if math.sqrt(n) - int(math.sqrt(n)) != 0:
        return -1
    else:
        n = math.sqrt(n)
        n += 1
        return int(n * n)

n = 121
a = solution(n)
print(a)