# https://school.programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):

        for i in range(1, count + 1) :
                money -= (price * i)
                # print(money)

        if money < 0 :
                return -money
        elif money >= 0 :
                money = 0 
                return money

price = 3
money = 20
count = 4
result = solution(price , money , count)
print(result)

