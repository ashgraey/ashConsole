# https://school.programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    array = [[0 for col in range(len(arr2[0]))] 
    for row in range(len(arr1))]
    #print(array)

    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            total = 0
            for k in range(len(arr1[0])):
                total += arr1[i][k] * arr2[k][j]
            array[i][j] = total


    return array

arr1 = [[1, 2], 
        [3, 4], 
        [5, 6],
        [7, 8]]

arr2 = [[10, 11, 12], 
        [13, 14, 15]]

r = solution(arr1 , arr2)
print(r)

"""
행렬
"""