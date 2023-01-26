'''
[문제]
	130 의 약수 중에서 작은 수부터 큰 수를 출력했을 때, 
	다섯 번째 약수만 출력하시오.
[정답]
	13
'''
num = 130
count = 0
i = 1 
while i <= num :
    # print(num)
    if num % i == 0 : 
        # print(i)
        count += 1 
        if count == 5 :
            print(i)
    # num -= 1
    i += 1 

'''
[문제]
    두 자릿수의 28의 배수 중에서 가장 큰 수를 출력하시오.
[정답]
   84
'''

# temp = 0
num = 0
# run = 1
i = 28
while i <= 100 :
    if i % 28 == 0 : 
        if i < 100 :
            # print(num)
            num = i
    i += 1 
print(num)

# while run == 1 :
#     if i % 28 == 0 :
#         num = i
#         if num < 100 :
#             # print(num, end = " ")
#             # num = i
#             num = i
    
#         if temp < num :
#             temp = num 
#             run = 0
#     i += 1 
# print(temp)

