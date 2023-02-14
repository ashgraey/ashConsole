# https://school.programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        min = arr[0]
        index = 0
        for i in range(len(arr)):
            if min > arr[i]:
                min = arr[i]
                index = i
        del(arr[index])
        return arr

arr =[4,3,2,1]
a = solution(arr)
print(a)