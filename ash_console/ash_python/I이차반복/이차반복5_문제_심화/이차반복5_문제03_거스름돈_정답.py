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

# count인덱스 값을 빼는 형식
temp = charge
for i in range(len(money)):
    # money 인덱스 값보다 temp의 값이 이상이여야함
    if money[i] <= temp:
        # temp보다 작은 money의 인덱스3인 5000 and count[3] == 1 
        # 조건문이 아닌 반복문으로 해결해야함
        # 조건문같은 반복문
        while money[i] <= temp and count[i] > 0:
            # 7800 - 5000 == 2800
            temp -= money[i]
            # count 1감소
            count[i] -= 1
            print(count, temp)

'''
    7800,   5000 1장    = 2800      : count [1, 1, 0, 1, 5, 10]
    2800,   1000 1장    = 1800      : count [1, 1, 0, 0, 5, 10]
    1800,   500  3개    = 300       : count [1, 1, 0, 0, 2, 10]
    300,    100  3개    = 0         : count [1, 1, 0, 0, 2, 7]

'''