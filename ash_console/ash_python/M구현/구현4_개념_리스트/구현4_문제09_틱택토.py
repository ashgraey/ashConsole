"""
   [틱택토]
	   	조건1) 구글 크롬에 "틱택토" 검색후 게임을 한번하고 
	   	          아래와같이 만들어보기.
	    조건2) P1 , P2 를 플레이어가 번갈아가면서 플레이.
	    조건3) 먼저 한줄을 완성하면 승리
	  =============
	   [처음화면]
	   0,0,0
	   0,0,0
	   0,0,0
	   [p1]인덱스 입력 : 6
	   =============
	   [1턴]
	   0,0,0
	   0,0,0
	   1,0,0
	   [p2]인덱스 입력 : 1
	   =============
	   [2턴]
	   0,2,0
	   0,0,0
	   1,0,0
	   [p1]인덱스 입력 : 3
	   =============
	   [3턴]
	   0,2,0
	   1,0,0
	   1,0,0
	   [p2]인덱스 입력 : 2
	   =============
	   [4턴]
	   0,2,2
	   1,0,0
	   1,0,0
	   [p1]인덱스 입력 : 0
	   =============
	   [5턴]
	   1,2,2
	   1,0,0
	   1,0,0
	   [p1] 승리
	   
"""

class TttGame :
    
	def __init__(self, ttt) :
		self.ttt = ttt
		self.win = 0

	def turn1(self) :
		while True :
			print("p1 turn : ")
			p1 = int(input())
			if self.ttt[p1] != 0 :
				continue 	
			else : 
				self.ttt[p1] = 1
				break

	def turn2(self) :
		# 중복 위치값이 안들어가게
		while True :
			print("p2 turn : ")
			p2 = int(input())
			if self.ttt[p2] != 0:
				continue
			else :
				self.ttt[p2] = 2 
				break                            
	def winCk(self) :
		# 가로 체크
		# if self.ttt[0] == 1 and self.ttt[1] == 1 and self.ttt[2] == 1 : 
		# 	self.win = 1
		# elif self.ttt[3] == 1 and self.ttt[4] == 1 and self.ttt[5] == 1 :
		# 	self.win = 1
		# elif self.ttt[6] == 1 and self.ttt[7] == 1 and self.ttt[8] == 1 :
		# 	self.win = 1 
		# else :
		# 	self.win = 2
		# 가로체크
		k = 0
		for _ in range(3) :
			cnt1 = 0
			cnt2 = 0 
			for _ in range(3) :
				if ttt[k] == 1 :
					cnt1 += 1
				if ttt[k] == 2 : 
					cnt2 += 2
				k += 1 
			if cnt1 == 3 :
				self.win = 1
				break 
			if cnt2 == 3 :
				self.win = 2
				break
		
		# 세로체크
		for i in range(3) :
			k = i
			cnt1 = 0
			cnt2 = 0
			for j in range(3) :
				if ttt[k] == 1 :
					cnt1 += 1 
				if ttt[k] == 2 :
					cnt2 += 1 
				k += 3
			if cnt1 == 3 :
				self.win = 1
				break
			if cnt2 == 3 :
				self.win = 2
				break 
		
		# 대각체크 0 4 8 
		if ttt[0] == 1 and ttt[4] == 1 and ttt[8] == 1 :
			self.win = 1 
		elif ttt[0] == 2 and ttt[4] == 2 and ttt[8] == 2 :
			self.win = 2
		
		# 대각체크 2 4 6 
		if ttt[2] == 1 and ttt[4] == 1 and ttt[6] == 1 :
			self.win = 1 
		elif ttt[2] == 2 and ttt[4] == 2 and ttt[6] == 2 :
			self.win = 2 


	def run(self) :
		while True :

			# print(self.ttt)
			self.turn1()
			self.turn2()
			self.winCk()
			
			i = 0
			for _ in range(3) :
				for _ in range(3) :
					print(self.ttt[i], end = " ")
					i += 1
				print()
			print()

			if self.win == 1 :
				print("p1 승리")
				break 
			elif self.win == 2 :
				print("p2 승리")
				break
			for i in range(len(ttt)) :
				ck = False
				if ttt[i] == 0 :
					ck = True
			if ck == False :
				print("무승부")
				break

ttt = [0, 0, 0, 0, 0, 0, 0, 0, 0]

tttGame = TttGame(ttt)
tttGame.run()