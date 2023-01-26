'''
    [문제]
        철수는 비밀번호는 아래와 같다. 
        철수는 비밀번호를 보호하기 위해 비밀번호 글자 사이사이에 
        알파벳을 a부터 순서대로 끼워넣었다.
        철수가 만든 비밀번호를 만들어보시오.
    [결과]
        qawbecrd1e2f3g4h
'''
password = "qwer1234"
sample = "abcdefghijklmnopqrstuvwxyz"

temp = ""
for i in range(len(password)):
    temp += password[i]
    temp += sample[i]
password = temp
print(password)

