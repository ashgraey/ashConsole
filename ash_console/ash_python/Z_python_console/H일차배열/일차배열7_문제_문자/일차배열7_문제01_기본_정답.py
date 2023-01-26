'''
    [문제]
        문자열 hello를 olleh로 출력하시오.
'''
text = "hello"

# 방법1
for i in range(len(text)):
    print(text[len(text) - 1 - i], end="")
print()

# 방법2
temp = ""
index = len(text) - 1
for i in range(len(text)):
    temp += text[index]
    index -= 1
print(temp)