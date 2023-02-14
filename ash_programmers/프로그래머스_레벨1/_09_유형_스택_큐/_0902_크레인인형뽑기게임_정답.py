# https://school.programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    arr = []
    for i in range(len(moves)):
        a = moves[i] - 1
        for j in range(len(board[0])):
            b = board[j][a]
            if b != 0:
                arr.append(board[j][a])
                board[j][a] = 0
                
                while True:
                    check = False
                    c = arr[0]
                    for j in range(len(arr)-1):
                        d = j + 1
                        if c == arr[d]:
                            arr.pop()
                            arr.pop()
                            answer += 2
                            break
                        c = arr[d]
                    if check == False:
                        break
                break
    return answer

board = [
     [0,0,0,0,0],
     [0,0,1,0,3],
     [0,2,5,0,1],
     [4,2,4,4,2],
     [3,5,1,3,1]
    ]
moves = [1,5,3,5,1,2,1,4]

re = solution(board , moves)
print("Re : " , re)