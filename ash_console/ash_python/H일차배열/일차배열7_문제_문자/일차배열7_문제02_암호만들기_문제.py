'''
    [문제]
        철수는 비밀번호는 아래와 같다. 

        철수는 비밀번호를 보호하기 위해 비밀번호 글자 사이사이에 
        알파벳을 a부터 순서대로 끼워넣었다.
        철수가 만든 비밀번호를 만들어보시오.
    [결과]
        qawbecrd1e2f3g4h
'''
'''
pasword 인덱스 사이사이에 a b c d e 를 끼워 넣어라

'''
password = "qwer1234"
sample = "abcdefghijklmnopqrstuvwxyz"

# [1116]
# temp = ""
# for i in range(len(password)) :
#     temp += password[i]
#     temp += sample[i]

# password = temp
# print(password)

# [1차]
# temp = ""
# # temp라는 문자열 형식의 빈 변수 생성 
# # temp 변수안에 password의 값과 sample의 값을 하나씩 저장
# for i in range(len(password)) : 
#     temp += password[i]
#     temp += sample[i]

# # temp변수를 password변수에 저장
# password = temp
# print(password)