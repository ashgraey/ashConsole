'''
    [문제]
        랜덤으로 3~8의 숫자를 저장한다. 
        랜덤숫자 3 이면 세자리 자리수를 뜻한다. 
        랜덤숫자 4 이면 네자리 자리수를뜻한다.
        랜덤숫자 8 이면 여덟자리 자리수를 뜻한다. 
        세자리수라면 100~999 사이의 랜덤숫자를 다시 출력
        네자리수라면 1000~9999 사이의 랜덤숫자를 다시 출력
        다섯자리수라면 10000~99999 사이의 랜덤숫자를 다시 출력
        ...
        여덟자리수라면 10000000~99999999 사이의 랜덤숫자를 다시 출력
    [주의]
        반복문을 사용할것  
    [예시] 
        r = 3  ==> 세자리수 534 
        r = 4  ==> 두자리수 1945 
        r = 5  ==> 다섯자리수 13534 
        ...
        r = 8  ==> 여덟자리수 56430145
'''
# print("--[문제1]--")
# import random
# start = 3 
# end = 8 

# while True :
#     r = random.randint(start, end)
#     print("r =", r)     
    
#     if start > 3 :
#         break
    
#     if r == 3 : 
#         start = 100 
#         end = 999
    
#     if r == 4 :
#         start = 1000
#         end = 9999

#     if r == 5 :
#         start = 10000
#         end = 99999

#     if r == 6 :
#         start = 100000
#         end = 999999

#     if r == 7 :
#         start = 1000000
#         end = 9999999

#     if r == 8 :
#         start = 10000000
#         end = 99999999

# [정답]
import random
# r = random.randint(3, 8)
r = 3

i = 1
start = 1
print(r)

while i < r:
    start *= 10
    i += 1

end = start * 10 - 1
print(start , " " , end)

r  = random.randint(start , end)
print(r)


    