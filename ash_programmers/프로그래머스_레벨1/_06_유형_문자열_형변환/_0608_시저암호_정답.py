# https://school.programmers.co.kr/learn/courses/30/lessons/12926
def solution(s, n):
    answer = ''
    temp1 = "abcdefghijklmnopqrstuvwxyz"
    temp2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(s)):
        if s[i] in temp1:
            index = (len(temp1) - 1) % (i + n)
            print(s[index])
            answer += str(s[index])
        if s[i] in temp2:
            index = (len(temp2) -1) % (i + n)
            print(s[index])
            answer += str(s[index])
    return answer

s = "AB"
n = 1

a = solution(s , n)
print(a)
