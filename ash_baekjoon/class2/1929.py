'''
소수 구하기 문제//
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

input//
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다.
(1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

output//
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
'''
import sys
import math

# front, back = map(int, sys.stdin.readline().split())

# for _ in range(front, back + 1):

#     cnt = 0
#     for j in range(1, front + 1):
#         if front % j == 0:
#             cnt += 1

#     if cnt == 2:
#         print(front)

#     front += 1
'''
에라토스테네스의 체(Sieve of Eratosthenes)는 소수(prime number)를 찾는 알고리즘 중 하나입니다. 이 알고리즘은 에라토스테네스라는 수학자가 고안한 것으로, 대략적으로 다음과 같은 과정으로 소수를 찾습니다.

2부터 찾고자 하는 수의 범위까지 모든 자연수를 적는다.
2부터 시작해서, 2의 배수를 모두 지운다. 즉, 2를 제외한 2의 배수는 모두 소수가 아니므로 제거한다.
다음으로 남은 수 중 가장 작은 수인 3을 찾아서, 3의 배수를 모두 지운다. 즉, 3을 제외한 3의 배수는 모두 소수가 아니므로 제거한다.
이러한 방법으로 지울 수 있는 모든 배수를 지우면, 남은 수는 모두 소수가 된다.
예를 들어, 2부터 30까지의 모든 소수를 찾을 때, 다음과 같은 과정을 거칩니다.

2부터 30까지의 모든 자연수를 적는다.
2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
2의 배수를 모두 지운다.
2 3 5 7 9 11 13 15 17 19 21 23 25 27 29
3의 배수를 모두 지운다.
2 3 5 7 11 13 17 19 23 25 29
5의 배수를 모두 지운다.
2 3 5 7 11 13 17 19 23 29
7의 배수를 모두 지운다.
2 3 5 7 11 13 17 19 23 29
따라서, 2부터 30까지의 모든 소수는 2, 3, 5, 7, 11, 13, 17, 19, 23, 29입니다. 이와 같은 방법으로 에라토스테네스의 체는 비교적 빠르게 소수를 찾을 수 있습니다.
'''


# def sosu(front, back):
#     sList = []
#     for num in range(front, back + 1):
#         if num == 3 or num == 5 or num == 7:
#             sList.append(num)
#         elif num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
#             sList.append(num)

#     return sList


# front, back = map(int, sys.stdin.readline().split())
# sosuList = sosu(front, back)
# for i in sosuList:
#     print(i)

def sosu(front, back):
    # sList = []
    i = front
    while i <= back :
        cnt = 0
        j = 2 
        while j <= math.sqrt(i) :
            # print(math.sqrt(i))
            if i % j == 0 :
                cnt += 1 
                break
            j += 1 

        if cnt == 0 :
            # sList.append(i)
            print(i)
        
        i += 1 
        
    # return sList

front, back = map(int, sys.stdin.readline().split())
sosu(front, back)
# sosuList = sosu(front, back)
# for v in sosuList:
#     print(v)
# print(sosuList)