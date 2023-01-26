'''
    [문제]
        아래 주민번호를 가진 사람의 
        나이와 성별을 구하시오.
    [정답]
        35세
        남성
'''
jumin = "870612-1012940"

year1 = 1900
year2 = 2022
temp = int(jumin[:2])
print(temp)
old = year2 - (year1 + temp)
print("나이 : ", old)

key = jumin[7:]
print(key)
# print(temp[0])
if key[0] == "1" or key[0] == "3" :
    print("남성")
elif key[0] == "2" or key[0] == "4" :
    print("여성")
