# # https://school.programmers.co.kr/learn/courses/30/lessons/86051
def solution(numbers):
    total = 0
    for i in range(10):
        total += i

    a = sum(numbers)
    b = total - a
    return b
numbers = [1,2,3,4,6,7,8,0]

result = solution(numbers)
print(result)