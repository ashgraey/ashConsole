'''
    [문제]
        랜덤으로 dir 리스트의 값을 d에 저장한다.
        d값의 방향으로 a리스트의 모든값이 한칸씩 이동한다.
        밀린값은 반대편으로 저장된다.
        
    [예시1]
        d = "북"
    [결과1]    
        [1004,1005,1006,1007],
        [1008,1009,1010,1011],
        [1000,1001,1002,1003],
        
    [예시2]
        d = "서"
    [결과2]
        [1001,1002,1003,1000],
        [1005,1006,1007,1004],
        [1009,1010,1011,1008],
    
'''
import random
dir = ["북" , "동" , "남" , "서"]
d = ""
a = [
    [1000,1001,1002,1003],
    [1004,1005,1006,1007],
    [1008,1009,1010,1011],
]

r = random.randint(0, len(dir)-1)
d = dir[r]
d = "서"
print(d)
if d == "북":
    temp = a[0]
    for i in range(len(a)-1):
        a[i] = a[i + 1]
    a[-1] = temp
elif d == "동":
    for i in range(len(a)):
        temp = a[i][-1]
        last = len(a[i])-1
        for j in range(len(a[i])-1):
            a[i][last] = a[i][last-1]
            last -= 1
        a[i][0] = temp
elif d == "남":
    temp = a[-1]
    last = len(a)-1
    for i in range(len(a)-1):
        a[last] = a[last -1]
        last -= 1
    a[0] = temp
elif d == "서":
    for i in range(len(a)):
        temp = a[i][0]
        for j in range(len(a[i])-1):
            a[i][j] = a[i][j + 1]           
        a[i][-1] = temp

for i in range(len(a)):
    print(a[i])

