'''
    [문제]
        a 리스트에서 백의자리가 2인 수만 출력하시오.
    [정답]
        1210
        1212
'''

a = [1210,1343,1524,1212,7452]

# [1114]
# for i in range(len(a)) :
#     백 = a[i] % 1000 // 100 
#     if 백 == 2 :
#         print(a[i])

for i in range(5):
    if a[i] % 1000 // 100 == 2:
        print(a[i])


