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
import random

front = [10,10,20,20,30,30,40,40,50,50]
back = [0,0,0,0,0,0,0,0,0,0]

for i in range(100):
   index1 = random.randint(0, len(front) - 1)
   index2 = random.randint(0, len(front) - 1)

   temp = front[index1]
   front[index1] = front[index2]
   front[index2] = temp
# print(front)

count = 0
while True:
   if count == len(front)//2:
      break

   index1 = random.randint(0, len(front) - 1)
   index2 = random.randint(0, len(front) - 1)
   print(index1, index2)

   if index1 != index2:
      if back[index1] == 0 and back[index2] == 0 and front[index1] == front[index2]:
         back[index1] = front[index1]
         back[index2] = front[index2]
         count += 1

         print("front =", front)
         print("back =", back)
      