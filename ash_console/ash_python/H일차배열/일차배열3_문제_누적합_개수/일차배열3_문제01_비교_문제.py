'''
    [문제]
        [조건1] 리스트에 랜덤숫자(1~100) 5개를 추가한다.
        [조건2] 리스트의 숫자중 50보다 큰값들만 출력
        [조건3] 위조건의 값들의 누적합을 출력
        [조건4] 위조건의 개수 출력 
       
    [예시]
        a = [1, 83, 22, 77 ,19]
        비교 = 50
        출력 : 83, 77
        합 : 160
        개수 : 2
'''
import random

# [1114]
# a = []
# result = []
# total = 0 
# count = 0

# for i in range(5) :
#     a.append(random.randint(1, 100))

#     if a[i] > 50 :
#         # print(a[i])
#         result.append(a[i])
#         total += a[i]
#         count += 1

# print("a =", a)
# print("50보다 큰 수 = ",result)
# print("total =", total)
# print("count =", count)

# [1차]
# a = []
# size = 5 
# total = 0
# count = 0
# result = []

# for i in range(size) :
#     a.append(random.randint(1,100))

#     if a[i] > 50 :
#         # print(a[i], end = " ")
#         result.append(a[i])
#         total += a[i]
#         count += 1 
# # print()
# print("a =", a)
# print ("비교 = 50")
# print("출력 =", result)
# print("합 =", total)
# print("개수 =", count)



