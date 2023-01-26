'''
    [문제] 클래스로 변경하시오.
        member는 회원목록이다.
        item은 쇼핑몰 판매상품이다.
        order는 오늘 주문목록이다.
        회원별 아이템 주문개수를 출력하시오.
    [정답]
        이만수: 고래밥 3
        김철민: 고래밥 1 칸쵸 1
        이영희: 새우깡 2 칸쵸 1
'''

member  = "3001/이만수,3002/김철민,3003/이영희"
item    = "1001/고래밥,1002/새우깡,1003/칸쵸"
order   = "3001,1001/3001,1001/3003,1002/3002,1003/3001,1001/3003,1002/3003,1003/3002,1001"

temp = member.split(",")
memberList = []
for i in range(len(temp)):
    info = temp[i].split("/")
    memberList.append(info)
print(memberList)

temp = item.split(",")
itemList = []
for i in range(len(temp)):
    info = temp[i].split("/")
    itemList.append(info)
print(itemList)

temp = order.split("/")
orderList = []
for i in range(len(temp)):
    info = temp[i].split(",")
    orderList.append(info)
print(orderList)

print("------------------------------------")

countList = []
for i in range(len(memberList)):
    temp = [0, 0, 0]
    for j in range(len(orderList)):
        if memberList[i][0] == orderList[j][0]:
            for k in range(len(itemList)):
                if itemList[k][0] == orderList[j][1]:
                    temp[k] += 1
    countList.append(temp)
print(countList)

for i in range(len(memberList)):
    print(memberList[i][1], end=": ")
    for j in range(len(itemList)):
        if countList[i][j] > 0:
            print(itemList[j][1], countList[i][j], end=" ")
    print()
        