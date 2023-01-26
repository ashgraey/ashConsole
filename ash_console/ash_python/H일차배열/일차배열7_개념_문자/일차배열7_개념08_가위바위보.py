"""
    [문제]
        아래는 두학생의 가위바위보 데이터이다. 
        철수는 몇번 승리했는지 출력하시오.
"""
철수 = ["가위" , "바위" , "바위" , "보" , "가위"]
민수 = ["보" ,"가위" ,"바위" , "가위" , "보"]
wincount = 0

for i in range(len(철수)):
    a = 철수[i]
    b = 민수[i]

    if a == b:
        print("비김")
    elif a == "가위" and b == "보":
        print("이김")
        wincount += 1
    elif a == "바위" and b == "가위":
        print("이김")
        wincount += 1
    elif a == "보" and b == "바위":
        print("이김")
        wincount += 1
    else:
        print("짐")

print(wincount)
