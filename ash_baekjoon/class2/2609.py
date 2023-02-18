'''
최대공약수 최소공배수 문제//
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

input//
첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

output//
첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

'''
# 시간초과 뜸
a, b = map(int, input().split())

if a > b:
    size = a
else:
    size = b

# 최대공약수
temp = []
for i in range(1, size):
    if a % i == 0 and b % i == 0:
        temp.append(i)
print(max(temp))

# 최소공배수
i = 1
while True:
    if i % a == 0 and i % b == 0:
        print(i)
        break
    i += 1
