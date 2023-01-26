# 기억력 게임 : 클래스 + 메서드

import random

class MemoryGame:
    count = 0                  # 정답을 맞춘 개수
    size = 10
    front = []
    back = []
    
    def set_game(self):
        j = 1
        for i in range(10):
            self.back.append(0)
            if i % 2 == 0 and i != 0:
                j += 1
            self.front.append(j)

    def suffle_front(self):
        for i in range(100):
            r = random.randint(0, 9)

            temp = self.front[0]
            self.front[0] = self.front[r]
            self.front[r] = temp       

    def run(self):
        self.set_game()
        self.suffle_front()

        while True:
            print(self.front)
            print(self.back)

            if self.count == 5:
                print("게임 종료")
                break

            index1 = int(input("인덱스1 입력 : "))
            index2 = int(input("인덱스2 입력 : "))

            if self.front[index1] == self.front[index2]:
                self.back[index1] = self.front[index1]
                self.back[index2] = self.front[index2]

                self.count += 1
        

#------------------------------------------------------------------
mg = MemoryGame()
mg.run()