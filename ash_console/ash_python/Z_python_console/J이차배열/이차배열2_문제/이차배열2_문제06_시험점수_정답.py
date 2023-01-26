'''
    student리스트는 이번 학기 중간고사 성적이다.
    가로 한 줄을 기준으로 맨 앞은 번호이고, 뒤에 숫자 3개는
    각각 국어, 수학, 영어 점수이다. 
'''
student = [
    [1001, 100, 20, 32],        # 152
    [1002, 40, 43, 12],         # 95
    [1003, 60, 21, 42],         # 123
    [1004, 76, 54, 55],         # 185
    [1005, 23, 11, 76],         # 110
]
rank = [0,0,0,0,0]

'''
    [문제1] 
        모든 점수의 총합을 출력하시오.
    [정답1] 
        665
'''
print("[문제1]")
total = 0
i = 0
while i < len(student):
    j = 1
    while j < len(student[i]):
        total += student[i][j]
        j += 1
    i += 1    
print(total)

'''
    [문제2] 
        국어 1등 번호를 출력하시오.
    [정답2]         	
        1001
'''
print("[문제2]")
korMax = 0
korMaxIndex = 0
for i in range(len(student)):
    if korMax < student[i][1]:
        korMax = student[i][1]
        korMaxIndex = i
print(student[korMaxIndex][0])

'''
    [문제3] 
        수학 1등 번호를 출력하시오.
    [정답3]    
        1004    
'''
print("[문제3]")
mathMax = 0
mathMaxIndex = 0
for i in range(len(student)):
    if mathMax < student[i][2]:
        mathMax = student[i][2]
        mathMaxIndex = i
print(student[mathMaxIndex][0])

'''        	
    [문제4] 
        영어 1등 번호를 출력하시오.
    [정답4]
        1005
'''
print("[문제4]")
engMax = 0
engMaxIndex = 0
for i in range(len(student)):
    if engMax < student[i][3]:
        engMax = student[i][3]
        engMaxIndex = i
print(student[engMaxIndex][0])

'''
    [문제5] 
        전체 1등 번호를 출력하시오.
    [정답5]
'''
print("[문제5]")
maxScore = 0
maxIndex = 0
i = 0
while i < len(student):
    total = 0
    j = 1
    while j < len(student[i]):
        total += student[i][j]
        j += 1

    if maxScore < total:
        maxScore = total
        maxIndex = i
    i += 1        
print(student[maxIndex][0], maxScore)

'''
    [문제6] 
        수학점수가 국어점수 보다 높은 번호를 출력하시오.
    [정답6]
        1001 1003 1004 1005
'''
print("[문제6]")
for i in range(len(student)):
    if student[i][1] > student[i][2]:
        print(student[i][0], end=" ")
print()

'''
    [문제7]
        세 과목의 총합의 등수를 rank리스트에 저장하시오.
    [정답7]
        [2, 5, 3, 1, 4]
'''
print("[문제7]")

tot = [0, 0, 0, 0, 0]

i = 0
while i < len(student):
    total = 0
    j = 1
    while j < len(student[i]):
        total += student[i][j]
        j += 1
    tot[i] = total
    i += 1

for i in range(len(tot)):
    count = 1
    for j in range(len(tot)):
        if tot[i] < tot[j]:
            count += 1
    rank[i] = count
print(rank)

            
            


