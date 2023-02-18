"""
	* # 타자연습 게임[1단계]
	* 1. 문제를 섞는다.(shuffle)
	* 2. 순서대로 문제를 출제하고, 문제를 다 맞추면 게임 종료
	* 예)
	* 문제 : mysql
	* 입력 : mydb
	* 문제 : mysql
	* 입력 : mysql	<--- 정답을 맞추면, 다음 문제 제시
	* 문제 : jsp

"""
import random


class typingGame:

    a = ["mysql", "jsp", "javascript", "python", "java"]
    cnt = 0

    def setShuffle(self):
        for _ in range(10):
            r = random.randint(0, len(self.a) - 1)
            temp = self.a[0]
            self.a[0] = self.a[r]
            self.a[r] = temp
        # print(self.a)

    def checkCt(self, user, list):
        ck = False
        for i in range(len(list)):
            if list[i] != user[i]:
                ck = True
                break
        if ck == False:
            return True
        else:
            return False

    def run(self):
        self.setShuffle()
        i = 0
        while True:
            print("문제", i + 1, " : ", self.a[i])
            user = input()
            if (self.checkCt(user, self.a[i])):
                i += 1

            if i == len(self.a):
                break


game = typingGame()
game.run()
