'''
[문제] 
	48의 약수 중 홀수만 출력하시오.
[정답]
	1
	3
'''
num = 48

i = 1
while i <= num:
    if num % i == 0 and i % 2 == 1:
        print(i)
    i += 1

print("------------")

i = 1
while i <= num:
    if num % i == 0:
        if i % 2 == 1:
            print(i)
    i += 1

