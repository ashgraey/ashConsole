'''
    [문제]
        member는 회원목록이다. 번호와 아이디가 기록되어있다.
        item은 쇼핑몰 판매상품이다. 상품이름과 가격이 기록되어있다.
        
        order는 오늘 주문 목록이다. 주문한회원아이디와 아이템이름 그리고, 주문개수가 기록되어있다. 
        오늘의 매출을 출력하시오.
        
        Member 클래스와 Item 클래스 와 Order클래스를 만들고,
        문자열을 잘라 각가의 클래스에 저장후 문제를 푸시오.
    [정답]
        33200
'''
class Member:
    number = int()
    id = str()
    
class Item:
    name = str()
    price = int()

class Order:
    id = str()
    item_name = str()
    count = 0

member_data = "1001,qwer1234/1002,pythongood/1003,testid"
item_data = "사과,1100/바나나,2000/딸기,4300"
order_data = "qwer1234,사과,3/phthongood,바나나,2/qwer1234,딸기,5/testid,사과,4"

memberList = []
itemList = []
orderList = []

token1 = member_data.split("/")
for i in range(len(token1)):
    token2 = token1[i].split(",")
    m = Member()
    m.number = int(token2[0])
    m.id = token2[1]
    memberList.append(m)
    
token1 = item_data.split("/")
for i in range(len(token1)):
    token2 = token1[i].split(",")
    it = Item()
    it.name = token2[0]
    it.price = int(token2[1])
    itemList.append(it)
    
token1 = order_data.split("/")
for i in range(len(token1)):
    token2 = token1[i].split(",")
    ord = Order()
    ord.id = token2[0]
    ord.item_name = token2[1]
    ord.count = int(token2[2])
    orderList.append(ord)

# 매출구하기
total = 0
for i in range(len(orderList)):
    order = orderList[i]
    for j in range(len(itemList)):
        item = itemList[j]
        if order.item_name == item.name :
            print(order.count , " " , item.price)
            total += (order.count * item.price)
      
print(total)
        