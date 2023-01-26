'''
    [문제]
        아래 주민번호를 가진 사람의 
        나이와 성별을 구하시오.
    [정답]
        35세
        남성
'''
jumin = "870612-1012940"

strYear = "19" + jumin[:2]
year = int(strYear)
age = 2022 - year
print(age, "세")

key = jumin[7:8]
if key == "1" or key == "3":
    print("남성")
elif key == "2" or key == "4":
    print("여성")