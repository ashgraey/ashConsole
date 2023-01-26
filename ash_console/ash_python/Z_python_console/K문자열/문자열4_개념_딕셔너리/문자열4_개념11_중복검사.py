'''
    [문제]
        itemList은 쇼핑몰 판매상품데이터이다.
        itemName 는 상품이름이다.
        price는 아이템 가격이다.
        
        orderList는 오늘 주문 목록이다. 
        ordernumber 는 주문번호이다. 
        orderid 는 주문한 회원 id 이다.
        itemName 는 주문한 상품이름이다. 
        count 는 주문한 상품개수이다. 

        cancleList 는 주문취소 목록이다. 
        canclenumber 는 주문을 취소한 번호이다. 

        취소한 상품이름을 출력하시오.단, 중복되면 한번만 출력하시오.    
    [정답]   
        ['바나나', '딸기']
'''

orderList = [
    {"ordernumber" : 100001 , "orderid" : "qwer1234" , "itemname" : "사과" , "count" : 3},
    {"ordernumber" : 100002 , "orderid" : "pythongood" , "itemname" : "딸기" , "count" : 6},
    {"ordernumber" : 100003 , "orderid" : "testid" , "itemname" : "바나나" , "count" : 4},
    {"ordernumber" : 100004 , "orderid" : "pythongood" , "itemname" : "사과" , "count" : 2},
    {"ordernumber" : 100005 , "orderid" : "testid" , "itemname" : "바나나" , "count" : 7},
    {"ordernumber" : 100006 , "orderid" : "qwer1234" , "itemname" : "사과" , "count" : 2}, 
    {"ordernumber" : 100007 , "orderid" : "testid" , "itemname" : "사과" , "count" : 3}, 
]
cancleList = [
    {"canclenumber" : 100003 },
    {"canclenumber" : 100002 },
    {"canclenumber" : 100005 },
]
totalList = []
for i in range(len(cancleList)):
    cancle = cancleList[i]
    for j in range(len(orderList)):
        order = orderList[j]
        if cancle["canclenumber"] == order["ordernumber"]:
            check = False
            for k in range(len(totalList)):
                if totalList[k] == order["itemname"]:
                    check = True
                    break
            if check == False:              
                totalList.append( order["itemname"])
print(totalList)                

