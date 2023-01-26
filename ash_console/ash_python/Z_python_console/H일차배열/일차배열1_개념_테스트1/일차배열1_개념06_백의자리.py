'''
    [문제]
        a 리스트에서 백의자리가 2인 수만 출력하시오.
    [정답]
        1210
        1212
'''

a = [1210, 1343, 1524, 1212, 7452]

'''
num = 1210
answer = num % 1000 // 100
print(answer)
'''

for i in range(len(a)):
    # print(a[i] % 1000 // 100)
    if a[i] % 1000 // 100 == 2:
        print(a[i])


