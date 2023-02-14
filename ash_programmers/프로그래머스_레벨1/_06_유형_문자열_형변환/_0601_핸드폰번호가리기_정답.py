# https://school.programmers.co.kr/learn/courses/30/lessons/12948
def solution(phone_number):
    answer = ''

    for i in range(len(phone_number)):
        if i < len(phone_number) - 4:
            answer += "*"
        else:
            answer += str(phone_number[i])

    return answer


pn = "01033334444"

a = solution(pn)

print(a)