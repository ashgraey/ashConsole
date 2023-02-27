'''
소수 문제//
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

input//
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

output//
주어진 수들 중 소수의 개수를 출력한다.

'''
import math

# numList = []
# for i in range(N):
#     numList.append(int(input()))
# N = int(input())
# numList = list(map(int, input().split()))

# sosu = 0
# cnt = 0
# for i in range(len(numList)):

#     if numList[i] != 1:
#         cnt = 0
#         for j in range(1, numList[i] + 1):
#             if numList[i] % j == 0:
#                 cnt += 1

#     if cnt == 2:
#         sosu += 1

# print(sosu)

# 소수를 구하기 속도 개선 => 그 수의 제곱근까지 구하면된다.
# N = int(input())
# numList = list(map(int, input().split()))

# sosu = 0
# cnt = 0
# for i in range(len(numList)):

#     if numList[i] != 1:
#         cnt = 0
#         j = 2 
#         while j <= math.sqrt(numList[i]) :
#             if numList[i] % j == 0 :
#                 cnt += 1
#             j += 1 

#     if cnt == 2:
#         sosu += 1

# print(sosu)