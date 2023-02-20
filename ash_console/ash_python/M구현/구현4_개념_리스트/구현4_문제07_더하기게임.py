"""
	[더하기게임]	
		1) 1~10 사이의 숫자를 랜덤으로 7개보여준다. (중복금지)
		2) 그안에서 3개의 인덱스를 고를수있게해준다. (중복금지)
		3) 숫자를 하나 제시하는데 인덱스3개의 값의 합이
		   제시된 숫자랑 같으면 정답. 
		   단, 정답은 여러개 일수있다. 
		4) 반드시 정답의 경우의 수는 있어야한다.	 
		   단! 중복으로 값을 고를순없다. 
		[예시]

		    보기  
      		a = [1,5,8,6,4,2,9]
		    r = 13	
		[정답] 
  			인덱스를 세개를 고른다. [0,2,4] 각각의 값은 이와 같다. [1 + 8 + 4] 합이 13이므로 정답	
		[주의]
		    인덱스를 이와같이 똑같은 자리는 고를수없다. [5,5,6] 
"""
import random 
class PlusGame :
	def __init__(self, a, r) :
		self.a = a 
		self.r = r
		self.idx1 = 0
		self.idx2 = 0
		self.idx3 = 0 
		# self.idxList = []
		self.run()
	
	def setRandom(self) :
		for _ in range(7) :
			self.a.append(random.randint(1, 10))
	
	def indexSet(self) :
		while True :
			print("인덱스를 3개 입력하시오.")
			self.idx1, self.idx2, self.idx3 = map(int, input().split())
			idxList = [self.idx1, self.idx2, self.idx3]
			# print(idxList)
			
			# 중복검사
			if idxList[0] == idxList[1] or idxList[0] == idxList[2] or idxList[1] == idxList[2] :
				# print(True)
				continue
			break
			
	def run(self) :
		self.setRandom()
		print(self.a)

		while True :
			self.indexSet()

			print("결과값을 입력해주세요.")
			self.r = int(input())

			total = self.a[self.idx1] + self.a[self.idx2] +self.a[self.idx3]
			print("total : ", total)

			if self.r == total :
				print("정답입니다.")
				break
			else :
				continue 

a = []
r = 0
plusGame = PlusGame(a,r)