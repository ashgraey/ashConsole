'''
분해합 문제//
어떤 자연수 N이 있을 때, 
그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 
어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. 
예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 
따라서 245는 256의 생성자가 된다. 
물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 
반대로, 생성자가 여러 개인 자연수도 있을 수 있다.

자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.

input//
첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

output//
첫째 줄에 답을 출력한다. 생성자가 없는 경우에는 0을 출력한다.

'''

# 부르트포스 알고리즘
# 모든 경우의 수를 찾는다

n = int(input())

temp = n
cnt = 0
while True:
    # 종료 조건
    if temp == 0:
        break

    # 문자열 형변환으로 리스트로 바꾸기
    temp = str(temp)
    nList = []
    for i in temp:
        nList.append(int(i))

    # 정수 형변환 시키고 합산값 구하기
    temp = int(temp)
    tot = temp + sum(nList)

    # 생성자가 큰 순으로 result 변수에 담기
    # cnt는 생성자가 없는 경우를 위해 만듬
    if n == tot:
        result = temp
        cnt += 1

    # cnt가 0이면 생성자가 없으므로 result에 0값 담기
    if cnt == 0:
        result = 0

    temp -= 1

# 결과 출력
print(result)
