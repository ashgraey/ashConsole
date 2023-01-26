'''
    [문제]
        동전의 앞과 뒤를 랜덤숫자 0 또는 1로 표현한다.
        동전 두 개를 던져서 둘 다 "앞"이면 "정답",
        둘 다 "뒤"이어도 "정답"이다.
        둘 중 하나라도 반대면 "꽝"을 출력하시오.
'''

import random

동전1 = random.randint(0,1)
동전2 = random.randint(0,1)
print("동전1 =", 동전1)
print("동전2 =",동전2)

동전앞 = 0
동전뒤 = 1 

# 둘다 앞이면 정답
if 동전1 == 동전앞 and 동전2 == 동전앞 :
    print("정답")
# 둘다 뒤이어도 정답
if 동전1 == 동전뒤 and 동전2 == 동전뒤 :
    print("정답")

# 둘 중 하나라도 반대면 꽝 
if (동전1 == 동전앞 and 동전2 == 동전뒤) or (동전1 == 동전뒤 and 동전2 == 동전앞) :
    print("꽝")



# coin1 = random.randint(0, 1)
# coin2 = random.randint(0, 1)
# print("동전1 =", coin1)
# print("동전2 =", coin2)

# if coin1 == coin2 :
#     print("정답")
# if coin1 != coin2 :
#     print("꽝")

# [정답]
# import random

# 동전1 = random.randint(0, 1)
# 동전2 = random.randint(0, 1)
# print("동전1 =", 동전1)
# print("동전2 =", 동전2)

# if 동전1 == 동전2:
#     print("정답")

# if 동전1 != 동전2:
#     print("꽝")


