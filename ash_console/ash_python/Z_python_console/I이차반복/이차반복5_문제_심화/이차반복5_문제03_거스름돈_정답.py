'''
    [문제]
        아래 리스트는 철수가 소지한 현금 개수이다.
        money는 돈 단위를 뜻하고,
        count는 단위별 개수를 뜻한다. 

        거스름돈은 7800일 때, 
        단위별로 나눠주고, 
        count리스트 값을 조정 후 출력하시오. 
    [정답]
        count = [1, 1, 0, 0, 2, 7]
'''
money = [50000, 10000, 5000, 1000, 500, 100]
count = [    1,     1,    1,    1,   5,  10]

charge = 7800

temp = charge
for i in range(len(money)):
    if money[i] <= temp:
        while money[i] <= temp and count[i] > 0:
            temp -= money[i]
            count[i] -= 1
print(count)
'''
    7800,   5000 1장    = 2800      : count [1, 1, 0, 1, 5, 10]
    2800,   1000 1장    = 1800      : count [1, 1, 0, 0, 5, 10]
    1800,   500  3개    = 300       : count [1, 1, 0, 0, 2, 10]
    300,    100  3개    = 0         : count [1, 1, 0, 0, 2, 7]

'''