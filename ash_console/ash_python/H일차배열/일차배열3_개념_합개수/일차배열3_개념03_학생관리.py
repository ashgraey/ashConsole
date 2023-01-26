'''
    [문제]
        number_list는 학생 다섯 명의 번호이다.
        score_list는 위 학생들의 수학 점수이다.
        60점 이상은 합격이다.
        [조건1] 합격생들의 번호와 점수 출력.
        [조건2] 전체 학생들의 점수와 평균을 출력.
        [조건3] 합격생들이 몇 명인지를 출력.
'''

number_list = [1001, 1002, 1003, 1004, 1005]
score_list = [10, 32, 65, 90, 89]

total = 0
count = 0
size = len(number_list)

for i in range(size):
    if score_list[i] >= 60:
        print("합격 : " , number_list[i] , " " , score_list[i])
        count += 1
    total += score_list[i]

print("총합 :", total)
print("평균 :", total/5)
print("합격생 수 :", count)





