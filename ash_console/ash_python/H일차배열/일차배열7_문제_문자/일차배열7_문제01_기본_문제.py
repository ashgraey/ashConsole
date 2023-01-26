'''
    [문제]
        문자열 hello를 olleh로 출력하시오.
'''
text = "hello"
# [1116]
# temp = ""
# idx = len(text) - 1
# for i in range(len(text)) :
#     # print(text[idx], end = "")
#     temp += text[idx]
#     idx -= 1
# print(temp)

# [1차]
# # 방법 1
# # 거꾸로 출력
# for i in range(len(text)) :
#     print(text[(len(text) - 1) - i], end = "")
   
# print()

# # 방법2
# # temp라는 문자열 변수안에 text의 마지막 인덱스의 값부터 저장
# # idx의 변수를 -1씩 감소시킨다.
# temp = ""
# idx = len(text) - 1 
# for i in range(len(text)) :
#     temp += text[idx]
#     idx -= 1
# print(temp)