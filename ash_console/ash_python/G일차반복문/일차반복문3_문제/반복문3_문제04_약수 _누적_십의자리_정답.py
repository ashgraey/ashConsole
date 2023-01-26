'''
	[문제]
	  	200의 약수 중에서 순서대로 약수를 출력했을 때, 
        [조건1] 십의자리가 4인 약수들만 출력하고, 
        [조건2] 그 전체 합을 구하시오.
        [조건3] 위 수의 개수를 출력하시오.
    [정답]
        40 
        total = 40
        count = 1
'''

num = 200

total = 0
count = 0

i = 1
while i <= num:
    if num % i == 0 and i % 100 // 10 == 4:
        print(i, end=" ")
        total += i
        count += 1
    i += 1
print()
print("total =", total)
print("count =", count)