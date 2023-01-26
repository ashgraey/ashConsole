'''
	[문제]
		a리스트의 값을 중복없이 value에 저장한다.
		그리고 중복되는 개수를 count에 저장한다.
	[정답]
		value = [10,20,30,100]
		count = [2,3,5,1]
'''

a = [10, 20, 30, 30, 100, 10, 30, 30, 20, 30, 20]

value = []
count = []

# 중복검사
# 중복되지 않은 값은 value리스트에 추가
i = 0
while i < len(a):
    check = False

    j = 0
    while j < len(value):
        if value[j] == a[i]:
            check = True
            break
        j += 1

    if check == False:
        value.append(a[i])

    i += 1

# count의 개수
# value리스트가 기점, a리스트를 돌면서 중복이면 cnt += 1 
# j 반복문이 끝난후 cnt값을 count리스트에 저장
# cnt는 0으로 초기화, i값은 증가 ..1
for i in range(len(value)):
    cnt = 0

    for j in range(len(a)):
        if value[i] == a[j]:
            cnt += 1
    
    count.append(cnt)

print("value =", value)
print("count =", count)