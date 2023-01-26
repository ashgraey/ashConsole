'''
  [문제]
    0~4 사이의 랜덤 숫자를 저장해 a리스트에서 그 위치의 값이
    최대값인지 검사한다.
    만약 최대값이면 그 위치의 값을 0으로 바꾸고,
    전부 0이되면 종료한다. 

    과정을 전부 출력하시오.
  [예]
      랜덤 : 3
      [11, 87, 42, 0, 24]

      랜덤 : 0
      [11, 87, 42, 0, 24]   <- 최대값이 아니므로 그대로 유지

      랜덤 : 1
      [11, 0, 42, 100, 24]

      ...
      
  '''
import random

a = [11, 87, 42, 100, 24]

# 횟수 ? 
# [1122]
# count = 0 
# while True :
#   r = random.randint(0, 4) 
#   print("랜덤 : ", r)

#   check = False
#   max = 0
#   # 리스트의 최댓값
#   for j in range(len(a)) :
#     if max < a[j] :
#       max = a[j]
      
#   # 리스트의 최댓값 == a[r]의 값이 같으면 check에 True 저장
#   if max == a[r] :
#     check = True 
  
#   if check == True :
#     a[r] = 0
#     count += 1 
#   else : 
#     continue

#   print(a)
  
#   if count == 5 : 
#     break



  

  