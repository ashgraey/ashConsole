def solution(n):
    a = str(n)
    arr = list(a)
    #print(arr)
    arr.reverse()
    #print(arr)
    a = map(int , arr)
    arr = list(a)
    #print(arr)
    return arr
n = 12345
a = solution(n)
print(a)