'''
    [문제]
        [1] 랜덤(1~50) 에서 3의 배수 3개의 합을 total 에 추가한다. 
        [2] 위내용을 총 다섯번 반복한다. 

    [예시]
        36 18 39  : 93
        21 27 15  : 63
        24 9 42  : 75
        21 3 39  : 63
        24 6 18  : 48

        total = [93, 63, 75, 63, 48]
'''
import random

total = []

for i in range(5):

    result = 0
    count = 0
    while True:
        r = random.randint(1, 50)

        if r % 3 == 0:
            result += r
            print(r, end=" ")
            count += 1
        
        if count == 3:
            break
    print(" :", result)

    total.append(result)


'''
for i in range(5):
    count = 0
    t = 0
    while True:
        r = random.randint(1,50)
        if r % 3 == 0:
            print(r , end=" ")
            t += r
            count += 1
        if count == 3:
            break
    total.append(t)
    print(total)
'''