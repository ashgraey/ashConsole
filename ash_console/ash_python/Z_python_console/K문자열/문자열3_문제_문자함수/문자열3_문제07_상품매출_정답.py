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

memberList = member.split(",")
print(memberList)

temp = item.split("/")
itemList = []
for i in range(len(temp)):
    info = temp[i].split(",")
    info[1] = int(info[1])
    itemList.append(info)
print(itemList)


temp = order.split("/")
orderList = []
for i in range(len(temp)):
    info = temp[i].split(",")
    info[2] = int(info[2])
    orderList.append(info)
print(orderList)

total = 0
for i in range(len(orderList)):
    for j in range(len(itemList)):
        if itemList[j][0] == orderList[i][1]:
            price = itemList[j][1] * orderList[i][2]
            print(price)
    total += price
print(total)