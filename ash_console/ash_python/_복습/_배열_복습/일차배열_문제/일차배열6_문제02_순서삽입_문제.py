'''
    [문제]  
        아래 a리스트는 순서대로 값이 저장되어있다.
        랜덤(1~70)숫자 하나를 저장 후,
        a리스트의 값들 사이에 저장하려고 한다. 
        저장조건은 a리스트의 바로 앞의 값 보다는 크고 
        바로 뒤의 값 보다는 이하인 위치에 삽입 후 출력하시오.
    [예시]
        r = 54
        a = [10,20,30,40,50,54,60]

'''
import random

a = [10, 20, 30, 40, 50, 60]

r = random.randint(1,70)
# r = 10
print("r =", r)

idx = -1 
# 저장조건 : a리스트의 바로 앞의 값보다는 크고 바로 뒤의 값보다는 이하인 위치
for i in range(len(a) - 1)  :
    if a[i] < r <= a[i + 1] :
        idx = i + 1
    elif r <= 10 :
        idx = 0 
print("idx =", idx)    

# idx의 값이 변함이 없으면 마지막 인덱스에 r의 값을 추가
if idx == -1 : 
    a.append(r)

else : 
    a.append(r)
    i = len(a) - 1
    while i > idx :
        a[i] = a[i - 1]
        i -= 1
    a[idx] = r
print(a)

# # r = random.randint(1, 70)
# r = 33
# print("r =", r)

# # 왜 -1이여야 하는가?
# idx = -1 
# for i in range(len(a) - 1) :
#     # 랜덤 값의 위치값을 찾는 조건
#     # a리스트의 바로 앞의 값 보다는 크고 바로 뒤의 값 보다는 이하 
#     # 위치값의 바로 뒤에 r값을 넣어야 하기에 idx = i + 1 
#     if a[i] < r <= a[i + 1] : 
#         idx = i + 1 
# print("idx =", idx)

# if idx == -1 :
#     a.append(r)

# else :
#     a.append(r)
#     i = len(a) - 1 
#     while i > idx :
#         a[i] = a[i - 1]
#         i -= 1 
#     a[idx] = r 
# print(a)
 