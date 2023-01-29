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

# 0129
tempList = []
for i in range(len(cancleList)) :
    cancle = cancleList[i]
    temp = {}
    for j in range(len(orderList)) :
        order = orderList[j]
        if cancle["canclenumber"] == order["ordernumber"] :
            name = order["itemname"]
            cnt = order["count"]
            for k in range(len(itemList)) :
                item = itemList[k]
                if order["itemname"] == item["itemname"] :
                    total = cnt * item["price"]

            temp = {"itemname" : name, "total" : total}
            tempList.append(temp)

# print(tempList)

# 중복찾기
for i in range(len(tempList)) :
    for j in range(i, len(tempList)) :
        if i != j and tempList[i]["itemname"] == tempList[j]["itemname"] :
            total = (tempList[i]["total"] + tempList[j]["total"])
            tempList[i]["total"] = total

del tempList[-1]
print(tempList)


# 1차
# totalList = []
# for i in range(len(cancleList)) :
#     cancle = cancleList[i]
#     n = ""

#     for j in range(len(orderList)) :
#         order = orderList[j]
#         if cancle["canclenumber"] == order["ordernumber"] :
#             for k in range(len(itemList)) :
#                 item = itemList[k]
#                 if order["itemname"] == item["itemname"] :
#                     n = item["itemname"]
#                     price = item["price"] * order["count"]
#                     total = {"itemname" : n, "total" : price}
#                     totalList.append(total)

#             print(n, price)

# # for i in range(len(totalList)) :
# #     print(totalList[i])

# for i in range(len(totalList)) :
#     info1 = totalList[i]
#     ck = False
#     for j in range(len(totalList)) :
#         info2 = totalList[j]
#         if i != j and info1["itemname"] == info2["itemname"] :
#             ck = True
#             break 

#     if ck == True :
#         info1["total"] += info2["total"]
#         del(totalList[j])
#         break
# # 출력
# for i in range(len(totalList)) :
#     print(totalList[i])






