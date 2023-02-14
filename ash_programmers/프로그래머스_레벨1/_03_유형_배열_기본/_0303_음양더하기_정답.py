# https://school.programmers.co.kr/learn/courses/30/lessons/76501
def solution(absolutes, signs):
    total =0
    for i in range(len(absolutes)):
        if signs[i] == True:
            total += absolutes[i]
        else:
            total -= absolutes[i]

    return total


absolutes = [4,7,12]
signs = [True,False,True]

result = solution(absolutes , signs)
print(result)