"""
    [문제]
        아래 리스트들은 학생들의 데이터이다. 
        학생두명의 국어 점수가 서로 바뀌어서 잘못 저장되었다. 
        랜덤으로 번호두개를 저장후 각 번호의 해당하는 국어점수를  교환후 출력하시오.

    [예시]
        1001 , 1003
        stkor = [30,20,10,40]
"""
import random

# [1116]
# stno = [1001, 1002, 1003, 1004]
# stname = ["김철수" , "이만수" , "신정아" , "이영희"]
# stkor = [10 , 20 , 30 , 40]
# steng = [60 , 80 , 32 , 13]

# r1 = random.randint(1001, 1004)
# r2 = random.randint(1001, 1004)
# print(r1, r2)

# idx1 = 0 
# idx2 = 0
# for i in range(len(stno)) :
#     if stno[i] == r1 :
#         idx1 = i
#     if stno[i] == r2 :
#         idx2 = i

# print(idx1, idx2)

# temp = stkor[idx1]
# stkor[idx1] = stkor[idx2]
# stkor[idx2] = temp

# print(stkor)

# [1차]
# # 교환할 값의 랜덤 학생번호
# r1 = random.randint(1001, 1004)
# r2 = random.randint(1001, 1004)
# print(r1, r2)

# # 인덱스의 번호 찾기
# idx1 = 0
# idx2 = 0
# for i in range(len(stno)) :
#     if stno[i] == r1 :
#         idx1 = i
#     if stno[i] == r2 :
#         idx2 = i
# print("idx =", idx1, idx2)

# # 값교환
# temp = 0
# temp = stkor[idx1]
# stkor[idx1] = stkor[idx2]
# stkor[idx2] = temp

# print(stkor)
# print(steng)

# # total = 0
# # first = 0  
# # for i in range(len(stkor)) :
# #     total = stkor[i] + steng[i]
# #     print(total, end = " ")

    
# #     if first < total :
# #         first = total
# # print()
# # print("1등 =", first)