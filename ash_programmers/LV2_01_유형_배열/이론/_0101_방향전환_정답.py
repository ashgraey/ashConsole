"""
    철수는 모두의 마블게임을 만들려고 한다.
    특이하게 배열의 크기를 조절가능하게 만들고싶다.
    숫자n을 랜덤으로 저장하고 그크기에 맞는 2차원배열을 생성한다.
    배열의 0,0의 위치에 숫자1을 저장하고 , 
    동남서북 방향으로 이동하며, 숫자를 1씩 증가하며 저장한다. 
    배열의 끝에 도착하면 방향은 바뀐다. 
    배열의 외각을 제외한 곳은 숫자 99로 채운다.
    랜덤 숫자 n은 2~5사이이다. 

    [예시1]
        n = 2

        [1][2]
        [4][3]

    [예시2]
        n = 4

        [ 1][ 2][ 3][ 4]
        [12][99][99][ 5]
        [11][99][99][ 6]
        [10][ 9][ 8][ 7]
"""
import random

n = random.randint(2, 5)
print(n)
arr = [[99 for j in range(n)] for i in range(n)]
#print(arr)

dir = "right" # right , down , left ,  up

y = 0
x = 0
num = 1
count = 0
i = 0
while True:
    #print(y , x)
    arr[y][x] = i + 1
    if dir == "right" and x + 1 >= n:
        dir = "down"

    if dir == "down" and y + 1 >= n:
        dir = "left"

    if dir == "left" and x - 1 < 0:
        dir = "up"

    if dir == "up" and arr[y-1][x] == 1:
        break
    
    if dir == "right":
        x += 1
    elif dir == "down":
        y += 1
    elif dir == "left":
        x -= 1
    elif dir == "up":
        y -= 1
    i += 1

print("------------------")
for i in range(n):
    print(arr[i])










