'''
    [문제]	
        a의 값들을 거꾸로 출력하시오.
    [정답]
        60 54 12 44 21 
'''
a = [21, 44, 12, 54, 60]

'''
        a[0] ... a[4]
        a[4] ... a[0]
'''
# 방법1)
index = len(a) - 1
for i in range(len(a)):
    # print(4 - i)
    print(a[index - i])
print()

# 방법2)
index = len(a) - 1
for i in range(len(a)):
    print(a[index])
    index -= 1


