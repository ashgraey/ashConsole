"""
[1] 문자열을 리스트로 변환

"""
a = "1 2 3 -4"
b = a.split(" ")
print(b)

"""
[2] 문자열 리스트를 숫자 리스트로 변환
"""

c = list(map(int, b))
print(c)

"""
[3] 숫자 리스트를 문자리스트로 변환
"""

d = list(map(str , c))
print(d)

"""
[4] 문자 리스트를 문자열로 변환
"""
e = " ".join(d)
print(e)