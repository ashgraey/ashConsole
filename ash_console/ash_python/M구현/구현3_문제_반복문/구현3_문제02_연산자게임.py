"""
    [문제]
	  	[연산자 기호 맞추기 게임]
		1. 1~10 사이의 랜덤 숫자 2개를 a와 b에 각각 저장한다. 예) a = 3 , b = 4 
		
		2. 1~4 사이의 랜덤 숫자 1개를 op에 저장한다.  예) op = 3
		
		3. op의 값은  연산자 기호에 해당된다. 예) op의값이 3이면 곱하기 이다.
			[1] + [2] - [3] * [4] % 
		
		4. 화면에 숫자두개와 답을 출력한다. (단, 기호는 출력하면안된다.)
		예) 3 ? 4  = 12
			[1] + [2] - [3] * [4] % 
			
		5. 사용자는 기호를 맞추면된다. 예) 3 ==> 정답
  
		6. 5번반복하고 맞춘결과 출력 
		
"""
import random

for _ in range(5):
    a, b = map(int, input().split())

    op = random.randint(1, 4)

    result = 0
    if op == 1:
        result = a + b
    elif op == 2:
        result = a - b
    elif op == 3:
        result = a * b
    else:
        result = a % b

    print(a, "?", b, "=", result)
    print("[1] +, [2] -, [3] *, [4] %")
    user = int(input())

    if user == op:
        print("정답")
    else:
        print("오답")
