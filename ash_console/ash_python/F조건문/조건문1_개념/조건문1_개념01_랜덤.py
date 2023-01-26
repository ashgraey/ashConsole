import random

'''
# 랜덤 사용법
    [1] 최상단에 import random을 해준다. 
        import 라는건 다른 파일에 있는 기능을 추가할 때 사용한다. 
        프로그램이 만들어질 때 import 한 파일 용량이 추가되기 때문에 
        정말 사용할 기능들만 import 해야 한다. 

    [2] random.randint(시작 값, 마침 값)
        예를 들어 주사위를 표현한다고 하면 주사위는 1부터 6까지의 값이 있고,
        어떤 값이 나올지 모른다. 이때 랜덤을 사용하면 주사위를 표현할 수 있다.
'''

주사위 = random.randint(1, 6) 
print(주사위)

'''
[문제1]
    주사위 두 개를 던져서 그 합을 출력하시오.
'''

주1 = random.randint(1, 6)
주2 = random.randint(1, 6)
print(주1, "+", 주2, "=", 주1 + 주2)
