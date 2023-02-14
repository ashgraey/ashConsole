# https://school.programmers.co.kr/learn/courses/30/lessons/12922
def solution(n):
    answer = ''
    temp = "수박"
    for i in range(n):
        answer += temp[i % 2]

    return answer


n = 3
a = solution(n)
print(a)