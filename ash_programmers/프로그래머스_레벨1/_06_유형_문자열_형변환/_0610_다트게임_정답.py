# https://school.programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    answer = 0
    numarr = []
    oparr = []
    while True:
        check = False
        for i in range(len(dartResult)):
            a = dartResult[i]
            if a in "SDT":
                if i != len(dartResult) - 1 and dartResult[i + 1] in "*#":
                    b = dartResult[:i + 2]
                    numarr.append(b[:i])
                    oparr.append(b[i:])                 
                    dartResult = dartResult[i + 2:]
                    check = True
                else:
                    b = dartResult[:i + 1]
                    numarr.append(b[:i])
                    oparr.append(b[i:])
                    dartResult = dartResult[i + 1:]
                    check = True
                break
        if check == False:
            break
    print(numarr)
    print(oparr)
    for i in range(len(oparr)):
        a = int(numarr[i])
        b = oparr[i]
        c = ""
        if len(oparr[i]) == 2:
            b = oparr[i][0]
            c = oparr[i][1]
        if b == 'S':
            numarr[i] = a 
        if b == 'D':
            numarr[i] = a ** 2
        if b == 'T':
            numarr[i] = a ** 3
        if c == '#':
            numarr[i] *= -1
        if c == '*':
            if i == 0:
                numarr[i] *= 2
            else :
                numarr[i-1] *= 2
                numarr[i] *= 2
    print(numarr)
    answer = sum(numarr)
    return answer
dartResult = "1D2S#10S"
result = solution(dartResult)
print(result)