'''
    [함수리턴]
        함수는 리턴을 통해서 함수를 즉시 종료할수있다.

    [문제]
        a리스트에 짝수가 하나라도있으면 "x"를 출력하시오.
        전부 짝수이면 "o" 를 출력하시오.
'''
import random
def checkEven(a):
    for i in range(len(a)):
        if a[i] % 2 == 0:
            print("x")
            return # 리턴을 만나면 함수가 즉시종료되므로 아래는 실행되지않는다.
    print("o") 

for k in range(100):
    a = []
    for i in range(4):
        r = random.randint(1, 100)
        a.append(r)

    print(a , end=" ")
    checkEven(a)




