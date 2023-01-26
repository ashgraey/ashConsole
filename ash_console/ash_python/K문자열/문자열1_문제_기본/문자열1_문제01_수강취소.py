'''
    [문제]
        regist 리스트는 수강신청을 신청한 학생명단이다.
        cancle 리스트는 수강철회를 신청한 학생명단이다.
        수강신청을 한 학생들을 last_regist 에 저장후 출력하시오.
'''

regist = ["김철민" ,"이민정" , "오사랑" , "최면술" , "김밥집" , "박대한" ,"조정민"]
cancle = ["이민정" , "최면술" , "조정민"]

last_regist = []

# regist 기준으로 중복이 없으면 last_regist에 저장
# 중복이 있으면 저장하지 않는다

# 0126
# cancle 리스트의 중복은 저장하지 않는다.
# for i in range(len(cancle)) :
#     regist.remove(cancle[i])

# for i in range(len(regist)) :
#     last_regist.append(regist[i])
# print(last_regist)

# 1차
# for i in range(len(regist)) :
#     ck = False
#     for j in range(len(cancle)) :
#         if regist[i] == cancle[j] :
#             ck = True
#             break

#     if ck == False :
#         last_regist.append(regist[i])

# # 출력
# print(last_regist)