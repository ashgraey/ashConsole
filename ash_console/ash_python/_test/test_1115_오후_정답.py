'''
    [문제]
        랜덤으로 3~8의 숫자를 저장한다. 
        랜덤숫자 3 이면 세자리 자리수를 뜻한다. 
        랜덤숫자 4 이면 네자리 자리수를뜻한다.
        랜덤숫자 8 이면 여덟자리 자리수를 뜻한다. 
        
        세자리수라면 100~999 사이의 랜덤숫자를 다시 저장한다.
        네자리수라면 1000~9999 사이의 랜덤숫자를 다시 저장한다. 
        다자리수라면 10000~99999 사이의 랜덤숫자를 다시 저장한다.
        ...
        여덟자리수라면 10000000~99999999 사이의 랜덤숫자를 다시 저장한다. 
        위 규칙으로 뽑은 랜덤숫자의 한가운데 위치의 수를 출력한다.
        단, 숫자의 개수가 짝수라면 가운데 자리의 수는 두개가 될것이고,
        그중 앞의 자리수를 출력한다. 
    [예시] 
        r = 3  ==> 세자리수 534 ==> 
        가운데위치의 수인 3을 출력한다.  
        r = 4  ==> 두자리수 1945 ==> 
        가운데위치는 9, 4 두개인데 그중 앞의 자리수인 9 를 출력한다.
        r = 5  ==> 다섯자리수 13534 ==> 
        가운데 위치의 수인 5를 출력한다.
        r = 6  ==> 여섯자리수 564301 ==> 
        가운데위치는 4, 3 두개인데 그중 앞의 자리수인 4를 출력한다. 
'''
import random
r = random.randint(3,8)
i = 1
a = 1
while i < r:
    a *= 10
    i += 1

b = a * 10 - 1
print(r , a, b)

center = 0
if r % 2 == 1:
    center = r // 2 + 1
else:
    center = r // 2

print("center : " , center)

r2 = random.randint(a, b)
print("rand : " , r2)
run = 1
i = r  # 자리수는 뒤에서 부터 구한다. 
while run == 1:
    # 끝자리만 temp변수 안에 저장
    temp = r2 % 10
    print("temp =", temp)

    # 끝자리를 삭제, temp변수안의 값이 자릿수 단위로 바뀌어 저장
    r2 //= 10
    print("r2 =", r2)

    if i == center:
        print("중앙값 : " , temp)
        run = 0
    i -= 1

# [정답]
# import random
# r = random.randint(3,8)
# a = 1
# size = 0
# i = 1
# while i < r:
#     a *= 10
#     # size += 1
#     i += 1

# b = a * 10 - 1
# print(r , a, b)

# center = 0
# if r % 2 == 1:
#     center = r // 2 + 1 
# else:
#     center = r // 2 - 1 

# print("center : " , center)

# r = random.randint(a, b)
# print("rand : " , r)

# run = 1
# i = 1
# while run == 1 :
#     # 일의자리부터 하나씩 출력
#     temp = r % 10
#     # print(temp, end = " ")
#     if i == center:
#         print()
#         print("중앙값 : " , temp)
#         run = 0

#     r //= 10
#     i += 1