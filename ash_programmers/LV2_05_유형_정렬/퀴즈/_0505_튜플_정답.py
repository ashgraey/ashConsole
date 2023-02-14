# https://school.programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    answer = []
    s = s[2:-2]
   # print(s)
    token = s.split("},{")
   # print(token)
    token.sort(key=lambda x: (len(x))) # 길이로 정렬 
    answer.append(token[0])
    for i  in range(1, len(token)):
        sample = token[i].split(",")
        for j in range(len(sample)):
            if sample[j] not in answer:
                answer.append(sample[j])
                break
    answer = list(map(int , answer))
    return answer


s = "{{20,111},{111}}"
r = solution(s)
print(r)

"""
길이로 정렬하는것이 핵심

"""