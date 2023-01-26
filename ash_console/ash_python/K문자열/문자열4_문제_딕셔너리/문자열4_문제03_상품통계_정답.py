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
        
        각아이템별로 구입한 회원이름과 개수를 구하시오.
        단, 주문목록에 없는 아이템은 구하지않는다. 
    [정답]
        {'itemname': '고래밥', 'name': '이만수', 'count': 1}
        {'itemname': '고래밥', 'name': '김철민', 'count': 1}
        {'itemname': '새우깡', 'name': '이만수', 'count': 1}
        {'itemname': '새우깡', 'name': '김철민', 'count': 1}
        {'itemname': '새우깡', 'name': '이영희', 'count': 3}
        {'itemname': '감자깡', 'name': '이영희', 'count': 1}
        {'itemname': '감자깡', 'name': '이만수', 'count': 1}
        {'itemname': '칸쵸', 'name': '이영희', 'count': 1}
        {'itemname': '빼빼로', 'name': '박민재', 'count': 1}
        {'itemname': '빼빼로', 'name': '이만수', 'count': 1}
        {'itemname': '고구마깡', 'name': '김철민', 'count': 2}
'''
memberList = [
    {"membernumber" : 3001 , "name" : "이만수"},
    {"membernumber" : 3002 , "name" : "김철민"},
    {"membernumber" : 3003 , "name" : "이영희"},
    {"membernumber" : 3004 , "name" : "조성아"},
    {"membernumber" : 3005 , "name" : "박민재"},
]
itemList = [
    {"itemnumber" : 100001 , "itemname" : "고래밥"},
    {"itemnumber" : 100002 , "itemname" : "새우깡"},
    {"itemnumber" : 100003 , "itemname" : "감자깡"},
    {"itemnumber" : 100004 , "itemname" : "칸쵸"},
    {"itemnumber" : 100005 , "itemname" : "오징어땅콩"},
    {"itemnumber" : 100006 , "itemname" : "빼빼로"},
    {"itemnumber" : 100007 , "itemname" : "고구마깡"},
]
orderList = [
    {"membernumber" : 3001 , "itemnumber" : 100001},
    {"membernumber" : 3001 , "itemnumber" : 100002},
    {"membernumber" : 3003 , "itemnumber" : 100004},
    {"membernumber" : 3002 , "itemnumber" : 100007},
    {"membernumber" : 3003 , "itemnumber" : 100003},
    {"membernumber" : 3005 , "itemnumber" : 100006},
    {"membernumber" : 3002 , "itemnumber" : 100002},
    {"membernumber" : 3001 , "itemnumber" : 100007},
    {"membernumber" : 3003 , "itemnumber" : 100002},
    {"membernumber" : 3002 , "itemnumber" : 100001},
    {"membernumber" : 3001 , "itemnumber" : 100003},
    {"membernumber" : 3003 , "itemnumber" : 100002},
    {"membernumber" : 3002 , "itemnumber" : 100007},
    {"membernumber" : 3001 , "itemnumber" : 100006},
    {"membernumber" : 3003 , "itemnumber" : 100002},
]
totalList = []

for i in range(len(itemList)):
    name = ""
        
    item = itemList[i]
    for j in range(len(orderList)):
        order = orderList[j]
        for k in range(len(memberList)):
            member = memberList[k]
            if member["membernumber"] == order["membernumber"]:
                name = member["name"]
                break 
        if item["itemnumber"] == order["itemnumber"]:           
            check = False
            for k in range(len(totalList)):
                total = totalList[k]
                if total["itemname"] == item["itemname"] and name == total["name"]:
                    check = True
                    total["count"] += 1
                    break                
            if check == False:
                temp = {"itemname" : item["itemname"] , "name" :  name , "count" : 1}
                totalList.append(temp)

for i in range(len(totalList)):
    print(totalList[i])




    
    









