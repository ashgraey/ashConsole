'''
    [문제]
        철수는 게임을 하고 있다. 
        monster는 게임의 적 4마리를 의미하고 
        숫자는 몬스터의 체력을 의미한다.
        
        철수의 공격력은 5이다.    
        총 다섯번을 반복하면서 
        랜덤으로 몬스터 중 하나를 선택해서 공격한다.
        모든 몬스터들을 공격한 후 몬스터들의 체력을 출력하시오.
        단, 몬스터 체력은 0이 되면 더 이상 내려가지 않는다.
    [정답]

'''
'''
반복 = 5
랜덤선택
체력 -
몬스터 체력 0까지
'''
import random

# [1115]
# monster = [9,7,8,6]
# att = 5

# for i in range(5) :
#     r = random.randint(0, len(monster) - 1)
#     # print("횟수 =", i)
#     print()
#     print("r =", r)
#     print("attack =", att)

#     monster[r] -= att

#     if monster[r] < 0 :
#         monster[r] = 0 
#         print("체력이 0입니다.") 
#     # print()
#     print(monster)

# [2차]
# monster = [9,7,8,6] # 게임의 적 수 : 4, 인덱스 수치 : 체력
# power = 5 # 공격력

# count = 0
# i = 0 
# while i < 5 : 
#     r = random.randint(0, 3)
#     print("r =", r)

#     if monster[r] - power < 0 :
#         monster[r] = 0
#         print("게임종료")
#         i = 5

#     else :
#         monster[r] -= power
#     print(r, "번째 몬스터 공격 :", monster)
#     i += 1 

# [1차]
# # 횟수 5번
# count = 0

# # while 무한반복문
# # count값이 5가되어야 반복을 종료함
# run = True
# while run:
#     if count == 5:
#         run = False # 반복문 종료

#     # 인덱스의 길이4 - 1 = 마지막 리스트의 위치
#     # 0, 1, 2, 3
#     r = random.randint(0, len(monster) - 1)
#     # 예시 3
#     if monster[r] > 0:
#         # 몬스터[] - power = 몬스터의 hp - 공격력
#         # 공격 후 hp의 값이 0보다 작으면 몬스터 hp의 값이 0이되는 조건
#         if monster[r] - power < 0:
#             monster[r] = 0
#         else:
#             # 몬스터hp - 공격력 > 0 보다 높으면
#             # 몬스터[] = 몬스터hp - 공격력
#             # 공격 후 hp의 값이 0보다 높으면 몬스터 hp는 남아있는 값을 따른다.
#             monster[r] -= power

#         print(r, "번째 몬스터 공격!", monster)
#         count += 1
#         # 단, 체력이 0인 몬스터는 더이상 내려가지않는다를 위한 조건 
#     elif monster[r] == 0:
#         print("체력이 0인 몬스터입니다. 다시 선택해주세요!")
    
