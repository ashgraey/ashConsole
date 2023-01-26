# 딕셔너리와 리스트

studentList = []
info = {"이름":"김철수", "수학":100, "국어":32}
studentList.append(info)

info = {"이름":"이만수", "수학":11, "국어":84}
studentList.append(info)

info = {"이름":"박영희", "수학":95, "국어":58}
studentList.append(info)

while True:
    for i in range(len(studentList)):
        print(studentList[i])
    print()
    
    print("[1]추가")
    print("[2]삭제")
    print("[3]정렬")
    print("[4]출력")
    print("[5]종료")

    sel = int(input("메뉴 선택 : "))

    if sel == 1:
        name = input("추가할 이름 입력 : ")
        math = int(input("수학성적 입력: "))
        kor = int(input("국어성적 입력 : "))

        temp = {}
        temp["이름"] = name
        temp["수학"] = math
        temp["국어"] = kor

        studentList.append(temp)
    elif sel == 2:
        del_name = input("삭제할 이름 입력 : ")

        # 삭제할 인덱스 검색
        del_idx = -1
        for i in range(len(studentList)):
            if studentList[i]["이름"] == del_name:
                del_idx = i
        if del_idx == -1:
            print("이름을 다시 확인해주세요.")
            continue
        
        # 삭제
        temp = studentList
        studentList = []

        for i in range(len(temp)):
            if i != del_idx:
                studentList.append(temp[i])
    elif sel == 3:
        for i in range(len(studentList)):
            min_name = studentList[i]["이름"]
            min_idx = i
            for j in range(i, len(studentList)):
                if min_name > studentList[j]["이름"]:
                    min_name = studentList[j]["이름"]
                    min_idx = j
            temp = studentList[i]
            studentList[i] = studentList[min_idx]
            studentList[min_idx] = temp
                    
    elif sel == 4:
        for i in range(len(studentList)):
            print("이름 : %s\t수학 : %d점\t국어 : %d점\t" % (studentList[i]["이름"], studentList[i]["수학"], studentList[i]["국어"]))
    elif sel == 5:
        break