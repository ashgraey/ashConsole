"""
	* # 타자연습 게임[2단계]
	* 1. 문제를 섞는다.(shuffle)
	* 2. 순서대로 문제를 출제하고, 문제를 다 맞추면 게임 종료
	* 3. 단 문제를 출제할 때, 단어의 랜덤한 위치 한 곳만 *로 출력
	* 예)
	* 문제 : mys*l
	* 입력 : mysql	<--- 정답을 맞추면, 다음 문제 제시
	* 문제 : *sp
	* 입력 : jsp

"""
import random
# class를 활용하여 풀어보자


class StarTypingData:

    def __init__(self, a):
        self.a = a

        # print(a)

    def setDataShuffle(self):
        # 문제를 섞는다. 셔플
        for _ in range(10):
            r = random.randint(0, len(self.a) - 1)
            temp = self.a[0]
            self.a[0] = self.a[r]
            self.a[r] = temp

    def setDataStar(self):
        tempList = []
        for i in range(len(self.a)):
            r = random.randint(0, len(self.a[i]) - 1)

            temp = ""
            for j in range(len(self.a[i])):
                temp += self.a[i][j]
                if r == j:
                    temp += "*"
            tempList.append(temp)

        for i in range(len(tempList)):
            self.a[i] = tempList[i]

        print(self.a)


class StarTypingGame(StarTypingData):
    def __init__(self):
        StarTypingData.__init__(self)

    def out(self):
        print(self.b)


a = ["mysql", "jsp", "javascript", "python", "java"]

data = StarTypingData(a)
data.setDataStar()
