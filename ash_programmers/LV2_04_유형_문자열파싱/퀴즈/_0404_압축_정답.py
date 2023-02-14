# https://school.programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    answer = []
    sample = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    di = {}
    lastnum = 0
    for i in range(len(sample)):
        lastnum = i + 1
        di[sample[i]] = lastnum
    
    i = 1
    while True:
        a = msg[:i] # 현재글자
        
        if i == len(msg):
            answer.append(di[a])
            break

        b = msg[:i + 1] # 다음글자 

        if b in di:
            i += 1
        else:
            answer.append(di[a])
            lastnum += 1
            di[b] = lastnum     
            msg = msg[i:]
            i = 1

    return answer
msg = "TOBEORNOTTOBEORTOBEORNOT"
r = solution(msg)
print(r)