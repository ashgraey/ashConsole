'''
    [문제]
        랜덤으로 dir 리스트의 값을 d에 저장한다. 
        랜덤으로 count 에 2~4를 저장한다.
        d값의 방향으로 a리스트의 모든값이 count 숫자만큼 이동한다. 
        밀린값은 반대편으로 저장된다.
        
    [예시1]
        d = "북" 
        count = 2
        
    [결과1]          
        [1008,1009,1010,1011],
        [1000,1001,1002,1003],
        [1004,1005,1006,1007],
        
    [예시2]
        d = "서"
        count = 3
    [결과2]
        [1003,1000,1001,1002],
        [1007,1004,1005,1006],
        [1011,1008,1009,1010],
    
'''
import random

dir = ["북" , "동" , "남" , "서"]
d = ""
count = 0
a = [
    [1000,1001,1002,1003],
    [1004,1005,1006,1007],
    [1008,1009,1010,1011],
]

count = random.randint(2,4)
d = random.randint(0, len(dir) - 1)
# d = "서"
print("방향 = ", dir[d])
print("count = ", count)

for i in range(count) :
    if dir[d] == "북" :
        temp = a[0]
        for i in range(len(a) - 1) :
            a[i] = a[i + 1]
        a[-1] = temp

    elif dir[d] == "동" :
        for i in range(len(a)) :
            temp = a[i][-1]
            j = len(a[i]) - 1 
            while j > 0 :
                a[i][j] = a[i][j - 1]
                j -= 1
            a[i][0] = temp

    elif dir[d] == "서" :
        for i in range(len(a)) :
            temp = a[i][0]
            for j in range(len(a[i]) - 1) :
                a[i][j] = a[i][j + 1]
            a[i][-1] = temp
    else :
        temp = a[-1]
        for i in range(len(a) - 1) :
            a[2 - i] = a[1 - i]
        a[0] = temp
    
for i in range(len(a)) :
    print(a[i]) 

