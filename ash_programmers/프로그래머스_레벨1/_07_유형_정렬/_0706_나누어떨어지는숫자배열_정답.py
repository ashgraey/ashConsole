# https://school.programmers.co.kr/learn/courses/30/lessons/12910
def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
    answer.sort()
    if len(answer) == 0:
        return [-1]
    return answer


arr = [5,9,7,10]
divisor = 5
a = solution(arr , divisor)
print(a)