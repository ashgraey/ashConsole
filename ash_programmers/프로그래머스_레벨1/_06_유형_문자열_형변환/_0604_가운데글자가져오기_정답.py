# https://school.programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    answer = ''
    index = len(s) // 2
    if len(s) % 2 == 0: 
        answer = s[index-1] + s[index]
    else:
        answer = s[index]
    return answer

s = "abcde"
a = solution(s)
print(a)