'''
    [문제]
        [조건1] 리스트에 랜덤 숫자(1~100) 20개를 추가한다.
        [조건2] 위 값 중 30보다 작거나 70보다 크면서 4의 배수만 출력하시오.
    [예시]
        arr = [66, 71, 9, 88, 79, 80, 53, 78, 97, 74, 38, 82, 82, 54, 89, 17, 48, 86, 94, 51]
        9
        88
        80
        17
'''
import random

arr = []

i = 0
while i < 20:
    r = random.randint(1, 100)
    arr.append(r)

    if arr[i] < 30 or (70 < arr[i] and arr[i] % 4 == 0):
        print(arr[i])
    i += 1
print(arr)



