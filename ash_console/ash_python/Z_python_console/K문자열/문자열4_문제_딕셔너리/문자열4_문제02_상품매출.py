'''
    [문제]
        memberList는 회원목록데이터이다.
        number 는 회원 번호이다. 
        id 는 회원아이디이다.

        itemList은 쇼핑몰 판매상품데이터이다.
        itemName 는 상품이름이다.
        price는 아이템 가격이다.
        
        orderList는 오늘 주문 목록이다. 
        orderid 는 주문한 회원 id 이다.
        itemname 는 주문한 상품이름이다. 
        count 는 주문한 상품개수이다. 

        각 회원별 주문 총액을 구하시오.
    [정답]
        {'id': 'qwer1234', 'total': 4400}
        {'id': 'pythongood', 'total': 28000}
        {'id': 'testid', 'total': 16000}
'''

memberList = [
    {"number" : 1001 , "id" : "qwer1234" },
    {"number" : 1002 , "id" : "pythongood"},
    {"number" : 1003 , "id" : "testid"},
]
itemList = [
    {"itemname" : "사과" , "price" : 1100},
    {"itemname" : "바나나" , "price" : 2000},
    {"itemname" : "딸기" , "price" : 4300},
]
orderList = [
    {"orderid" : "qwer1234" , "itemname" : "사과" , "count" : 3},
    {"orderid" : "pythongood" , "itemname" : "딸기" , "count" : 6},
    {"orderid" : "testid" , "itemname" : "바나나" , "count" : 1},
    {"orderid" : "pythongood" , "itemname" : "사과" , "count" : 2},
    {"orderid" : "testid" , "itemname" : "바나나" , "count" : 7},
    {"orderid" : "qwer1234" , "itemname" : "사과" , "count" : 1}, 
]

totalList = []
for i in range(len(memberList)):
    total = {"id" : memberList[i]["id"] , "total" : 0}
    totalList.append(total)
# print(totalList)

for i in range(len(orderList)):
    order = orderList[i]
    for j in range(len(memberList)):
        member = memberList[j]       
        if order["orderid"] == member["id"]:
            for k in range(len(itemList)):
                item = itemList[k]
                if item["itemname"] == order["itemname"]:
                    totalList[j]["total"] += (item["price"] * order["count"])
                    
for i in range(len(totalList)):
    print(totalList[i])




