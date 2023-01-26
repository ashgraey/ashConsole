'''
    [문제]
        아래 a리스트는 3 x 3의 빙고 판을 표현한 것이다.
        1이 연속으로 3개이면, 빙고이다.
        즉 아래 빙고 판은 빙고가 2개이다.
        판정을 통해 빙고가 2개가 나오도록 식을 작성하시오.
'''
a = [0, 0, 1,
     0, 1, 1,
     1, 0, 1]
'''
0   1   2
3   4   5
6   7   8
'''
# [1121]
# count = 0 
# # 가로 
# for i in range(3) :
#     if a[i] == 1 and a[i + 1] == 1 and a[i + 2] == 1 :
#         count += 1 
#     i += 3
# print("가로 빙고 =", count)

# # 세로 
# count = 0 
# for i in range(3) :
#     if a[i] == 1 and a[i + 3] == 1 and a[i + 6] == 1 :
#         count += 1 
# print("세로 빙고 =", count)
# # if a[0] == 1 and a[3] == 1 and a[6] == 1 :
# #     count += 1 

# # if a[1] == 1 and a[4] == 1 and a[7] == 1 :
# #     count += 1 

# # if a[2] == 1 and a[5] == 1 and a[8] == 1 :
# #     count += 1 
# # print("세로 빙고 =", count)

# # 대각
# count = 0 
# if a[0] == 1 and a[4] == 1 and a[8] == 1 :
#     count += 1 
# if a[2] == 1 and a[4] == 1 and a[6] == 1 :
#     count += 1 

# print("대각 빙고 =",count)

# [1116]
# print(a)
# count = 0 
# for i in range(3) :
#     if a[i] == 1 and a[i + 1] == 1 and a[i + 2] == 1 :
#         count += 1 
#     i += 3 


# for i in range(3) :
#     if a[i] == 1 and a[i + 3] == 1 and a[i + 6] == 1 :
#         count += 1
#     i += 1 

# if a[0] == 1 and a[4] == 1 and a[8] == 1 :
#     count += 1
# if a[2] == 1 and a[4] == 1 and a[6] == 1 :
#     count += 1 

# print(count)


# [2차]
# count = 0 
# # 가로 겁사
# for i in range(3) :
#     if a[i] == 1 and a[i + 1] == 1 and a[i + 2] == 1 :
#         count += 1 
#     i += 3
# # print(count)

# # 세로 검사
# for i in range(3) : 
#     if a[i] == 1 and a[i + 3] == 1 and a[i + 6] == 1 :
#         count += 1 

# # 대각선 검사
# if a[2] == 1 and a[4] == 1 and a[6] == 1 :
#     count += 1

# if a[0] == 1 and a[4] == 1 and a[8] == 1 :
#     count += 1 

# print(count)

# [1차]
# print(a)
# for i in range(len(a)) :
#     if i % 2 == 0 :
#         if a[i] == 1 :
#             print("빙고")

#     if i % 3 == 2 :
#         if a[i] == 1 :
#             print("빙고")