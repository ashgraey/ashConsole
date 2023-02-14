# https://school.programmers.co.kr/learn/courses/30/lessons/42584

def solution(p):
    answer = []
    for i , v in enumerate(p):
        c = 0
        #print(i , v )
        for j in range(i + 1, len(p)):
            c += 1
            if v > p[j]:
                break
        answer.append(c)

    return answer


prices = [1,2,3,2,3]

r = solution(prices)

print(r)