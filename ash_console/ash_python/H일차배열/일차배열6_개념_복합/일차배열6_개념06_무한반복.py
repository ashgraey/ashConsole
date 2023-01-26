'''
    [문제]
        [조건1] 리스트에 랜덤숫자(1~100) 5개를 추가한다.
        [조건2] 랜덤으로 홀수만 저장한다.   
'''
'''
    문제만 보면 5번 반복하면 될 것 같지만 함정이다. 
    홀수만 저장이기 때문에 무한반복을 사용해야 한다.
'''
import random

a = []

i = 0
while i < 5:
    r = random.randint(1, 100)
    # print(r) # 주석을 해제하고 반복문을 실행하면 매번 반복 횟수가 다르다.
    # r이 홀수일때 실행, 조건이 참이여야 i 증가식 실행
    # 조건에 부합해야 반복횟수가 올라가기 떄문에 사실상 무한반복이고 좀 더 직관적으로 코드를 볼수있다. 
    if r % 2 == 1:
        a.append(r)
        i += 1 # 이 부분이 중요하다. 
    
print(a)

# count = 0
# run = 1 
# while run == 1 :
#     r = random.randint(1, 100)
#     print("랜덤 =", r)

#     if r % 2 == 1 :
#         a.append(r)
#         count += 1 
    
#     if count == 5 :
#         run = 0

# print(a)