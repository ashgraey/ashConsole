# https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    s = s.split(" ")
    #print(s)
    for i , v in enumerate (s):
        if v != "":
            st = v[0].upper()
            st += v[1:].lower()
            s[i] = st + " "
    print(s) # 맨마지막 문자열의 공백은 뒤에서 제거한다. 
    st = ""
    for v in s:
        if v == "":
            st += " "
        else:
            st += v
    st = st[:-1] # 맨뒤의 공백 제거 
    return st

s = "     3people     unFollowed     me"	
s = "for the last week"
# s = "3people unFollowed me"	
r = solution(s)
print(r)


# 공백이 여러줄이 있는 함정이 있다. 