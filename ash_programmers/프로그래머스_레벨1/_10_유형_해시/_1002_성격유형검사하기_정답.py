# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    answer = ''
    test1 = "RCJATFMN"
    test2 = [0 for i in range(len(test1))]
   
    for i in range(len(choices)):
        a = "모르겠음"
        b = 0
        if choices[i] ==  4:
            pass
        elif choices[i] < 4:
            b = 4 - choices[i]
            a = survey[i][0]
        elif choices[i] > 4:
            b = choices[i] - 4
            a = survey[i][1]

        index =  test1.find(a)
        test2[index] += b
    #print(test1)
    #print(test2)
    for i in range(len(test2) // 2):
        if test2[i] >= test2[i + 4]:
            answer += test1[i]
        else:
            answer += test1[i + 4]
    return answer

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5,3,2,7,5]
r = solution(survey , choices)
print(r)