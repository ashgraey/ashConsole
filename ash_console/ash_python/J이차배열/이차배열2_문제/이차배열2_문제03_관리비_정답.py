'''
    apt 리스트는 아파트 1동의 각 세대를 의미한다.
    pay 는 이번달 관리비를 뜻한다.
'''
import random

apt = [
		[101, 102, 103],	
		[201, 202, 203],	
		[301, 302, 303]		
	]		
pay = [
		[1000, 2100, 1300],	 
		[4100, 2000, 1000],	 
		[3000, 1600,  800]  
	]
rank = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

'''
    [문제 1] 
        각 층별 관리비 합을 출력하시오.
    [정답 1] 
        4400 7100 5400
'''
print("[문제1]")
for i in range(len(pay)):
    total = 0
    for j in range(len(pay[i])):
        total += pay[i][j]
    print(total, end=" ")
print()

'''
    [문제 2] 
        랜덤으로 호수와 관리비 한개 출력하시오.
    [예시 2]
        0 2
        103 1300 원 
'''
print("[문제2]")
rY = random.randint(0, 2)
rX = random.randint(0, 2)
print(rY, rX)
print(apt[rY][rX], pay[rY][rX], "원")


'''
    [문제 3] 
        관리비가 가장 많이 나온 집, 가장 적게 나온 집을 출력하시오.
    [정답 3]
        가장 많이 나온 집 = 201
        가장 적게 나온 집 = 303    
'''
print("[문제3]")
maxPay = 0
maxY = 0
maxX = 0

minPay = 4100
minY = 0
minX = 0

for i in range(len(pay)):
    for j in range(len(pay[i])):
        if maxPay < pay[i][j]:
            maxPay = pay[i][j]
            maxY = i
            maxX = j
        if minPay > pay[i][j]:
            minPay = pay[i][j]
            minY = i
            minX = j
print("가장 많이 나온 집 =", apt[maxY][maxX])
print("가장 적게 나온 집 =", apt[minY][minX])

'''     
    [문제 4] 
        관리비 많이나온 순서대로 rank리스트에 등수를 저장하시오.
    [정답 4]
        [7, 3, 6]
        [1, 4, 7]
        [2, 5, 9]
'''
print("[문제4]")
temp = []
for i in range(len(pay)):
    for j in range(len(pay[i])):
        temp.append(pay[i][j])

y = 0
x = 0
for i in range(len(temp)):
    count = 1
    for j in range(len(temp)):
        if temp[i] < temp[j]:
            count += 1
    
    rank[y % 3][x % 3] = count
    x += 1

    if i % 3 == 2:
        y += 1
    
for i in range(len(rank)):
    print(rank[i])