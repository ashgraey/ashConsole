'''
    [문제]
        
        orderList는 오늘 주문 목록이다. 
        ordernumber 는 주문번호이다. 
        orderid 는 주문한 회원 id 이다.
        itemName 는 주문한 상품이름이다. 
        count 는 주문한 상품개수이다. 

        cancleList 는 주문취소 목록이다. 
        canclenumber 는 주문을 취소한 번호이다. 

        orderList 에서 cancleList 의 번호를 전부 삭제하시오.
    [정답]      
        {'ordernumber': 100001, 'orderid': 'qwer1234', 'itemName': '사과', 'count': 3}
        {'ordernumber': 100004, 'orderid': 'pythongood', 'itemName': '사과', 'count': 2}
        {'ordernumber': 100006, 'orderid': 'qwer1234', 'itemName': '사과', 'count': 1}
'''

orderList = [
    {"ordernumber" : 100001 , "orderid" : "qwer1234" , "itemName" : "사과" , "count" : 3},
    {"ordernumber" : 100002 , "orderid" : "pythongood" , "itemName" : "딸기" , "count" : 6},
    {"ordernumber" : 100003 , "orderid" : "testid" , "itemName" : "바나나" , "count" : 1},
    {"ordernumber" : 100004 , "orderid" : "pythongood" , "itemName" : "사과" , "count" : 2},
    {"ordernumber" : 100005 , "orderid" : "testid" , "itemName" : "바나나" , "count" : 7},
    {"ordernumber" : 100006 , "orderid" : "qwer1234" , "itemName" : "사과" , "count" : 1}, 
]
cancleList = [
    {"canclenumber" : 100003 },
    {"canclenumber" : 100002 },
    {"canclenumber" : 100005 },
]

# 여러개 삭제는 리스트 개수가 계속 변하기때문에 아래와 같이 해야한다. 
while True:
    if len(cancleList) == 0:
        break
    cancle = cancleList[0]
    for i in range(len(orderList)):
        order = orderList[i]
        if order["ordernumber"] == cancle["canclenumber"]:
            del(orderList[i])
            break
    del(cancleList[0])

for i in range(len(orderList)):
    print(orderList[i])
print()




