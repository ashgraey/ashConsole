'''
    [문제]
        아래 dbId와 logId가 서로 일치하는지 검사하시오.
        단, 대소문자를 구분하지 않는다. 
        즉, A나 a나 서로 같은 것이다.
    [정답]
'''		
dbId = "q1W2E3r4"
logId = "q1w2e3R4"

#힌트
str0 = "0123456789"
str1 = "abcdefghijklmnopqrstuvwxyz"
str2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# dbId의 위치값
if len(dbId) == len(logId) :
    dbIdx = []
    for i in range(len(dbId)) :
        for j in range(len(str1)) :
            if dbId[i] == str1[j] or dbId[i] == str2[j] :
                dbIdx.append(j)
                break
        
        for k in range(len(str0)) :
            if dbId[i] == str0[k] :
                dbIdx.append(k)

    print("dbIdx : ", dbIdx)

    # logId의 위치값
    logIdx = []
    for i in range(len(logId)) :
        for j in range(len(str1)) :
            if logId[i] == str1[j] or logId[i] == str2[j] :
                logIdx.append(j)
                break
        
        for k in range(len(str0)) :
            if logId[i] == str0[k] :
                logIdx.append(k)

    print("logIdx : ", logIdx)

    # 비교
    ck = False
    for i in range(len(dbIdx)) :
        if dbIdx[i] != logIdx[i] :
            ck = True
            break

    if ck == False :
        print("서로 같다")

    else :
        print("다르다")
else :
    print("다르다")
