"""
[문제]
    아래 a 이차원배열에서 "o" 은 값이 있다는 뜻이고 "x" 는 없다는뜻이다.
    "o" 은 중력을 가지고있어서 아래로 내려간다. 
    전부 내려간이후의 모습을 출력하시오.
    [예시]
        ["o","o","o","o"],
        ["o","x","o","o"],
        ["x","x","o","x"],
        ["x","o","x","o"],
        아래와 같이된다. 
        ["x","x","x","x"],
        ["x","x","o","o"],
        ["o","o","o","o"],
        ["o","o","o","o"],

"""
arr = [
    ["o","o","o","o"],
    ["o","x","o","o"],
    ["x","x","o","x"],
    ["x","o","x","o"],
]

for i in range(len(arr)): 
    y = len(arr) - 1
    for j in range(len(arr[i])):
        if arr[y][i] == "x" :
            z = y - 1
            for k in range(y):
                if arr[z][i] == "o":
                    temp = arr[z][i]
                    arr[z][i] = arr[y][i]
                    arr[y][i] = temp
                    break
                z -= 1
        y -= 1
for i in range(len(arr)):
    print(arr[i])