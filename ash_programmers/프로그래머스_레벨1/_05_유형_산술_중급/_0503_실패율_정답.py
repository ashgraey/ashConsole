# https://school.programmers.co.kr/learn/courses/30/lessons/42889
def solution(N, stages):
    answer = []
    test = []
    max = len(stages)
    for i in range(N):
        c = 0
        for j in range(len(stages)):
            a = i + 1
            if stages[j] == a:
                c += 1
        if c == 0:
            b = 0
        else:
            b = c / max
            max -= c
        test.append([a , b])
    test.sort(key = lambda x: (-x[1] , x[0]))
    print(test)
    for i in range(len(test)):
        answer.append(test[i][0])
    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
result = solution(N , stages)
print(result)