'''
문제 1157)
알파벳 대소문자로 된 단어가 주어지면, 
이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
단, 대문자와 소문자를 구분하지 않는다.

'''

# word = input()
# word = "Mississipi"
word = input().lower()
wordList = list(set(word)) # 중복제거 후 배열변환
# print(word)
# print(wordList)

# 가장 많이 사용되는 알파벳
cntList = []
for i in range(len(wordList)) :

    cnt = 0 
    for j in range(len(word)) :
        if wordList[i] == word[j] :
            cnt += 1
    cntList.append(cnt)

# print(cntList)

# max값 구하기
max = 0
maxIdx = 0 
for i in range(len(cntList)) :
    if max < cntList[i] :
        max = cntList[i] 
        maxIdx = i

# print("max : ", max)
# print("maxIdx : ", maxIdx)

# max값이 중복일 경우 ?출력, 아니면 첫째줄 대문자 출력
ck = False
for i in range(len(cntList)) :
    if i != maxIdx and cntList[maxIdx] == cntList[i] :
        ck = True
        break

if ck == False :
    print(wordList[maxIdx].upper())
else : 
    print("?")
