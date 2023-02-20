"""
	[기억력 게임]
		
		1. 같은 글자가 적혀있는 카드 2장씩 5세트가있다. (총10장)
		2. 먼저 card 를 셔플한다. 
		3. card 에 있는 카드 2개를 선택한다. (마우스가없으므로 인덱스로 선택)
		4. 선택한카드 2장의 내용이 같으면 정답이고, 총 다섯번 다맞추면 게임종료.
		[조건] 
  			[1] 같은 인덱스 선택할수없다. 
			[2] 이미 선택해서 맞춘카드는 다시 선택할수없다.
		
"""
import random

class memoryGame :
    def __init__(self, c) :
        self.card = c
        self.count = 0
        self.run()
        
    def cardShuffle(self) :
        for _ in range(100) :
            r = random.randint(0, len(self.card) - 1)
            temp = self.card[0]
            self.card[0] = self.card[r]
            self.card[r] = temp
    
    
    def breakCk(self) :
        if self.count == 5 :
            print("게임종료")
            return False
        return True
        
	
    def	run(self) :
        self.cardShuffle()
        
        while self.breakCk() :
            print(self.card)
            print("입력1 : 입력2 : ")
            idx1, idx2 = map(int, input().split())
            
            if idx1 == idx2 : 
                continue
            
            if self.card[idx1] == self.card[idx2] :
                   print("정답")
                   self.count += 1 
            else :
                print("오답")
            
            # if self.count == 5 : 
            #     break
	
card = ['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'e', 'e' ]
memoryGame = memoryGame(card)
# memoryGame.cardShuffle()
# print(memoryGame.card)