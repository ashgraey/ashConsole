# https://school.programmers.co.kr/learn/courses/30/lessons/12930
def solution(s):
    answer = ''
    a = s.split(" ")
    print(a)
    main = ""
    for i in range(len(a)):
        temp = ""
        for j in range(len(a[i])):
            if j % 2 == 0:
                temp += a[i][j].upper()
            else:
                temp += a[i][j].lower()
        main += temp
        main += " "
    answer = main[:-1]
    return answer

s = "try hello world"
a = solution(s)
print(a)