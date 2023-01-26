'''
    [문제]
        a 와 b 의 각 자리의 합을 total에 저장하시오.
    [정답]
        [64, 49, 27, 24, 103]
'''

a     = [10, 43, 23, 12, 53]
b     = [54, 6,   4, 12, 50]
total = [0,  0,   0,  0,  0]

# total[0] = a[0] + b[0]
# total[1] = a[1] + b[1]
# total[2] = a[2] + b[2]
# total[3] = a[3] + b[3]
# total[4] = a[4] + b[4]

for i in range(5):
    total[i] = a[i] + b[i]
print(total)


