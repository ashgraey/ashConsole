"""
	[정답]
	[홀짝 게임]
		1. 1~10개의 숫자중 랜덤으로 한개의 숫자를 저장한다.
		2. [1.홀수][2.짝수] 선택지를 보여준다.
		3. 사용자는 선택지를 고르고 "정답" , "오답" 을 출력한다.
"""
import random

r = random.randint(1, 10)
print("random : ", r)

print("[1]홀수 [2]짝수 입력하세요")
choice = int(input())

if choice == 1 and r % 2 == 1:
    print("정답")

elif choice == 2 and r % 2 == 0:
    print("정답")

else:
    print("오답")
