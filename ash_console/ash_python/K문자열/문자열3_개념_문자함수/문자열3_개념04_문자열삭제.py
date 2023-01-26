'''
    [문제]
        아래 데이터는 학생점수데이터이다. 
        번호, 이름, 점수 이렇게 한 세트이다.
        일등을 삭제하고 다시 문자열로 만드시오.
    [정답]
        1001,김철수,17/1003,신민아,49
'''
text = "1001,김철수,17/1002,이민수,80/1003,신민아,49"
temp = text.split("/")

a = []
for i in range(len(temp)):
    temp2 = temp[i].split(",")
    temp2[0] = int(temp2[0])
    temp2[2] = int(temp2[2])
    a.append(temp2)
print(a)

max = a[0][2]
index = 0
for i in range(len(a)):
    if max < a[i][2]:
        max = a[i][2]
        index = i
print(max, ",", index)    
a.remove(a[index])
print(a)

text = ""
for i in range(len(a)):
    text += str(a[i][0])
    text += ","
    text += a[i][1]
    text += ","
    text += str(a[i][2])
    text += "/"
    
print(text) # 1001,김철수,17/1003,신민아,49/ 
text = text[:len(text)-1] # 마지막 / 를 제거한다. 
print(text)






