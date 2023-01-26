'''
    [문자열(문자여러개)]
'''
a = "python"    # 큰따옴표로 감싼다.
print(a)

b = 'python'    # 작은따옴표로 감싼다.
print(b)

c = "'hi'"      # 작은따옴표를 표시하고 싶을 때는 큰따옴표로 감싼다.
print(c)

d = '"hi"'      # 큰따옴표를 표시하고 싶을 때는 작은따옴표로 감싼다.
print(d)

# 곱하기(*) : 파이썬만의 특징으로 문자열에 곱하기를 사용하면 곱한 개수만큼 저장된다.
text = "hi" * 3 
print(text)

# 더하기(+) : 더하기를 사용하면 서로 다른 문자를 연결할 수 있다.
sung = "홍"
name = "길동"
fullname = sung + name
print(fullname)


# 문자열 초기화 : 보통 큰따옴표에 아무것도 표시하지 않고 초기화한다.
a = ""


# 문자열 길이 : 리스트와 마찬가지로 len(문자열)을 사용한다.
text = "abcde"
print(len(text))