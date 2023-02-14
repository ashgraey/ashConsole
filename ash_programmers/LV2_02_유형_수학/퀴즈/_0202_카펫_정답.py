# https://school.programmers.co.kr/learn/courses/30/lessons/42842

import math

def getBrownCount(garo , sero):
    count = 0
    count += garo * 2
    count += sero * 2
    count += 4
    return count

def solution(brown, yellow):
    answer = []
    i = 1
    garo = 0
    sero = 0
    sqrt = math.sqrt(yellow)
    sqrt = int(sqrt)
    while i <= sqrt:
        if yellow % i == 0:
            sero = i
            garo = yellow // sero
            #print(sero , garo)          
            bc = getBrownCount(garo , sero)
            if bc == brown :
                answer = [garo + 2 , sero + 2]
                break
        i += 1
    return answer


brown = 24
yellow = 24
r = solution(brown , yellow)
print(r)


"""
노란색 의 가로세로를 구해서 
노란색 가로 + 2 , 노란색 세로 + 2 가 정답이다.
구하는 방법은 아래와 같다. 
--------------------------------------------------------------
브라운은 24이고 , 노란색이 24이라고했을때, 
노란색의 가로 세로를 먼저 구하기위해 노란색의 약수를 구한다. 
24 => 1,2,3,4,6,8,12,24

결국 노란색의 가로와 세로는 아래 네개중 하나이다. 
1 * 24 
2 * 12
3 * 8
4 * 6

노란색을 브라운색이 감싸고있으니 결국 
브라운은 노란색 가로 * 2 + 노란색 세로 * 2 + 양쪽모서리 4 이다. 

브라운개수를 구한다. 
1 * 24 이면 => ( 2 + 48 + 4 )  => 54
2 * 12 이면 => ( 4 + 24 + 4)   => 32
3 * 8  이면 => ( 6 + 16 + 4)   => 26
4 * 6  이면 => ( 8 + 12 + 4)   => 24

브라운이 24이므로 정답은 4 * 6 이다 
노란색 가로는 6이고 세로는 4인것이다. 
전체 가로 세로를 구해야하니 6 + 2 , 4 + 2 => [8,6]이 정답이다. 
"""