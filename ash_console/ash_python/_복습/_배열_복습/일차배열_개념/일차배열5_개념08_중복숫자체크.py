'''
   [문제]
      a리스트에 랜덤(1~4) 숫자 4개를 저장한다. 
      단, 중복없는 숫자로 저장한다.
   
   [예시]
      [1,4,2,3]
'''
# a리스트에 랜덤(1~4) 숫자 4개를 저장한다. 
# 단, 중복없는 숫자로 저장한다.

   
import random

[1115]
a = [0, 0, 0, 0]
check = [False, False, False, False]

count = 0 
while True :
   r = random.randint(0, 3)

   if check[r] == False :
      a[count] = r + 1 
      check[r] = True
      count += 1 
   
   if count == 4 :
      break

print(a)

# [2차]
# count = 0
# while True:
#    r = random.randint(0, 3)

#    # 중복인지 검사하는 조건
#    if check[r] == False:
#       a[count] = r + 1
#       check[r] = True
#       count += 1

#    if count == 4:
#       break

# [1차]
# count = 0
# while True :  
#    r = random.randint(1, 4)

#    if check[r] == False:
#       a[count] = r + 1 # a[0] = r + 1
#       check[r] = True
#       count += 1
   
#    if count == 4:
#       break

# print(a)


