"""
	[max게임]
	   
	    1. 가장 큰 값을 찾아 입력한다.
	    2. 정답이면 해당 값을 0으로 변경한다.
	    3. arr배열의 모든 값이 0으로 변경되면 프로그램은 종료된다.
	   	4. 가장큰값이 아닌 인덱스를 선택하면 아무일도 안생긴다.
"""

class MaxGame :
	def __init__(self, a) :
		self.a = a
		self.run()
	
	def run(self) :

		while self.runBreak() :
			print(self.a)
			num = int(input())

			if num == max(self.a) :
				for i in range(len(self.a)) :
					if num == self.a[i] :
						idx = i
						break
				self.a[idx] = 0
				
			else :
				print("MaxGame : 가장 큰 값을 찾아 입력하세용")
				continue
		print(self.a)

	def runBreak(self) :
		cnt = 0
		for i in self.a :
			if i == 0 :
				cnt += 1 
			else :
				cnt = 0
		
		if cnt == len(self.a) :
			return False
		return True

a = [10,54,345,656,87]
maxGame = MaxGame(a)

