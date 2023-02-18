'''
기억력 게임 class + 메서드

[2, 2, 5, 5, 3, 4, 4, 1, 3, 1]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
인덱스1 입력 :
인덱스2 입력 :

기억력게임을 만드시오.

'''
import random


class MemoryGame:

    memory = []
    user = []
    cnt = 0
    exit = True

    def setData(self):
        while True:
            r = random.randint(1, 10)
            ck = False
            for j in range(len(self.memory)):
                if self.memory[j] == r:
                    ck = True
                    break

            if ck == False:
                self.memory.append(r)
                self.memory.append(r)

            if len(self.memory) == 10:
                break

        for _ in range(10):
            self.user.append(0)

    def shuffle(self):

        for _ in range(20):
            r = random.randint(0, 9)
            temp = self.memory[0]
            self.memory[0] = self.memory[r]
            self.memory[r] = temp

    def dataCk(self):
        print("=====", self.cnt + 1, "=====")
        print(self.memory)
        print(self.user)
        print("idx1 : ")
        idx1 = int(input())
        print("idx2 : ")
        idx2 = int(input())
        self.cnt += 1

        # 똑같은지 검사 후 삽입
        if idx1 != idx2 and self.memory[idx1] == self.memory[idx2]:
            self.user[idx1] = self.memory[idx1]
            self.user[idx2] = self.memory[idx2]

    def exitCt(self):
        exitCnt = 0
        for i in range(len(self.user)):
            if self.user[i] != 0:
                exitCnt += 1
        print(exitCnt)
        if exitCnt == len(self.user):
            print("승리 게임을 종료합니다.")
            self.exit = False
        elif self.cnt == 10:
            print("10번의 턴이 종료됩니다.")
            self.exit = False
        else:
            self.exit = True

    def run(self):
        self.setData()
        self.shuffle()
        # run 및 출력
        while self.exit:
            # print(exit)
            self.dataCk()
            self.exitCt()


game = MemoryGame()
# game.setData()
# game.shuffle()
# print(game.memory)
# print(game.user)
game.run()
