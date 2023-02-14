
"""
    [1] 아래문자열을 첫글자는 대문자로 나머지는 소문자로 변환하시오.
    [2] 단 , 공백을 그대로 유지한다.
    [3] 첫글자가 숫자면 숫자를 유지한다. 

    [예시]
        [1] "     3people     unFollowed     me  "
        [2] "     3people     Unfollowed     Me  "

"""

s = "     3people     unFollowed     me  "	
print(s)

s = s.split(" ")
#print(s)

for i , v in enumerate (s):
    if v != '':
        a = v[0].upper()
        b = v[1:].lower()
        s[i] = (a + b) + " " # 마지막 글자는 공백이 한칸 더들어갈수밖에 없다. 추후에 삭제한다.
print(s)

st = ""

for i , v in enumerate(s):
    if v == '':
        st += " "
    else:
        st += v

print(st)
st = st[:-1] # 마지막 공백 삭제
print(st)