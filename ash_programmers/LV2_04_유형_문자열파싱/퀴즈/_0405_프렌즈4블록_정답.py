# https://school.programmers.co.kr/learn/courses/30/lessons/17679

def getArr(m, n , board):
    arr = []
    for i in range(len(board)):
        arr.append(list(board[i]))
    return arr

def printArr(arr):
    for v in arr:
        print(v)

def check4way(i , j , arr):
    val = arr[i][j]
    if arr[i + 1][j] == val and arr[i][j + 1] == val and arr[i+1][j+1] == val:
        return True
    return False


def deleteBlock(m , n , arr):
    temp = [[0 for j in range(n)] for i in range(m)]
    for i in range(m - 1):
        for j in range(n - 1):
            if arr[i][j] == "#":
                continue
            if check4way(i , j , arr):
                temp[i][j] = 1
                temp[i + 1][j] = 1
                temp[i ][j + 1] = 1
                temp[i + 1][j + 1] = 1
    #printArr(temp)
    c = 0
    for i in range(m):
        for j in range(n):
            if temp[i][j] == 1:
                arr[i][j] = "#"
                c += 1
    #printArr(arr)
    return c




def downBlock(m, n, arr):
    #print("downBlock=[start]")
    for x in range(n):
        ye = m - 1
        while ye >= 0:
            if arr[ye][x] == "#":
                y2e = ye - 1
                while y2e >= 0:
                    if arr[y2e][x] != "#":
                        temp = arr[y2e][x]
                        arr[y2e][x] = arr[ye][x]
                        arr[ye][x] = temp
                        break
                    y2e -= 1
            ye -= 1

    #printArr(arr)
    #print("downBlock=[end]")
    return arr

def solution(m, n, board):
    arr = getArr(m , n , board)
    #printArr(arr)
    total = 0
    while True:
        c = deleteBlock(m , n, arr)
        total += c
        if c == 0:
            break
        arr = downBlock(m , n , arr)
    return total


m , n , board =   4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]
r = solution(m, n , board)
print(r)