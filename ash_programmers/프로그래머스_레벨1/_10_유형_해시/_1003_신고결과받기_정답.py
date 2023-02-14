# https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    answer = []
    all = {}
    for i in range(len(report)):
        a = report[i]
        token = a.split(" ")
        #print(token)
        user = None
        if token[1] in all:
            user = all[token[1]]
            user[token[0]] = 1
        else:
            user = {token[0] : 1}
        all[token[1]] = user   
        #print(all)  
    
    keys = all.keys()
    answer = [0 for i in range(len(id_list))]
    for key in keys:
        if len(all[key]) >= k:
            #print(key)
            d = all[key]
            #print(d)
            for i in range(len(id_list)):                
                if id_list[i] in d.keys():
                    answer[i] += 1      
    return answer
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
result = solution(id_list , report , k)
print(result)
