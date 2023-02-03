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

# 1216
charge = 7800
temp = 0
for i in range(len(money)) :
    cnt = 0 
    if charge >= money[i] and count[i] != 0 :
        cnt = charge // money[i]
        print("cnt : ", cnt)
        if count[i] - cnt >= 0 :
            count[i] -= cnt
            charge %= money[i]
        else :
            temp = cnt - count[i]
            count[i] -= temp
            charge -= money[i] * temp
            # print(charge)
    print(i, charge)
    print()

print(money)
print(count)
 
1124
# # -되는 count값의 어떻게 해야할지 모르겠음
# 값을 한번에 구해서 해결하려함 
# 조건문이 아닌 반복문을 통해 해결해야했음
# while True : 
#     for i in range(len(money)) :
#         if charge > money[i] :
#             c = charge // money[i]
#             charge %= money[i]
#             print(c, charge)

#             if count[i] - c > 0 :
#                 count[i] -= c
#                 print(count)
    
#     if charge == 0 :
#         break
# print(count)
            
# 1122
# # 거스름돈 7800원을 뺀 나머지 금액(61700)
# total = 0 
# for i in range(len(money)) :
#     total += money[i] * count[i]
# # print(total)
# total -= charge
# print(total)

# # 61700을 단위별로 count분배
# for i in range(len(money)) :
#     cnt = total // money[i]
#     total %= money[i]
#     # print(cnt)  
#     # print(total)
#     count[i] = cnt
# print(count)
