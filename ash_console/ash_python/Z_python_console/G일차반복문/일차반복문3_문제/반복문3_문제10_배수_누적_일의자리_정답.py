'''
	[문제]
	    100~200 사이의 숫자 중에서 
        [조건1] 6의 배수 중에서 일의 자리가 2인 수만 출력하고, 
        [조건2] 그 합을 구하시오.
        [조건3] 그 개수를 구하시오.
    [정답]
        102 132 162 192 
        total = 588
        count = 4
'''

total = 0
count = 0

i = 100
while i <= 200:
    if i % 6 == 0 and i % 10 == 2:
        print(i, end=" ")
        total += i
        count += 1
    i += 1
print()
print("total =", total)
print("count =", count)
