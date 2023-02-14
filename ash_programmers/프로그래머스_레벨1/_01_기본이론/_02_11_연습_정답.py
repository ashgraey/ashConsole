"""
[문제]
    아래 itemData 아이템들의 총목록이다.
    salesData 는 오늘의 매출 현황이다. 
    상품이름과 판매개수가 한쌍이다.
    오늘의 총매출 결과를 출력하시오.
    단 판매개수로 내림차순하시오.
[예시]
    감자깡 13
    새우깡 9
    콘칩 3
    오징어볼 0
"""

itemData = ["새우깡" , "감자깡" , "오징어볼" , "콘칩"]
salesData = "새우깡 5,감자깡 6,새우깡 4,콘칩 3,감자깡 7"
viewData = {}

def printView(viewData):
    print("----------------------------")
    for key in viewData.keys():
        print(key , " " , viewData[key])
    print("----------------------------")


# 아이템 이름만 먼저 복사
tokenList = salesData.split(",")
for i in range(len(itemData)):
    viewData[itemData[i]] = 0
printView(viewData)

# 판매개수 누적하기
for i in range(len(tokenList)):
    token = tokenList[i].split(" ")
    viewData[token[0]] += int(token[1])
printView(viewData)

# 정렬 
# 단, 데이터가 리스트안의 튜플로 바뀐다. 
sortedView = sorted(viewData.items(), key=lambda x: x[1], reverse=True)
print(sortedView)













