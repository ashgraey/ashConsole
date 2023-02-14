#https://school.programmers.co.kr/learn/courses/30/lessons/87389
def solution(n):
    answer = 0
    for i in range(n):
        if n % (i + 1) == 1:
            answer = i + 1
            break
    return answer
    
n = 10
result = solution(n)
print(result)