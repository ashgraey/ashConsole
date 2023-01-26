'''
    [문제]
        [조건1] 리스트에 랜덤 숫자(1~100) 20개를 추가한다.
        [조건2] 위 값 중 50보다 크면서 7의 배수만 출력하시오.
    [예시]
        arr = [18, 64, 54, 91, 2, 56, 18, 18, 16, 71, 17, 15, 35, 73, 34, 22, 50, 55, 35, 93]
        91
        56
'''
import random

arr = []

i = 0
while i < 20:
    r = random.randint(1, 100)
    arr.append(r)

    if 50 < arr[i] and arr[i] % 7 == 0:
        print(arr[i])
    i += 1
print(arr)


