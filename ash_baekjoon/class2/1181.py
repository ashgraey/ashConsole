'''
문제 단어정렬//
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
    길이가 짧은 것부터
    길이가 같으면 사전 순으로
단, 중복된 단어는 하나만 남기고 제거해야 한다.

input//
첫째 줄에 단어의 개수 N이 주어진다.
(1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다.
주어지는 문자열의 길이는 50을 넘지 않는다.

output//
조건에 따라 정렬하여 단어들을 출력한다.

조건2 // 길이가 같으면 사전순으로를 못 풀겠음
'''

# 나의 방식
n = int(input())

word = []
for _ in range(n):
    word.append(input())

# 중복제거 for
# tempList = []
# for i in range(len(word)):
#     ck = False
#     for j in range(len(tempList)):
#         if word[i] == tempList[j]:
#             ck = True
#             break

#     if ck == False:
#         tempList.append(word[i])
# word = tempList

set_word = list(set(word))

# 정렬
sort_word = []
for i in set_word:
    sort_word.append((len(i), i))

result = sorted(sort_word)

for len_word, word in result:
    print(word)

# 정렬 sort() // 시간초과 뜸
# tempList.sort()
# tempList.sort(key=len)
# word = tempList
# print(word)


# sortTemp = []
# for i in range(len(tempList)):
#     min = len(tempList[i])
#     minIdx = 0
#     for j in range(i, len(tempList)):
#         tempMin = len(tempList[j])
#         if min >= tempMin:
#             min = tempMin
#             minIdx = j

#     sortTemp.append(tempList[minIdx])
#     temp = tempList[i]
#     tempList[i] = tempList[minIdx]
#     tempList[minIdx] = temp
# print(sortTemp)

# 다른사람 풀이
# n = int(input())
# nList = []
# for _ in range(n):
#     nList.append(input())

# # 중복제거
# sList = set(nList)  # 딕셔너리로 변환
# nList = list(sList)  # 리스트로 다시변환

# # 정렬
# nList.sort(key=len)
# print(nList)
