# https://school.programmers.co.kr/learn/courses/30/lessons/131127

def solution(want, number, discount):
    sample = []
    for i , v in enumerate(number):
        for j in range(v):
            sample.append(want[i])
    #print(sample)
    sample.sort()
    i = 0
    c = 0
    while True:
        sample2 = discount[i: i + 10]
        if len(sample2) < len(sample)  :
            break
        sample3 = sample2.copy()
        sample3.sort()
        #print(sample , sample3)
        check = False
        for i2, v in enumerate(sample):
            if v != sample3[i2]:
                check = True
                break
        if check == False:
            c += 1
        i += 1
    
    return c

want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana",
            "rice", "apple", "pork", "banana", "pork",
            "rice", "pot", "banana", "apple", "banana"]

r = solution(want , number , discount)
print(r)