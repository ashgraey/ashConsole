
studentList = []
info = {"이름":"김철수", "수학":100, "국어":32}
studentList.append(info)

info = {"이름":"이만수", "수학":11, "국어":84}
studentList.append(info)

info = {"이름":"박영희", "수학":95, "국어":58}
studentList.append(info)

for i in range(len(studentList)):
    studentList[i]["총점"] = studentList[i]["수학"] + studentList[i]["국어"]
    studentList[i]["평균"] = studentList[i]["총점"] / 2

'''
    [문제1]
        수학이 꼴등인 학생의 이름을 출력하시오.
    [정답1]
        이만수
'''
print("[문제1]")
minScore = 100
minIndex = 0
for i in range(len(studentList)):
    if minScore > studentList[i]["수학"]:
        minScore = studentList[i]["수학"]
        minIndex = i
print("수학점수가 꼴등인 학생 =", studentList[minIndex]["이름"])

'''
    [문제2]
        총점이 높은 순서대로 학생의 이름을 출력하시오.
    [정답2]
        박영희 김철수 이만수 
'''
print("[문제2]")
i = 0
while i < len(studentList):
    maxScore = 0
    maxIndex = 0

    j = i
    while j < len(studentList):
        if maxScore < studentList[j]["총점"]:
            maxScore = studentList[j]["총점"]
            maxIndex = j
        j += 1

    temp = studentList[i]
    studentList[i] = studentList[maxIndex]
    studentList[maxIndex] = temp

    print(studentList[i]["이름"], end=" ")
    i += 1
print()

'''
    [문제3]
       인덱스가 1인 학생을 삭제 후, 전체 출력하시오.
    [정답3]
        [{'이름': '박영희', '수학': 95, '국어': 58, '총점': 153},
         {'이름': '이만수', '수학': 11, '국어': 84, '총점': 95}]
'''
print("[문제3] 방법1 >>> del 함수 사용")
# del studentList[1]
# print(studentList)

print("[문제3] 방법2")
delIndex = 1
temp = studentList
studentList = []
for i in range(len(temp)):
    if i != delIndex:
        studentList.append(temp[i])
print(studentList)
