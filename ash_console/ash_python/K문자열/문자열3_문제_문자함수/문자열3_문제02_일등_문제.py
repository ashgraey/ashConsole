'''
   [문제]
        text는 학생점수를 기록한 데이터이다.
        전체 평균과 일등의 점수를 출력하시오.
    [정답]
        평균 = 30.2
        일등 점수 = 80
'''
text = "13,32,80,3,23"

# score = text.split(',')
# print(score)

# 정수로 형변환
# scList = []
# for i in range(len(score)) :
#     scList.append(int(score[i]))
# print(scList)

# # 평균 / 일등
# tot = 0
# max = scList[0]
# for i in range(len(score)) :
#     tot += scList[i]
#     if scList[i] > max :
#         max = scList[i]
# avg = tot / len(score)
# print(avg)
# print(max)

# 0127
score = text.split(",")
print(score)

max = score[0]
maxIdx = 0
tot = 0
for i in range(len(score)) :
    if max < score[i] :
        max = score[i]
        maxIdx = i
    tot += int(score[i])

avg = tot / len(score)
print(score[maxIdx], avg)

