# https://school.programmers.co.kr/learn/courses/30/lessons/12915
def solution(strings, n):
    for i in range(len(strings)):
        for j in range(len(strings)):
            a = strings[i]
            b = strings[j]
            c = strings[i][n]
            d = strings[j][n]
            if c < d:
                temp = strings[i]
                strings[i] = strings[j]
                strings[j] = temp
            
            if c == d:
                if a < b:
                    temp = strings[i]
                    strings[i] = strings[j]
                    strings[j] = temp

    return strings


strings =["abce", "abcd", "cdx"]
n = 2
a = solution(strings , n)
print(a)