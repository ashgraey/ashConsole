
# https://school.programmers.co.kr/learn/courses/30/lessons/17677


def getArr(str):
    arr = []
    sample = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(str)-1):
        a = str[i]
        b = str[i + 1]
        a = a.upper()
        b = b.upper()
        if a in sample and b in sample:
            arr.append(a + b)
    return arr

def solution(str1, str2):  

    arr1 = getArr(str1)
    arr2 = getArr(str2)
   # arr1.sort()
   # arr2.sort()
    print(arr1, arr2)

    c1 = 0
    c2 = len(arr1) + len(arr2)
    if c2 == 0:
        return 65536
    
    for v in arr1:
        if v in arr2:
            c1 += 1
            index = arr2.index(v)
            del(arr2[index])  
    c2 = c2 - c1
    # print(c1 , c2)
    result = int(c1 / c2 * 65536)
    return result

str1 = "handshake"
str2 = "shake hands"

r = solution(str1 , str2)
print(r)