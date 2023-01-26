'''
    [문제] 클래스로 변경하시오.
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

# 0 : 문자만 있다.
# 1 : 숫자만 있다.
# 2 : 문자와 숫자가 섞여있다.
check = 0
for i in range(len(a)):
    count = 0
    for j in range(len(a[i])):
        for k in range(len(hint2)):
            if a[i][j] == hint2[k]:
                count += 1
    if count == len(a[i]):
        check += 1
    elif count > 0:
        check += 1
    print(msg[check])