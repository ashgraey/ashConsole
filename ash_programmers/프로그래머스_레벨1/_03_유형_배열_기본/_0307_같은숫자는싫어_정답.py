# https://school.programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    answer = []
    a = arr[0]
    answer.append(a)
    for i in range(len(arr) - 1):
        if a != arr[i + 1]:
            a = arr[i + 1]
            answer.append(a)
    return answer
arr = [1,1,3,3,0,1,1]
a = solution(arr)
print(a)