"""
    [문제]
        아래 조건에 모두 맞는 결과를 출력하시오.
        [1] 랜덤 숫자 10개를 출력한다.
        [2] 랜덤 숫자는 2 또는 5만출력한다.
        [3] 단, 둘중하나라도 3개에 먼저도달하면, 남은개수는 반대편 숫자로 전부 출력한다. 

    [예시]
        2, 5, 5, 2, 5, 2, 2, 2, 2, 2  
    [예시]
        5, 5, 2, 2, 2, 5, 5, 5, 5, 5
"""
import random

size = 10
count2 = 0 
count5 = 0

run = 1 
# count변수를 활용하여 2,5중 하나의 count값이 3이 될때까지 반복문을 돌린다.
while run == 1  :
    num = random.randint(0, 1)
    
    if num == 0 :
        num = 2
        count2 += 1 

    elif num == 1 :
        num = 5
        count5 += 1

    print(num, end = " ")

    if count2 == 3 or count5 == 3 :
        run = 0

# 2,5의 count값 중 하나가 3이되면 반복문을 종료하고
# 두 count를 더한값에서 10까지 반복
# count2가 3에 먼저 도달했다면 나머지 값으로 5를 출력
# count5가 3에 먼저 도달했다면 나머지 값으로 2를 출력 
i = count2 + count5
while i < 10 :
    if count2 == 3 :
        print(5, end = " ")
    elif count5 == 3 :
        print(2, end = " ") 
        
    i += 1 

print()
print("2 count =",count2)
print("5 count =",count5)

# i = 0 
# while i < 10 :
    
#     if count2 == 3 or count5 == 3 :
#        break
     
#     i += 1 
