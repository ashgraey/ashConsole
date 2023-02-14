def solution(n):

    arr = list(str(n))
    print(arr)
    arr = list(map(int , arr))
    print(arr)
    
    return sum(arr)

n = 123
a = solution(n)
print(n)