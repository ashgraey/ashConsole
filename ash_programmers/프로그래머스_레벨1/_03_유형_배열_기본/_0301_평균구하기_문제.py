# https://school.programmers.co.kr/learn/courses/30/lessons/12944

def solution(arr):

    total = 0
    for i in arr :
        total += i
    
    avg = total / len(arr)
    
    return avg


arr = [1,2,3,4]
a = solution(arr)
print(a)