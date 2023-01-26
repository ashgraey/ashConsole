'''
    [문제]
        철수는 영어단어 타자 게임을 만들고 있다.
        한 단어씩 출력하는데 그냥 출력하면 재미없기 때문에 
        랜덤 위치에 글자 대신 * 을 한 개 출력한다.
        타자 게임을 구현을 위한 화면을 출력하시오.
    [예시]
        ja*a
        pytho*
        c+*
        n*de
        *avascript
'''
import random
wordList = ["java", "python", "c++", "node", "javascript"]

# print(len(wordList[0]) - 1)
# print(wordList[0][0])
# for i in range(len(wordList)) :

#     # for j in range(len(wordList[i])) :

#     r = random.randint(0, 4)
#     wordList[i][r] = "*"

# print(wordList)

# 1214
# 임시변수에 인덱스의 위치 순서로 저장
# 랜덤값 하나를 받고 j의 위치와 같으면 *을 저장
# for i in range(len(wordList)) :

#     r = random.randint(0,len(wordList[i]) - 1)
#     temp = ""
#     for j in range(len(wordList[i])) :
#         if j == r :
#             temp += "*"
#         else :  
#             temp += wordList[i][j]
#     # print(temp)
#     wordList[i] = temp

# print(wordList)

# # 0126
# for i in range(len(wordList)) :
#     r = random.randint(0, len(wordList[i]) - 1)
#     temp = ""

#     # j == r 같은 위치의 값일 때에만 *을 저장
#     for j in range(len(wordList[i])) :
#         if j == r :
#             temp += "*"
#         else :
#             temp += wordList[i][j]
#     wordList[i] = temp
#     print(wordList[i])


    



