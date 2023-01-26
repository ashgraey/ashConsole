'''
    [문제]
        member는 회원목록이다. 번호와 아이디가 기록되어있다.
        item은 쇼핑몰 판매상품이다. 상품이름과 가격이 기록되어있다.
        
        order는 오늘 주문 목록이다. 주문한회원아이디와 아이템이름 그리고, 주문개수가 기록되어있다. 
        오늘의 매출을 출력하시오.
    
    [정답]
        33200
'''

member = "qwer1234,pythongood,testid"
item = "사과,1100/바나나,2000/딸기,4300"
order = "qwer1234,사과,3/phthongood,바나나,2/qwer1234,딸기,5/testid,사과,4"

# member 스플릿
memList = member.split(",")
print("member = ", memList)

# itemList 스플릿
itemList = item.split("/")
for i in range(len(itemList)) :
    itemList[i] = itemList[i].split(",")

print()
print("itemList : ")
for i in range(len(itemList)) :
    print(itemList[i])

# order split
orderList = order.split("/")
for i in range(len(orderList)) :
    orderList[i] = orderList[i].split(",") 
    orderList[i].append(0)

print()
print("orderList : ")
for i in range(len(orderList)) :
    print(orderList[i])

# orderList의 인덱스를 하나늘리고 
# 중복값을 orderList 마지막 인덱스에 가격을 저장
for i in range(len(orderList)) :
    for j in range(1, len(orderList[i])) :

        for y in range(len(itemList)) :
            for x in range(len(itemList[y])) :
                if orderList[i][j] == itemList[y][x] :
                    price = int(orderList[i][j + 1]) * int(itemList[y][x + 1])
                    # print(price)
                    orderList[i][-1] = price

# 매출 총액 출력
print()
print("orderList price pls =")
tot = 0 
for i in range(len(orderList)) :
    tot += orderList[i][-1]
    print(orderList[i])
print("매출 총액 : ", tot)