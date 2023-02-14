# https://school.programmers.co.kr/learn/courses/30/lessons/68645

def getTriangle(n):
    arr = []
    for i in range(n):
        temp = [0 for i in range(i + 1)]
        arr.append(temp)
    return arr
def getCount(n):
    total = 0
    for i in range(n):
        total += (i + 1)
    return total
def solution(n):
    arr = getTriangle(n)
    total = getCount(n)
    #print(arr)
    #print(total)
    dir = "d"
    i = 1
    y = 0
    x = 0
    c = 0
    mx = n
    answer = []
    while True:
        if i > total:
            break
        c += 1
        if mx == c:
            if dir == "d":
                dir = "r"
            elif dir == "r":
                dir = "u"
            elif dir == "u":
                dir = "d"
            mx = mx - 1
            c = 0     
        arr[y][x] = i
        if dir == "d":
            y += 1
        elif dir =="r":
            x += 1
        elif dir == "u":
            y -= 1
            x -= 1   
        i += 1

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            answer.append(arr[i][j])

    return answer 

n = 4
result = solution(n)
print(result)