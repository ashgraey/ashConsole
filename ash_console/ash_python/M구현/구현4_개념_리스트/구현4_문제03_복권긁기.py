"""
	[복권긁기]
		[1] a 리스트에 숫자7을 세개 , 숫자 1을 7개를 저장한다. 
		[2] 위치는 랜덤으로 저장한다.
		[3] 사용자는 인덱스로 위치 3개를 선택할수있다. 
		[4] 전부 7이면 당첨 아니면 꽝 출력 

"""

# 구성
# 1) aList 숫자 7 3개, 숫자 1 7개 총 10개
# 2) 사용자 인덱스 선택 3개
# 3) 당첨 체크, 7이 3개면 당첨 아니면 꽝
import random

class LottoManager : 
	# 생성자
	def __init__(self, lottoList) :
		self.lottoList = lottoList

	# lottoList 생성
	def lottoCreate(self) :
		for _ in range(7) :
			self.lottoList.append(1)
		
		for _ in range(3) :
			self.lottoList.append(7)

		# shuffle 
		for _ in range(100) :
			r = random.randint(0, len(self.lottoList) - 1)
			temp = self.lottoList[0]
			self.lottoList[0] = self.lottoList[r]
			self.lottoList[r] = temp
		
		# print(self.lottoList)
		# return self.lottoList

	def run(self) :
		self.lottoCreate()
		print(self.lottoList)
		chIdx = list(map(int, input().split()))
		# print(chIdx)
		# 당첨 검사
		if self.lottoList[chIdx[0]] == 7 and self.lottoList[chIdx[1]] == 7 and self.lottoList[chIdx[2]] == 7 :
			print("당첨")
		else :
			print("꽝")


a = []
lotto = LottoManager(a)
# print(lotto.lottoList)
# lotto.lottoCreate()
lotto.run()