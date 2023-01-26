# 숫자이동 : 클래스 + 메서드

class Game:

    move = [0, 0, 0, 0, 8, 0, 0, 0, 0, 0]
    player = 0                            # 캐릭터의 위치

    def set_player(self):
        for i in range(len(self.move)):
            if self.move[i] == 8:
                self.player = i

    def print_game(self):
        for i in range(len(self.move)):
            if self.move[i] == 0:
                print("[ ]", end=" ")
            else:
                print("옷", end=" ")
        print()

    def move_left(self):
        if self.player - 1 >= 0:
            self.move[self.player] = 0
            self.player -= 1
            self.move[self.player] = 8
        else:
            print("더 이상 이동할 수 없습니다.")

    def move_right(self):
        if self.player + 1 < len(self.move):
            self.move[self.player] = 0
            self.player += 1
            self.move[self.player] = 8
        else:
            print("더 이상 이동할 수 없습니다.")

    def run(self):
        self.set_player()
        
        while True:
            self.print_game()

            number = int(input("1)좌 2)우 3)종료 : "))
            
            if number == 1:
                self.move_left()
            elif number == 2:
                self.move_right()
            elif number == 3:
                break
#----------------------------------------------------------
g = Game()
g.run()