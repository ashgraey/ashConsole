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

        취소한 상품이름별 총가격을 구하시오.
        
    [정답]   
        [{'itemname': '바나나', 'total': 22000}, 
        {'itemname': '딸기', 'total': 25800}]
'''

itemList = [
    {"itemname" : "사과" , "price" : 1100},
    {"itemname" : "바나나" , "price" : 2000},
    {"itemname" : "딸기" , "price" : 4300},
]
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
            price = 0
            for k in range(len(itemList)):
                item = itemList[k]
                if item["itemname"] == order["itemname"]:
                    price = item["price"] * order["count"]
            check = False
            for k in range(len(totalList)):
                total = totalList[k]
                if total["itemname"] == order["itemname"]:
                    total["total"] += price
                    check = True
                    break
            if check == False:
                temp = {"itemname" : order["itemname"], "total" : price}
                totalList.append(temp)
print(totalList)                






