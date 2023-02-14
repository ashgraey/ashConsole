# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(rent):
    mx = len(rent)

    for i in range(len(rent)):
        c = 0
        for j in range(len(rent)):
            if rent[j] >= mx :
                c += 1
            if c >= mx:
                return mx
        mx -= 1
    return 0

citations = 	[10000, 9999, 9998, 9997, 9996]
#citations = [0, 10000]
r = solution(citations)
print(r)