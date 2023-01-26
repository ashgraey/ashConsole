'''
    [문제]
        철수는 비밀번호는 아래와 같다. 
        철수는 비밀번호를 보호하기 위해 비밀번호 글자 사이사이에 
        알파벳을 a부터 순서대로 끼워 넣었다.
        이제 철수는 원래 비밀번호로 다시 변환해야 한다.
        암호화된 비밀번호를 원래대로 복구하시오.
    [정답]
        qwer1234
'''
'''
암호화된 비밀번호 idx 
1 3 5 7 9 11 13 15

암호화 안된 비밀버호 idx 
0 3 5 7 9 11 
'''
password = "qawbecrd1e2f3g4h"
temp = ""

# [1116]
# for i in range(len(password)) :
#     if i % 2 == 0 :
#         temp += password[i]
# # password[0] = "a"
# temp = temp.replace('a', 'q')
# password = temp
# print(password)

# [1차]
# # 암호화 안된 비밀번호의 값을 temp변수에 저장
# # password = temp password로 값을 다시 저장 출력
# temp =""
# for i in range(len(password)) :
#     if i % 2 == 0 : 
#         # del(password[i])
#         temp += password[i]

# password = temp
# print(password)