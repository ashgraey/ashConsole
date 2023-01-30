'''
    [문제]
        리스트에 랜덤으로 -100 ~ 100 사이의 홀수 4개를 저장 후,
        전부 홀수인지 검사하는 함수를 만드시오.
    [예시]
        [-5, 99, -71, 27] 전부 홀수이다.
        [0, 22, -41, 21] 전부 홀수가 아니다.
'''
import random 

def oddCk(a) :

    for i in range(4) :
        a.append(random.randint(-100, 100))
    
    print(a)
    cnt = 0
    ck = False
    for i in range(len(a)) :
        if a[i] % 2 == 1 or a[i] % 2 == -1:
            cnt += 1 
    if cnt == len(a) :
        ck = True
        
    return ck
    
a = []
result = oddCk(a)
print(result)
