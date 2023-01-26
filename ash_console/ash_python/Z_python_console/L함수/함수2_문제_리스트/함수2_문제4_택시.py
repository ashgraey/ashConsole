"""
	[문제]
		
		현재 택시는 5 , 5 위치에 있다.
		taxi의 왼쪽세로줄은 속도를 뜻한다.
		taxi의 오른쪽세로줄은 방향 뜻하고 (북, 동, 남, 서) 를 뜻한다. 
		
		속도 와 방향은 택시가 매번이동한 내용을 기록한것이다. 

		pos 리스트에 택시가 이동한경로를 모두 기록하는 함수를 만드시오.
		단, 딕셔너리로 기록하시오.


	[예시]
		["4","북"] 은 북쪽으로 4만큼 이동한것을 뜻한다.
		y가 4증가해  x : 5 , y : 9 가된다.  	
	[정답]
		{'y': 5, 'x': 5}
		{'y': 9, 'x': 5}
		{'y': 9, 'x': 9}
		{'y': 8, 'x': 9}
		{'y': 8, 'x': 4}
		{'y': 8, 'x': 0}
		{'y': 8, 'x': 2}
"""
def movetaxi(taxi, pos):

	for i in range(len(taxi)):
		lastpos = {"y" : 0 , "x" : 0}
		lastpos["y"] = pos[-1]["y"]
		lastpos["x"] = pos[-1]["x"]
		next = taxi[i]
		if next[1] == "북":
			lastpos["y"] += next[0]
		if next[1] == "동":
			lastpos["x"] += next[0]
		if next[1] == "남":
			lastpos["y"] -= next[0]
		if next[1] == "서":
			lastpos["x"] -= next[0]
		pos.append(lastpos)

taxi = [
	[4,"북"],
	[4,"동"],
	[1,"남"],
	[5,"서"],
	[4,"서"],
	[2,"동"],
]

pos = [
	{"y" : 5 , "x" : 5}
]

movetaxi(taxi , pos)
for i in range(len(pos)):
	print(pos[i])
