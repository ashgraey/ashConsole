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

# count를 이용하여 hint1의 count가 문자열의 길이와 일치하면 문자만있다.
# count == 0이면 숫자만 있다
# count != 0 and count != 문자열의 길이이면 문자와 숫자가 섞여있다 출력

for i in range(len(a)) :
    cnt = 0
    for j in range(len(a[i])) :

        for k in range(len(hint1)) :
            if a[i][j] == hint1[k] :
                cnt += 1 
    print(cnt)
    if cnt == len(a[i]) :
        print(msg[0])
    elif cnt == 0 : 
        print(msg[1])
    elif cnt != 0 and cnt != len(a[i]) :
        print(msg[2])

