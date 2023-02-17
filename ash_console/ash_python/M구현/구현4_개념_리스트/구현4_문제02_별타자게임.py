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


class StarTypingGame:

    def __init__(self, a) :
        self.a = a
        self.cnt = 0
        self.end = True 

    def setDataShuffle(self):
        tempList = self.setDataStar()
        # 문제를 섞는다. 셔플
        for _ in range(10):
            r = random.randint(0, len(self.a) - 1)
            temp1 = self.a[0]
            self.a[0] = self.a[r]
            self.a[r] = temp1

            temp2 = tempList[0]
            tempList[0] = tempList[r]
            tempList[r] = temp2

            return tempList


    def setDataStar(self):
        tempList = []
        for i in range(len(self.a)):
            r = random.randint(0, len(self.a[i]) - 1)

            temp = ""
            for j in range(len(self.a[i])):
                
                if r == j:
                    temp += "*"
                else :
                    temp += self.a[i][j]

            tempList.append(temp)

        return tempList

    def run(self):
        tempList = self.setDataShuffle()
        print(tempList)
        print(self.a)
        self.cnt = 0
        while self.end :
            print("문제", self.cnt + 1, ":", tempList[self.cnt])
            user = input()

            ck = False
            for i in range(len(self.a[self.cnt])) :
                if len(user) == len(self.a[self.cnt]) :
                    if user[i] != self.a[self.cnt][i] :
                        ck = True
                        break
                else :
                    ck = True
                    break

            if ck == False :
                self.cnt += 1 

            if len(tempList) - 1 == self.cnt :
                print("게임종료")
                self.end = False

                 
a = ["mysql", "jsp", "javascript", "python", "java"]

data = StarTypingGame(a)
data.run()
