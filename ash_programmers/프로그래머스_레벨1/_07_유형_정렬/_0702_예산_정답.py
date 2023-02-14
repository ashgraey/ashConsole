# https://school.programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    sample = 0
    d.sort()
    c = 0
    for i , v in enumerate(d):
        temp = sample + d[i]
        if temp > budget:
            break
        sample = temp
        c += 1
    return c

d = [1,3,2,5,4]

budget = 9

result = solution(d , budget)
print(result)

