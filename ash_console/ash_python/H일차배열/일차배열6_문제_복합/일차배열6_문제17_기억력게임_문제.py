'''
     [문제]
      1. 같은 숫자가 적혀있는 카드 2장씩 5세트가 있다. (총10장)
      2. front는 카드를 엎어놓은 상태를 뜻한다. 
      3. 먼저 front를 셔플한다. 
      4. front에 있는 카드 2개를 랜덤으로 선택한다. (마우스가 없으므로 인덱스로 선택)
      5. 선택한 카드 2장의 내용이 같으면 back에 복사해서 맞춘 걸 표시한다. 
         back에 모든 글자가 채워지면 게임은 종료된다.
         
      6. 같은 인덱스 선택할 수 없다. 
      7. 이미 선택한 자리를 또 선택할 수 없다. 
'''
# [1120]
# import random

# front = [10,10,20,20,30,30,40,40,50,50]
# back = [0,0,0,0,0,0,0,0,0,0]
# size = len(front) - 1 

# for i in range(100) :
#    r = random.randint(0, size)
#    temp = front[0]
#    front[0] = front[r]
#    front[r] = temp

# print(front) 

# count = 0
# while True :
#    idx1 = random.randint(0, size)
#    idx2 = random.randint(0, size)
#    print(idx1, idx2)

#    if idx1 == idx2 :
#       continue

#    if front[idx1] == front[idx2] and back[idx1] == 0 and back[idx2] == 0 : 
#       back[idx1] = front[idx1]
#       back[idx2] = front[idx2]
#       count += 1 
#    else :
#       continue

#    if count == len(back) // 2  : 
#       break

# print(front)
# print(back)

# [1116]
# front = [10,10,20,20,30,30,40,40,50,50]
# back = [0,0,0,0,0,0,0,0,0,0]
# last_idx = len(front) - 1

# for i in range(len(front)) :
#    idx1 = random.randint(0, len(front) - 1)
#    idx2 = random.randint(0, len(front) - 1)

#    temp = front[idx1]
#    front[idx1] = front[idx2]
#    front[idx2] = temp

# print(front)

# count = 0
# while True :
#    if count == len(back) // 2 :
#       break

#    idx1 = random.randint(0, len(front) - 1)
#    idx2 = random.randint(0, len(front) - 1)
#    # print(idx1, idx2, front[idx1], front[idx2])

#    if idx1 == idx2 :
#       continue
#    if front[idx1] != front[idx2] :
#       continue

#    if front[idx1] == front[idx2] and back[idx1] == 0 and back[idx2] == 0 :
#       back[idx1] = front[idx1]
#       back[idx2] = front[idx2]
#       count += 1  

# print(back)


# [1차]
# # 셔플
# for i in range(100) :
#    r1 = random.randint(0, last_idx)
#    r2 = random.randint(0, last_idx)
#    # print(r1, r2)

#    temp = front[r1]
#    front[r1] = front[r2]
#    front[r2] = temp

# # print(front)

# count = 0
# # 무한반복
# while True :
#    # 종료식 / 2개씩 값을 채우기때문에 리스트 길이의 절반값과 카운트 값이 동일하면 반복문을 종료한다.
#    if count == len(front) // 2 :
#       break

#    idx1 = random.randint(0, last_idx)
#    idx2 = random.randint(0, last_idx)
#    print(idx1, idx2)

#    # 같은 인덱스를 선택할 수 없다.
#    if idx1 != idx2 :
#       # back의 인덱스 값이 비어있고 front 인덱스의 값이 같으면
#       if back[idx1] == 0 and back[idx2] == 0 and front[idx1] == front[idx2] :
#          back[idx1] = front[idx1]
#          back[idx2] = front[idx2]
#          count += 1 

#          print("front =", front)
#          print("back =", back)