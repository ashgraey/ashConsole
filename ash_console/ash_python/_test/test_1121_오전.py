
"""
    [문제]
        아래는 우리반 학생들 이름을 배열로 나열한것이다. 
        팀포트폴리오를 위해 3명씩 5팀을 만들려고한다. 
        실행할때마다 한팀에 3명씩 5팀을 만들어, 
        각각 , a,b,c,d,e 배열에 저장후 출력하시오. 
        단, 매번 팀원은 랜덤으로 배정된다. 
"""
import random 

arr = [
"권종률" , "김식" , "김유정" , 
"김지현" , "송민수" , "신정규" ,
"안성현" , "안지선" , "양나비" ,
"유재형" , "이주호" , "장준영" , 
"황지현" , "김사라" , "이근일"]

a = []
b = []
c = []
d = []
e = []

for i in range(100) :
    idx1 = random.randint(0, len(arr) - 1)
    idx2 = random.randint(0, len(arr) - 1)

    temp = arr[idx1]
    arr[idx1] = arr[idx2]
    arr[idx2] = temp


for i in range(len(arr)) :
    if i < 3 :
        a.append(arr[i])
    elif i < 6 :
        b.append(arr[i])
    elif i < 9 :
        c.append(arr[i])
    elif i < 12 :
        d.append(arr[i])
    else :
        e.append(arr[i])

print(a)
print(b)
print(c)
print(d)
print(e)

# [정답]
# print(arr)
# i = 0
# while i <= 1000:
#     r = random.randint(0, 14)
#     temp = arr[r]
#     arr[r] = arr[0]
#     arr[0] = temp
#     i += 1

# print(arr)

# i = 0
# while i < 3:
#     a.append(arr[i])
#     i += 1

# while i < 6:
#     b.append(arr[i])
#     i += 1

# while i < 9:
#     c.append(arr[i])
#     i += 1

# while i < 12:
#     d.append(arr[i])
#     i += 1

# while i < 15:
#     e.append(arr[i])
#     i += 1

# print(a, b, c, d, e)