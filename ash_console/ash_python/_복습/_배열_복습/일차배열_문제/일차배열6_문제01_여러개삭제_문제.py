'''
    [문제]  
        아래 a리스트는 순서대로 값이 저장되어있다.
        랜덤(1~100)숫자 하나를 저장 후,
        랜덤 값보다 작은 값은 전부 a리스트에서 삭제하시오.
    [정답]

'''
import random

a = [10, 20, 30, 40, 50, 60]

# [1116]
# r = random.randint(1, 100)
# print("r =", r)

# i = 0 
# while True : 
#     if i == len(a) :
#         break

#     if a[i] < r :
#         a.remove(a[i])
#         i -= 1
#     i += 1 
# print(a)
    
# [1차]
# r = random.randint(1, 100)
# # r = 4 
# print("r =", r)

# i = 0 
# while True : 
#     if i == len(a) :
#         break
    
#     # a리스트의 값과 r의 값 비교
#     # r보다 작으면 안에 값을 제거
#     if a[i] < r :
#         a.remove(a[i])
#         i -= 1 
#     i += 1 
# print(a)