'''
    [문제]
        [1] 1~50까지 반복한다.
        [2] 3이나 6이나 9가 없는 수 중 짝수만 a리스트에 추가하시오.
    [정답]
        a = [2, 4, 8, 10, 12, 14, 18, 20, 22, 24, 28, 40, 42, 44, 48, 50]
'''
'''
조건1 : 1~ 50반복
조건2 : 3, 6, 9,가 없는 수
조건3 : 조건2중 짝수만
'''
a = []
size = 50

# [1114]
# for i in range(size) :
#     i += 1 
#     십 = i // 10 
#     일 = i % 10

#     if i % 2 == 0 :
#         if (일 != 3 and 일 != 6 and 일 != 9) and (십 != 3 and 십 != 6 and 십 != 9) :
#             a.append(i)
# print(a)

# [2차]
# for i in range(size) :
#     # a.append(i)
#     i += 1 
#     십 = i // 10 
#     일 = i % 10
    
#     if i % 2 == 0 :
#         if 십 != 3 and 십 != 6 and 십 != 9 and 일 != 3 and 일 != 6 and 일 != 9 :
#             a.append(i) 
    
# print(a)

# [1차]
# for i in range(size) :
#     i += 1 
#     x = i // 10
#     y = i % 10

#     if i % 2 == 0 :
#         if x != 3 and x != 6 and x != 9 and y != 3 and y != 6 and y != 9:
#             a.append(i)
# print(a)
