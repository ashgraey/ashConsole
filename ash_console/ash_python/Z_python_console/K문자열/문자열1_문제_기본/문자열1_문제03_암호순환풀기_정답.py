'''
    [문제]
        철수는 비밀번호는 아래와 같다. 
        철수는 비밀번호를 보호하기 위해 비밀번호를 순환을 3번 반복했다.
        순환이란 글자를 한 칸씩 앞으로 밀고 맨 앞의 글자는 뒤로 붙이는 걸 말한다.
        철수가 만들 암호를 풀어 원래대로 비밀번호를 복원하시오.
    [예시]
        r1234qwe
    [결과]
        qwer1234
'''
password = "r1234qwe"

for i in range(3):
    temp = ""
    temp += password[len(password) - 1]
    for j in range(len(password) - 1):
        temp += password[j]
    password = temp
print(password)


