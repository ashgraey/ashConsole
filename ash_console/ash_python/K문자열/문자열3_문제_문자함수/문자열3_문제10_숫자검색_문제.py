'''
    [문제]
        철수는 a리스트에서 숫자 검사를 해야한다.
        각 단어를 검사해서 해당 메시지 중 하나를 출력하시오.
    [정답]
        문자만 있다
        숫자만 있다
        문자와 숫자가 섞여있다.
'''
a = ["adklajsiod", "123123", "dasd12312asd"]
msg = ["문자만 있다", "숫자만 있다", "문자와 숫자가 섞여있다."]

hint1 = "abcdefghijklmnopqrstuvwxyz"
hint2 = "0123456789"

for i in range(len(a)) :
    ck = False
    for j in range(len(a[i])) :
        
        for k in range(len(hint1)) :
            if a[i][j] == hint1[k] :
                ck = True 
        
            if ck == True :
                for n in range(len(hint2)) :
                    if a[i][j] == hint2[n] :
                        result = msg[2]
                        ck = 0
                        break

    if ck == True :
        result = msg[0]
    if ck == False :
        result = msg[1]
    
    print(result)

