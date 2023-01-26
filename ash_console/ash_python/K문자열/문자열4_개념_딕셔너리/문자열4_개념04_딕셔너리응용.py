"""
    [딕셔너리응용]
        딕셔너리는 단독으로 사용하기보다는 리스트와 함께 2차원 모양으로 사용된다. 
"""
studentList = []
info = {"이름":"김철수", "수학":100, "국어":32}
studentList.append(info)

info = {"이름":"이만수", "수학":11, "국어":84}
studentList.append(info)

info = {"이름":"박영희", "수학":95, "국어":58}
studentList.append(info)

for i in range(len(studentList)):
    print(studentList[i])
print("----------------------------")
"""
    [문제]
        studentList리스트에 각학생점수들의 총점과 평균을 추가하시오.
"""
for i in range(len(studentList)):
    studentList[i]["총점"] = studentList[i]["수학"] + studentList[i]["국어"]
    studentList[i]["평균"] = studentList[i]["총점"] / 2


for i in range(len(studentList)):
    print(studentList[i])
