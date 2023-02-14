# https://school.programmers.co.kr/learn/courses/30/lessons/77484
def solution(lottos, win_nums):
    answer = []
    count = 0
    count2 = 0
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            count += 1
        if lottos[i] == 0:
            count2 += 1
    # print(count , " " , count2)

    if count == 0 and count2 == 0:
        answer.append(6)
    else:
        answer.append(7-(count + count2))
    if count == 0:
        answer.append(6)
    else:
        answer.append(7 - count)

    return answer

lottos = [0, 0, 0, 0, 0, 0]
win_nums = [31, 10, 45, 1, 6, 19]	


result = solution(lottos , win_nums)
print(result)