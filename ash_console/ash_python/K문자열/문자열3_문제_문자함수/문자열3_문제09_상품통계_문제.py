'''
    [문제]
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

# 0127

# member split
member = member.split(",")
memberList = []
for i in range(len(member)) :
    member[i] = member[i].split("/")
    member[i][0] = int(member[i][0])
    memberList.append(member[i])
    print(memberList[i])

# item split
print()
item = item.split(",")
itemList = []
for i in range(len(item)) :
    item[i] = item[i].split("/")
    item[i][0] = int(item[i][0])
    itemList.append(item[i])
    print(itemList[i])

# order split
print()
order = order.split("/")
orderList = []
for i in range(len(order)) :
    order[i] = order[i].split(",")
    order[i][0] = int(order[i][0])
    order[i][1] = int(order[i][1])
    orderList.append(order[i])
    print(orderList[i])

# 카운트 로직
cnt = []
for i in range(len(memberList)) :
    temp = [0, 0, 0]
    for j in range(len(orderList)) :
        if memberList[i][0] == orderList[j][0] :
            for k in range(len(itemList)) :
                if orderList[j][1] == itemList[k][0] :
                    temp[k] += 1
    cnt.append(temp)
print(cnt)

# 출력
for i in range(len(memberList)) :
    print(memberList[i][1], end = " : ")
    for j in range(len(cnt)) :
        if cnt[i][j] > 0 :
            print(itemList[j][1], cnt[i][j], end = " ")
    print()

# 1차
# temp = member.split(',')
# memList = []
# for i in range(len(temp)) :
#     info = temp[i].split("/")
#     info[0] = int(info[0])
#     memList.append(info)
#     # memList[i].append(0)

# print("member = ")
# for i in range(len(memList)) :
#     print(memList[i])

# # 
# temp = item.split(',')
# itemList = []
# for i in range(len(temp)) :
#     info = temp[i].split("/")
#     info[0] = int(info[0])
#     itemList.append(info)

# print("item = ")
# for i in range(len(itemList)) :
#     print(itemList[i])

# # 
# temp = order.split('/')
# # print(temp)
# orderList = []
# for i in range(len(temp)) :
#     info = temp[i].split(",")
#     info[0] = int(info[0])
#     info[1] = int(info[1])
#     orderList.append(info)

# print("order = ")
# for i in range(len(orderList)) :
#     print(orderList[i])

# # 
# for i in range(len(memList)) :

#     cnt = 0 
#     for j in range(len(orderList)) :
#         if memList[i][0] == orderList[j][0] :
#             for k in range(len(itemList)) :
#                 if orderList[j][1] == itemList[k][0] : 
#                     cnt += 1 
#                     memList[i].append(itemList[k][1])
#                     print(itemList[k][1])
#     # print(cnt)
#     # memList[i].append(itemList[])
# for i in range(len(memList)) :
#     print(memList[i])


