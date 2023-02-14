#https://school.programmers.co.kr/learn/courses/30/lessons/42748
def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        a = commands[i]
        b = array[a[0] - 1 : a[1] ]
        #print("b " , b)
        b.sort()
        c = b[a[2]-1]
        # print(c)
        answer.append(c)

    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
result = solution(array , commands)
print(result)
