def solution(left, right):
    a = left
    total = 0
    while a <= right: 
        n = 1
        arr = []
        while n <= a:
            if a % n == 0:
                arr.append(n)
            n += 1
        print(arr)
        if len(arr) % 2 == 0:
            total += a
        else:
            total -= a
        a += 1
    return total

left = 13
right = 17
result = solution(left , right)
print(result)