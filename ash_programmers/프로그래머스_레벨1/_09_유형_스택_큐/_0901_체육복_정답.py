# https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    answer = 0
    answer = n - len(lost)
    lost.sort()
    reserve.sort()
    check = False
    while True:
        check = False
        for i in range(len(lost)):
            if lost[i] in reserve:
                ri = reserve.index(lost[i])
                answer += 1      
                del(lost[i])
                del(reserve[ri])     
                #lost.remove(i)
                #reserve.remove(ri)
                check = True
                break
        if check == False:
            break

    for i in range(len(lost)):
        a = lost[i]
        a1 = a - 1
        if a1 in reserve:
            answer += 1
            reserve.remove(a1)
            continue
        a2 = a + 1
        if a2 in reserve:
            answer += 1
            reserve.remove(a2)
    return answer


n = 5
lost = [1,2]
reserve = [2,3]
result = solution(n, lost, reserve)
print(result)