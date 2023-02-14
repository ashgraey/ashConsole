# https://school.programmers.co.kr/learn/courses/30/lessons/72410
def solution(new_id):
    answer = new_id
    answer = answer.lower()
    temp1 = "abcdefghijklmnopqrstuvwxyz0123456789-_."
    print(answer)

    for i in range(len(answer)):
        if answer[i] not in temp1:   
            answer = answer.replace(answer[i] , ' ')
    print(answer)
    answer = answer.replace(' ' , '')

    print(answer)
    while True:
        check = False
        if ".." in answer:
            answer = answer.replace("..", '.')
            check = True
        if check == False:
            break
    print(answer)

    if answer[0] == '.':
        answer = answer[1:]
    print(answer)

    if answer == '':
        answer += 'a'

    if answer[-1] == '.':
        answer = answer[:-1]
    print(answer)

    if answer == '':
        answer += 'a'

    if len(answer) >= 16:
        answer = answer[:15]
    print(answer)

    if answer[-1] == '.':
        answer = answer[:-1]
    print(answer)

    if len(answer) <= 2:
        temp = answer[-1]
        while len(answer) < 3:
            answer += temp

    return answer

new_id = "...!@BaT#*..y.abcdefghijklm"
#new_id = "z-+.^."
#new_id = "=.="
#new_id = "123_.def"
#new_id = "abcdefghijklmn.p"
result = solution(new_id)
print(result)