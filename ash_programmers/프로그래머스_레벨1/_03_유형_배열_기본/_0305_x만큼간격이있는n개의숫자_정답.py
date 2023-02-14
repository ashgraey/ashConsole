# https://school.programmers.co.kr/learn/courses/30/lessons/12954
def solution(x, n):
    answer = []
    a = x
    for i in range(n):
        answer.append(a)
        a += x
    return answer

x = 2
n = 5
answer = solution(x , n)
print(answer)