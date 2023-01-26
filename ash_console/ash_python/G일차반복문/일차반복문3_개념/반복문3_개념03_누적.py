'''
[문제] 1~5까지의 합을 출력하시오.  1 + 2 + 3 + 4 + 5
[정답] 15
'''

total = 0

i = 1
while i <= 5:
    # total = total + i
    total += i
    print("i =", i, ", total =", total)
    '''
    total = 0 + 1       1
    total = 1 + 2       3
    total = 3 + 3       6
    total = 6 + 4       10
    total = 10 + 5      15
    '''
    i += 1
print("total =", total)