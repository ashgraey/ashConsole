# https://school.programmers.co.kr/learn/courses/30/lessons/86491
def getMin(arr):
    t1 = arr[0]
    for i in range(len(arr) - 1):      
        t2 = arr[i + 1]

        m1 = max(t1[0] , t2[0])
        m2 = max(t1[1] , t2[1])

        m3 = max(t1[0] , t2[1])
        m4 = max(t1[1] , t2[0])
        #print(m1 , " " , m2 , " " , m3 , " " , m4)
        r1 = m1 * m2
        r2 = m3 * m4
        #print(r1 , " " , r2)
        if r1 > r2:
            t1 = [m3, m4]
        else:
            t1 = [m1, m2]
    #print(t1)
    return t1

def solution(size):
    answer = 0
    c = getMin(size)

    answer = c[0] * c[1]
    return answer

size = [[60, 50], [30, 70], [60, 30], [80, 40]]
#size = [[3, 5], [6, 2]]
result = solution(size)
print(result)

