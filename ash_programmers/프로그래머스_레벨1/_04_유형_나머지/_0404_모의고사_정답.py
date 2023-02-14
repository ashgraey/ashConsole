def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    maxlist = [0,0,0]
    for i in range(len(answers)):
        if answers[i] == a[i % len(a)]:
            maxlist[0] += 1
        if answers[i] == b[i % len(b) ]:
            maxlist[1] += 1
        if answers[i] == c[i % len(c)]:
            maxlist[2] += 1
    result = max(maxlist[0] , maxlist[1], maxlist[2])

    for i in range(3):
        if result == maxlist[i]:
            answer.append(i + 1)
    answer.sort()
    return answer

answers =  [5, 5, 4, 2, 3] 
result = solution(answers)
print(result)