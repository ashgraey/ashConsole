'''
    [문제]
        memberList는 회원목록데이터이다.
        number 는 회원 번호이다. 
        id 는 회원아이디이다.

        itemList은 쇼핑몰 판매상품데이터이다.
        itemname 는 상품이름이다.
        price는 아이템 가격이다.
        
        orderList는 오늘 주문 목록이다. 
        orderid 는 주문한 회원 id 이다.
        itemname 는 주문한 상품이름이다. 
        count 는 주문한 상품개수이다. 

        각회원별 상품별 이름과 총가격을 구하는 함수를 만드시오. 
        단, 아무것도 주문하지않은 회원은 출력하지않는다.
    [정답]
        {'id': 'qwer1234', 'itemname': '사과', 'count': 4, 'total': 2200}
        {'id': 'pythongood', 'itemname': '딸기', 'count': 6, 'total': 4300}
        {'id': 'pythongood', 'itemname': '사과', 'count': 2, 'total': 1100}
        {'id': 'testid', 'itemname': '바나나', 'count': 8, 'total': 4000}
        {'id': 'cccddd', 'itemname': '바나나', 'count': 3, 'total': 2000}
        {'id': 'cccddd', 'itemname': '사과', 'count': 2, 'total': 1100}
       
'''
memberList = [
    {"number" : 1001 , "id" : "qwer1234" },
    {"number" : 1002 , "id" : "pythongood"},
    {"number" : 1003 , "id" : "testid"},
    {"number" : 1004 , "id" : "aaabbb"},
    {"number" : 1005 , "id" : "cccddd"},
]
itemList = [
    {"itemname" : "사과" , "price" : 1100},
    {"itemname" : "바나나" , "price" : 2000},
    {"itemname" : "딸기" , "price" : 4300},
]
orderList = [
    {"orderid" : "qwer1234" , "itemname" : "사과" , "count" : 3},
    {"orderid" : "pythongood" , "itemname" : "딸기" , "count" : 6},
    {"orderid" : "testid" , "itemname" : "바나나" , "count" : 1},
    {"orderid" : "pythongood" , "itemname" : "사과" , "count" : 2},
    {"orderid" : "testid" , "itemname" : "바나나" , "count" : 7},
    {"orderid" : "qwer1234" , "itemname" : "사과" , "count" : 1}, 
    {"orderid" : "cccddd" , "itemname" : "바나나" , "count" : 3},
    {"orderid" : "cccddd" , "itemname" : "사과" , "count" : 2},
]

totalList = []



