"""
	[문제]
		number 와 name 과 score 리스트의 각각의 값은 학생데이터이다.
		data 리스트에 한줄로 저장하는 함수를 만드시오.
	[예시]
		data = [1001,"김철수",32,1002,"이만수",54,1003,"조영민",12]
"""
def oneline(number , name, score, data):
    for i in range(len(number)):
        data.append(number[i])
        data.append(name[i])
        data.append(score[i])

number= [1001,1002,1003];
name = ["김철수","이만수","조영민"]
score = [32,54,12]
data = []

oneline(number , name , score, data)
print(data)