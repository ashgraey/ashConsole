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

# 0 1 2 3 4 5 6 7 
# 1차
# temp = ""
# idx = 5
# for i in range(len(password) - 1) :
#     temp += password[idx]
#     idx += 1
#     if idx == len(password) :
#         idx = 0
# password = temp
# print(password)

# 0126
# 비밀번호 순환 : 3
# 결과
# 1234qwer -> 234qwer1 -> 34qwer12 -> 4qwer123 -> qwer1234
# 정순환으로 풀었음
for i in range(5) :
    temp = password[0]
    tempPw = ""
    for j in range(1, len(password)) :
        tempPw += password[j]

    tempPw += temp
    password = tempPw
    print(password)

print("결과 : ", password)
    

