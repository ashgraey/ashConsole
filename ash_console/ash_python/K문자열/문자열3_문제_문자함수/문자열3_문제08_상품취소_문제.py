'''
    [문제]
        member는 회원목록이다. 번호와 아이디가 기록되어있다.
        item은 쇼핑몰 판매상품이다. 상품이름과 가격이 기록되어있다.
        
        order는 오늘 주문 목록이다. 주문한회원아이디와 아이템이름 그리고, 주문개수가 기록되어있다. 
        cancel은 주문취소 목록이다. 취소한회원아이디와 아이템이름 그리고, 주무개수가 기록되어있다.
        오늘의 매출을 출력하시오.
    [정답]
        7700
'''

member = "qwer1234,pythongood,testid"
item   = "사과,1100/바나나,2000/딸기,4300"
order  = "qwer1234,사과,3/phthongood,바나나,2/qwer1234,딸기,5/testid,사과,4"
cancle = "qwer1234,딸기,5/phthongood,바나나,2"

# 0127
# 구조 : orderList 매출총합 - cancleList 취소총합 = 오늘매출
# 리스트로 변환
member = member.split(",")
print(member)

print()
item = item.split("/")
itemList = []
for i in range(len(item)) :
    item[i] = item[i].split(",")
    itemList.append(item[i])
    print(itemList[i])

print()
order = order.split("/")
orderList = []
for i in range(len(order)) :
    order[i] = order[i].split(",")
    orderList.append(order[i])
    print(orderList[i])

print()
cancle = cancle.split("/")
cancleList = []
for i in range(len(cancle)) :
    cancle[i] = cancle[i].split(",")
    cancleList.append(cancle[i])
    print(cancleList[i])

# order total
total = 0
for i in range(len(orderList)) :
    for j in range(len(itemList)) :
        if orderList[i][1] == itemList[j][0] :
            total += (int(orderList[i][2]) * int(itemList[j][-1]))
print(total)

# cancle total
cancleTotal = 0
for i in range(len(cancleList)) :
    for j in range(len(itemList)) :
        if cancleList[i][1] == itemList[j][0] :
            cancleTotal += (int(cancleList[i][2]) * int(itemList[j][-1]))
print(cancleTotal)
print(total - cancleTotal)
    


# 1차
# # member split
# member = member.split(',')
# print("member = ", member)

# # 원하는 인덱스 형변환 후 저장
# temp = item.split("/")
# itemList = []
# for i in range(len(temp)) :
#     info = temp[i].split(",")
#     info[1] = int(info[1])
#     itemList.append(info)

# print("item = ")
# for i in range(len(itemList)) :
#     print(itemList[i])
# # print(info)

# # order split, int
# temp = order.split("/")
# orderList = []
# for i in range(len(temp)) :
#     info = temp[i].split(',')
#     info[2] = int(info[2])
#     orderList.append(info)
# print("order = ")
# for i in range(len(orderList)) :
#     print(orderList[i])

# # cancel split, int
# temp = cancel.split('/')
# cancelList = []
# for i in range(len(temp)) :
#     info = temp[i].split(",")
#     info[2] = int(info[2])
#     cancelList.append(info)
# print("cancel = ")
# for i in range(len(cancelList)) :
#     print(cancelList[i])

# # order - cancel 
# for i in range(len(orderList)) :

#     for j in range(len(cancelList)) :
#         if orderList[i][-2] == cancelList[j][-2] :
#             orderList[i][-1] -= cancelList[j][-1]
# print()
# print("cancel orderList = ")
# for i in range(len(orderList)) :
#     print(orderList[i])

# # price and total
# total = 0
# for i in range(len(orderList)) :

#     for j in range(len(itemList)) :
#         if orderList[i][1] == itemList[j][0] :
#             price = (orderList[i][-1] * itemList[j][-1])
#             print(price, end = " ")
#     total += price
# print()
# print("매출 = ", total)