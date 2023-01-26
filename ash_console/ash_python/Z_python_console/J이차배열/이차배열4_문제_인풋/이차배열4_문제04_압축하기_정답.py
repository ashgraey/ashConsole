'''
    [문제]
        a리스트는 압축하기 전 데이터이다.
        다음데이터를 압축 하시오.
        
        압축 기준은 데이터와 개수로 저장한다.
        예를 들어 3이 연속으로 5개이므로
        b = [[3,5]]
        다시 5가 6개이므로
        b = [[3,5],[5,6]]
        위와 같이 마지막까지 반복하시오.  
    [정답]     
        [3, 5]
        [5, 6]
        [2, 1]
        [4, 1]
        [2, 2]
'''
a = [3,3,3,3,3,5,5,5,5,5,5,2,4,2,2]
b = []

temp = [0, 0]
count = 1

i = 1
while i < len(a):
    
    if a[i - 1] == a[i]:
        count += 1
    else:
        print("실행", i)
        temp[0] = a[i - 1]
        temp[1] = count
        b.append(temp)

        count = 1
        temp = [0, 0]
    print(i)
    i += 1

temp = [0, 0]
temp[0] = a[14]
temp[1] = count
b.append(temp)

for i in range(len(b)):
    print(b[i])