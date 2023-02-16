'''
숫자이동 클래스 + 메서드

[ ] [ ] [ ] [ ] 옷 [ ] [ ] [ ] [ ] [ ] 
1)좌 2)우 3)종료 :
보이는대로 만드시오.

'''


class numMoveGame:

    move = [0, 0, 0, 0, 8, 0, 0, 0, 0]
    position = 0
    dir = ""

    # run환경에 묶어 놓음
    def moveInput(self):
        print("1)좌 2)우 3)종료 :")
        userInput = int(input())

        if userInput == 1:
            self.dir = "좌"
        elif userInput == 2:
            self.dir = "우"
        else:
            exit(1)

    # move_left 와 move_right를 합쳐놓음
    def movePosition(self):
        # 현재 위치 찾기 // set_player
        for i in range(len(self.move)):
            if self.move[i] == 8:
                self.position = i

        # 이동
        tempPosition = self.position
        if self.dir == "좌":
            tempPosition -= 1
        elif self.dir == "우":
            tempPosition += 1

        # 범위 처리
        if tempPosition < 0 or tempPosition >= len(self.move):
            print("범위를 초과하였습니다.")
            print()
            self.exit(1)
        else:
            # move 최신화
            self.move[self.position] = 0
            self.move[tempPosition] = 8
            # print(self.move)

    # print_game
    def gameOutput(self):
        for i in range(len(self.move)):
            if self.move[i] == 8:
                print("옷", end=" ")
            else:
                print("[ ]", end=" ")
        print()

    def run(self):
        exit = self.exit(0)
        while exit:
            self.moveInput()
            self.movePosition()
            self.gameOutput()

    def exit(self, ck):

        if ck == 0:
            return True
        else:
            return False


game = numMoveGame()
game.run()
