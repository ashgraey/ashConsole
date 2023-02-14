# https://school.programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    week = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    mon = [31,29,31,30,31,30,31,31,30,31,30,31]
    day = 0
    for i in range(a - 1):
        day += mon[i]
    day += b - 1
    #print("day : " , day)
    index = (day + 5) % 7   
    #print(index)
    return week[index]

a = 5
b = 24
r = solution(a , b)
print(r)