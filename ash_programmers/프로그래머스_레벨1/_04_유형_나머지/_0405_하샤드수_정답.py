# https://school.programmers.co.kr/learn/courses/30/lessons/12947
def solution(x):
    total = 0
    a = x
    while True:       
        if x  == 0:
            break
        total += x % 10
        x = x // 10      
    print(a , " " , total)
    if total == 0 or a == 0:
        return False
    return a % total == 0

arr = 1203
a = solution(arr)
print(a)

