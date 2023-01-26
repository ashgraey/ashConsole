
# 문제 1) 숫자 2개를 입력받아, 합 출력
x = int(input("숫자1 입력 : "))
y = int(input("숫자2 입력 : "))

print("두 수의 합 =", (x + y))

# 문제 2) 숫자 1개를 입력받아, 홀수이면 True 출력
num = int(input("숫자 입력 : "))
print(num % 2 == 1)

# 문제 3) 성적을 입력받아, 60점 이상이고 100점 이하이면 True 출력
score = int(input("성적 입력 : "))
print(60 <= score and score <= 100)