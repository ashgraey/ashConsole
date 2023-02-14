# https://school.programmers.co.kr/learn/courses/30/lessons/82612
def solution(price, money, count):
    total = 0
    a = price
    for i in range(count):
        total += price
        price = price + a
    if money >= total:
        total = 0
    else:
        total -= money
    return total

price = 3
money = 20
count = 4
result = solution(price , money , count)
print(result)