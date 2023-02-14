# https://school.programmers.co.kr/learn/courses/30/lessons/67256
def getPos(num):
    phone = [   
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [-1,0,-1]]
    pos = []
    for i in range(len(phone)):
        for j in range(len(phone[i])):
            if phone[i][j] == num:
                pos.append(i)
                pos.append(j)
                return pos

def getDistance(pos , finger):
    distance = 0
    y = pos[0] - finger[0]
    x = pos[1] - finger[1]
    if y < 0:
        y *= -1
    if x < 0:
        x *= -1
    distance = x + y
    return distance
  
def solution(numbers, hand):
    answer = ''
    lf = [3,0]
    rf = [3,2]
    #print(lf , " " , rf)   
    for i in range(len(numbers)):
    #for i in range(2):
        num = numbers[i]    
        pos = getPos(num)
        if num  in [1,4,7]:
            lf = pos
            st = "L"
        elif num in [3,6,9]:
            rf = pos
            st = "R"
        else:
            dis1 = getDistance(pos , lf)
            dis2 = getDistance(pos , rf)
            st = ""
            if dis1 == dis2 :
                if hand == "left":
                    lf = pos
                    st = "L"
                elif hand == "right":
                    rf = pos
                    st = "R"
            elif dis1 < dis2 :
                lf = pos
                st = "L"
            else :
                rf = pos
                st = "R"   
        #print(lf , " " , rf)   
        answer += st
    return answer

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
result = solution(numbers , hand)
print(result)