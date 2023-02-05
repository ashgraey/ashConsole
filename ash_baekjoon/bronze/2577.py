'''
세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고, 
계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.

입력/
첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어진다. A, B, C는 모두 100보다 크거나 같고, 1,000보다 작은 자연수이다.

출력/
첫째 줄에는 A × B × C의 결과에 0 이 몇 번 쓰였는지 출력한다. 
마찬가지로 둘째 줄부터 열 번째 줄까지 A × B × C의 결과에 1부터 9까지의 숫자가 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력한다.
'''
# 정답, 0202
# a = int(input())
# b = int(input())
# c = int(input())

# abc = a * b * c
# abc = list(str(abc))
# print(abc)
# tempAbc = list(set(abc))
# print(tempAbc)

# cntList = []
# for i in range(len(tempAbc)) :

#     cnt = 0
#     for j in range(len(abc)) :
#         if tempAbc[i] == abc[j] :
#             cnt += 1 
#     cntList.append(cnt)
# print(cntList)

# # numList 배열생성
# numList = []
# for i in range(10) :
#     numList.append(i)
# print(numList)

# # 숫자별 중복갯수 출력
# for i in range(len(numList)) :
#     ck = False
#     idx = 0
#     for j in range(len(tempAbc)) :
#         if numList[i] == int(tempAbc[j]) :
#             ck = True
#             idx = j
#             break
#     if ck == False :
#         print(0)
#     else :
#         print(cntList[idx])

# 다른 풀이 // 내장 함수를 잘 쓰면 코드의 양을 줄일 수 있다.
a = int(input())
b = int(input())
c = int(input())

result = list(str(a * b * c))
print(result)

for i in range(10) :
    print(result.count(str(i)))