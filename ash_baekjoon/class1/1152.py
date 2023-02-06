'''
문제 1152)
영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열에는 몇 개의 단어가 있을까? 
이를 구하는 프로그램을 작성하시오. 
단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.
'''

# a = "The Curious Case of Benjamin Button"
# cnt = 0
# for i in range(len(a)):
#     if a[i] == " ":
#         cnt += 1

# word = cnt + 1
# print(word)

# word = input().split() # split()함수의 매개변수의 기본값은 none이며, 이때 동작은 띄워쓰기, 엔터를 구분자로 문자열을 자른다.
# print(word)

# word = input()
# wordList = word.split()
# print(wordList)
# print(len(wordList))

word = input().split()
print(len(word))
