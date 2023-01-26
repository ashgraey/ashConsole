"""
    [문제]
    [내마음대로 주사위게임]
        내마음대로 주사위게임 은 a와 b가 주사위를 두개를 던진다.
        두개의 주사위중 하나를 랜덤으로 선택해서 제시한다.

        아래의 특별한 게임규칙에 따라 승패가 갈린다. 
    
        a는 주사위를 2개 던진다.
        b는 주사위를 2개 던진다.

        a와 b는 두 주사위중 하나를 랜덤 선택해서 제출한다. 

        <게임규칙>
            [1] 숫자가 둘다 짝수이면 둘중 큰수가 승리 , 숫자가 같으면 비김
            [2] 숫자가 둘다 홀수이면 둘중 작은수가 승리 , 숫자가 같으면 비김
            [3] 하나는 짝수이고 하나는 홀수이면 
                주사위 숫자와 상관없이 비긴다. 
"""
print("----- 문제1 -----")
import random 

# a와 b가 주사위를 두개를 던진다.
a1 = random.randint(1, 6)
a2 = random.randint(1, 6)
print("a의 주사위 =", a1, a2)
b1 = random.randint(1, 6)
b2 = random.randint(1, 6)
print("b의 주사위 =", b1, b2)

# a와 b는 두 주사위중 하나를 랜덤 선택해서 제출한다. 
a_ch = random.randint(0, 1)
b_ch = random.randint(0, 1)
print(a_ch, b_ch)

if a_ch == 0 :
    a_ch = a1
else :
    a_ch = a2

if b_ch == 0 :
    b_ch = b1
else :
    b_ch = b2

print("a선택 =", a_ch)
print("b선택 =", b_ch)

# [1] 숫자가 둘다 짝수이면 둘중 큰수가 승리 , 숫자가 같으면 비김
# [2] 숫자가 둘다 홀수이면 둘중 작은수가 승리 , 숫자가 같으면 비김
# [3] 하나는 짝수이고 하나는 홀수이면 
# 주사위 숫자와 상관없이 비긴다.

# [1] 숫자가 둘다 짝수이면 둘중 큰수가 승리 , 숫자가 같으면 비김
if a_ch % 2 == 0 and b_ch % 2 == 0 :
    if a_ch > b_ch :
        print("a의 승리")
    elif a_ch < b_ch :
        print("b의 승리")
    else :
        print("비김")

# [2] 숫자가 둘다 홀수이면 둘중 작은수가 승리 , 숫자가 같으면 비김
if a_ch % 2 == 1 and b_ch % 2 == 1 :
    if a_ch < b_ch :
        print("a의 승리")
    elif a_ch > b_ch :
        print("b의 승리")
    else :
        print("비김") 

# [3] 하나는 짝수이고 하나는 홀수이면 주사위 숫자와 상관없이 비긴다. 
if (a_ch % 2 == 0 and b_ch % 2 == 1) or (a_ch % 2 == 1 and b_ch % 2 == 0) :
    print("비김")

"""
    [문제]
        반복문을 활용해서 1~99까지 반복한다.
        1~99사이의 숫자중에서 4 와 8 의 개수를 출력하시오.
    [정답]
        40
"""
'''
44
48
84
88
'''
print("----- 문제2 -----")
count = 0
i = 1 
while i <= 99 :
    일 = i % 10 
    십 = i // 10

    if 일 == 4 or 일 == 8 : 
        # print(i, end = " ")
        count += 1

    if  십 == 4 or 십 == 8 :
        # print()
        # print(i)
        count += 1 
    
    # if (일 == 4 and 십 == 4) or (일 == 8 and 십 == 8) :
    #     count += 1 
    i += 1 
print(count)

# count = 0
# i = 1 
# while i <= 99 :
#     일 = i % 10 
#     십 = i // 10

#     if 일 == 4 or 십 == 4 : 
#         # print(i, end = " ")
#         count += 1

#     if 일 == 8 or 십 == 8 :
#         # print()
#         # print(i)
#         count += 1 
    
#     if (일 == 4 and 십 == 4) or (일 == 8 and 십 == 8) :
#         count += 1 

#     i += 1 
# print(count)