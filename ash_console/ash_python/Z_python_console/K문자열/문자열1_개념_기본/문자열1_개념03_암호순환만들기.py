'''
    [문제]
        철수는 비밀번호는 아래와 같다. 
        철수는 비밀번호를 보호하기 위해 비밀번호 순환을 3번 반복했다.
        순환이란 글자를 한칸씩 앞으로 밀고 맨 앞의 글자는 뒤로 붙이는 걸 말한다.
        철수가 만든 비밀번호를 만들어보시오.
    [예시]
        qwer1234
        wer1234q
        er1234qw
        r1234qwe
    [정답]
        r1234qwe
'''
password = "qwer1234"

for i in range(3):
    temp = ""
    for j in range(len(password)):
        if j == len(password) - 1:
            temp += password[0]
        else:
            temp += password[j + 1]
    password = temp
    print(password)