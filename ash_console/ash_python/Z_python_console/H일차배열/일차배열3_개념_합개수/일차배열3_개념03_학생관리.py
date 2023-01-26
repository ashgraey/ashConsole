'''
    [문제]
        number_list는 학생 다섯 명의 번호이다.
        score_list는 위 학생들의 수학 점수이다.
        60점 이상은 합격이다.
        [조건1] 합격생들의 번호와 점수 출력.
        [조건2] 전체 학생들의 총점과 평균을 출력.
        [조건3] 합격생들이 몇 명인지를 출력.
'''

number_list = [1001, 1002, 1003, 1004, 1005]
score_list  = [  10,   32,   65,   90,   89]

count = 0
total = 0
avg = 0
for i in range(len(number_list)):
    if score_list[i] >= 60:
        print("합격 :", number_list[i], ",", score_list[i])
        count += 1
    total += score_list[i]

avg = total / len(number_list)

print("총점 =", total)
print("평균 =", avg)
print("합격생 수 =", count)


