# https://school.programmers.co.kr/learn/courses/30/lessons/12943
def solution(num):
    answer = 0
    
    while True :
        if num % 2 == 0 :
            num = num // 2 
            answer += 1

        elif num != 1 and num % 2 == 1 :
            num = (num * 3) + 1
            answer += 1 

        # print(num)
        if num == 1 :
            # return count
            break

        if answer >= 500 :
            answer = -1 
            # return count
            break
    return answer

n = int(input())
result = solution(n)

print(result)

