# https://school.programmers.co.kr/learn/courses/30/lessons/12919
def solution(seoul):
    idx = 0
    answer = ''
    for i in range(len(seoul)) :
        if seoul[i] == "kim" :
            idx += 1 
            print(seoul[i])
    
    answer += "김서방은 "
    answer += str(idx)
    answer += "에 있다"
    return answer


s = ["Jane" , "Kim"]
solution(s)
# a = solution(s)
# print(a)