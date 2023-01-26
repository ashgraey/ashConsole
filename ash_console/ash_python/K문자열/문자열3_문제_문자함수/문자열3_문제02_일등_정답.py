'''
   [문제]
        text는 학생점수를 기록한 데이터이다.
        전체 평균과 일등의 점수를 출력하시오.
    [정답]
        평균 = 30.2
        일등 점수 = 80
'''
text = "13,32,80,3,23"

scoreList = text.split(",")
print(scoreList)

for i in range(len(scoreList)):
    scoreList[i] = int(scoreList[i])
print(scoreList)

total = 0
avg = 0
max = 0
for i in range(len(scoreList)):
    total += scoreList[i]
    if max < scoreList[i]:
        max = scoreList[i]
avg = total / len(scoreList)
print("평균 =", avg)
print("일등 점수 =", max)


