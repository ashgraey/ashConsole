'''
    [문자열 수정 시 주의점]
        문자열은 리스트와 유사하지만 한 글자를 직접 수정하는 건 불가능하다.
        처음부터 새로 변수를 만들어야 한다.       
        또는, replace를 사용한다. 
'''
'''
    [문제]
        text변수에서 y를 i로 변경하시오.
'''
text = "python"

# text[1] = 'i' # 에러가 발생한다. 직접 수정은 불가능하다.
print(text)
b = ""
for i in range(len(text)):
    if text[i] == 'y':
        b += 'i'
    else:
        b += text[i]
text = b # 수정한 변수를 넣어준다.
print(text)
print("--------------------")

# replace
'''
    [문제]
        h를 k로 변경하시오.
'''
c = 'hello world'
print(c)
c = c.replace('h' , 'k')
print(c)
