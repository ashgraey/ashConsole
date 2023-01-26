'''
    [문제]
        a리스트는 단어들이 모여있는 리스트이다.
        search는 검색하고 싶은 단어이다.
        a리스트에서 해당 단어를 검색해서 출력하시오.
        단, 부분 검색도 되어야한다.
        
    [예시] 
        school, teacher, child
'''


a =["school", "teacher", "child","father", "love"]

search = "ch"

# 문자열이 하나의 배열이라 생각하자
# 이차배열 형식으로 출력
for i in range(len(a)) :
    print(a[i])
# 폐기
# ======================================
# 문자열 변환
# temp =""
# for i in range(len(a)) :
#     temp += a[i]
#     if i != len(a) - 1 :
#         temp += ","
# print(temp)
# print(len(temp))
# print(len(search))

# 28번 검사해야함
# for i in range(len(temp) - 4) :

#     cnt = 0 
#     for j in range(len(search)) :
#         if temp[j + i] == search[j] :
#             cnt += 1 
    
#     if cnt == 2 :
# =======================================

result = []
# a리스트 길이값만큼 돌린다.
for i in range(len(a)) :

    # 마지막 인덱스까지 돌려야 인덱스에러가 안뜸 ex/ len(a[0]) : 5, lastIdx : 4 ... 4,5
    for j in range(len(a[i]) - 1) :
        cnt = 0
        # 이차배열로 이해해야 풀수있음 
        for k in range(len(search)) :
            if a[i][j + k] == search[k] :
                cnt += 1
  
        # cnt : 중복검사
        # cnt값이 2이면 True, result 배열에 결과값 추가
        if cnt == 2 :
            result.append(a[i])

print(result)