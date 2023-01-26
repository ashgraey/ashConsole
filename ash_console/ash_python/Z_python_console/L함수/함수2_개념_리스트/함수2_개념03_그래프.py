'''
    [문제] 
	  	철수는 그래프를 만들고 있다.
	  	graph리스트의 각각의 값만큼 * 을 반복적으로 가로로 출력하고,
	  	각각의 숫자마다 줄을바꿔서 출력하는 함수를 만드시오.
	[정답]
		 3   : ***
		 7   : *******
		 5   : *****
		 0   : 
		 10  : **********
		 2   : **
'''

def makeGraph(graph):
	for i in range(len(graph)):
		print(graph[i], end=" :\t")

		for j in range(graph[i]):
			print("*", end="")
		print()

graph = [3, 7, 5, 0, 10, 2]
makeGraph(graph)