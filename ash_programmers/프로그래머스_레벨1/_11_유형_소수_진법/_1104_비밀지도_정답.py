# https://school.programmers.co.kr/learn/courses/30/lessons/17681

def change10(n, num, maxnum):
    st = ""
    a = num
    for i in range(n):
        b = a // maxnum
        if b == 1:
            st += str("#")
        else:
            st += str(" ")
        a %= maxnum
        maxnum //= 2

    return st

def solution(n, arr1, arr2):
    answer = []
    maxnum = 1
    for i in range(n-1):
        maxnum *= 2
    temp1 = []
    for i, v in enumerate(arr1):
        a = change10(n, v , maxnum)
        temp1.append(a)
    temp2 = []
    for i, v in enumerate(arr2):
        a = change10(n, v , maxnum)
        temp2.append(a)
    
    for i in range(len(temp1)):
        a = ""
        for j in range(len(temp1[i])):
            if temp1[i][j] == "#" or temp2[i][j]== "#":
                a += "#"
            else:
                a += " "
        answer.append(a)
    return answer


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

result = solution(n, arr1, arr2)
print(result)