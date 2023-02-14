# https://school.programmers.co.kr/learn/courses/30/lessons/12950
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        answer.append([])
        for j in range(len(arr1[i])):
            temp = arr1[i][j] + arr2[i][j]
            answer[i].append(temp)
    return answer



arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]

a = solution(arr1, arr2)
print(a)