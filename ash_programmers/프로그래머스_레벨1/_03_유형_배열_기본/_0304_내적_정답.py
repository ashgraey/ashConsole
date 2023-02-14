#https://school.programmers.co.kr/learn/courses/30/lessons/70128
def solution(a, b):
    total = 0
    for i in range(len(a)):
        c = a[i] * b[i]
        total += c 
    return total


a = [1,2,3,4]
b = [-3,-1,0,2]

result = solution(a, b)
print(result)