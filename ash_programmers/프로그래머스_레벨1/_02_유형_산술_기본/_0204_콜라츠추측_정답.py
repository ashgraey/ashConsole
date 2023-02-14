# https://school.programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    answer = 0
    if num == 1:
        return 0
    while True:
        if answer >= 500:
            return -1
        if num == 1:
            break
        answer += 1
        if num % 2 == 0:
            num //= 2
        else:
            num *= 3
            num += 1
    return answer

n = 16

result = solution(n)

print(result)

