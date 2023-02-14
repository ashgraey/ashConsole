
def solution(s):
    answer = 0
    sample = ["zero" , "one" , "two" , "three" , "four" , "five" , "six" , "seven" , "eight" , "nine"]
    for i in range(len(sample)):
        if sample[i] in s:
            print(sample[i])
            ri = sample.index(sample[i])
            s = s.replace(sample[i] , str(ri))
    answer = int(s)
    return answer

s = "one4seveneight"

result = solution(s)

print(result)

