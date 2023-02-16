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

dbSize = len(dbId)
logSize = len(logId)

count = 0
check = True
if dbSize == logSize:
    for i in range(len(dbId)):
        checkNumDbId = -1
        for j in range(len(str0)):
            if dbId[i] == str0[j]:
                checkNumDbId = i
        
        # 숫자이면
        if checkNumDbId != -1:
            if dbId[i] == logId[i]:
                print(dbId[i], ",", logId[i])
                count += 1
        # 문자이면
        else:
            checkStr1DbId = -1
            checkStr1LogId = -1
            for j in range(len(str1)):
                if dbId[i] == str1[j]:
                    checkStr1DbId = j
                if logId[i] == str1[j]:
                    checkStr1LogId = j
            
            checkStr2DbId = -1
            checkStr2LogId = -1
            for j in range(len(str2)):
                if dbId[i] == str2[j]:
                    checkStr2DbId = j
                if logId[i] == str2[j]:
                    checkStr2LogId = j
                    
            if checkStr1DbId == checkStr1LogId:
                print(dbId[i], ",", logId[i])
                count += 1
            elif checkStr1DbId == checkStr2LogId:
                print(dbId[i], ",", logId[i])
                count += 1
            elif checkStr2DbId == checkStr1LogId:
                print(dbId[i], ",", logId[i])
                count += 1
            elif checkStr2DbId == checkStr2LogId:
                print(dbId[i], ",", logId[i])
                count += 1
        
    if count != len(dbId):
        check = False
else:
    check = False

if check == True:
    print("같은 단어")
else:
    print("다른 단어")
