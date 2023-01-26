'''
   [문제]
      member는 어떤회원의 어제까지 상품 구입 리스트이다. 
      orderList는 오늘 주문한 아이템 목록이다. 
      member 에 orderList 의 주문량을 추가하시오. 
      중복되는 아이템이면 개수를 1증가하시오.
      새로은 아이템이면 항목을 추가하고 개수를 1증가하시오.
   [정답]
      {'새우깡': 12, '감자깡': 6, '칸쵸': 7, '빼빼로': 2, '감자칩': 1}
'''

member = {"새우깡" : 10 , "감자깡" : 4, "칸쵸" : 6}

orderList = ["새우깡" , "감자깡" ,"감자깡" , "새우깡" , "빼빼로" , "빼빼로" , "감자칩" , "칸쵸"]

for i in range(len(orderList)):
   order = orderList[i]
   if order in member:
      member[order] += 1
   else:
      member[order] = 1
print(member)

