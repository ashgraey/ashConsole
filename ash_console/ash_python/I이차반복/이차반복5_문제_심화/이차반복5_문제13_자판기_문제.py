'''
    [문제]
        철수는 자판기에 물건을 채우려고 한다. 
        vending 리스트는 현재 자판기에 남아있는 물건 개수이다.
        box리스트는 자판기에 추가할 물건 개수이며, 5개씩 4줄 총 20개 여분이 있다.
        box의 앞에서부터 순차적으로 자판기에 물건을 채워 넣는다.
        자판기는 한 줄당 최대 10개까지 채울 수 있다.
        자판기가 전부 채워지거나 box가 전부 비워지면 종료되는 프로그램을 작성하시오.
    [예시]
        vending = [7, 5, 3, 5, 3]
        box     = [5, 5, 5, 5]

        vending = [10, 5, 3, 5, 3]
        box     = [2, 5, 5, 5]    

        vending = [10, 7, 3, 5, 3]
        box     = [0, 5, 5, 5]    

        vending = [10, 10, 3, 5, 3]
        box     = [0, 2, 5, 5]

        vending = [10, 10, 5, 5, 3]
        box     = [0, 0, 5, 5]

        vending = [10, 10, 10, 5, 3]
        box     = [0, 0, 0, 5]

        vending = [10, 10, 10, 10, 3]
        box     = [0, 0, 0, 0]
    [정답] 
        vending = [10, 10, 10, 10, 3]
        box     = [0, 0, 0, 0]
'''
# tip : idx 변수를 따로 둔다.
vending = [7, 5, 3, 5, 3]
box = [5, 5, 5, 5]
# 구성 
# 10 - vending[i] = plus
# box[i] - plus = box의 값
vIdx = 0 
bIdx = 0 
while True :
    if vending[vIdx] < 10 :

        plus = 10 - vending[vIdx]

        if box[bIdx] >= plus :
            vending[vIdx] += plus
            box[bIdx] -= plus
        else :
            vending[vIdx] += box[bIdx]
            box[bIdx] = 0 
    
    if box[bIdx] == 0 :
        bIdx += 1 
    
    if vending[vIdx] == 10 :
        vIdx += 1 
    
    print("vending =", vending)
    print("box =", box)
    print()
    
    # vIdx가 마지막 인덱스 번호를 넘어가거나 bIdx가 마지막 인덱스번호를 넘어가면 break
    if vIdx == 5 or bIdx == 4 : 
        break

 