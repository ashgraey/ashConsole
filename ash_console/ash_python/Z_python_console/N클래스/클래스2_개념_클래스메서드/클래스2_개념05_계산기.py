# 계산기 프로그램
 
class Calc:
 
    def add(self, x, y):
        return x + y
 
    def sub(self, x, y):
        return x - y
 
    def mul(self, x, y):
        return x * y
 
    def div(self, x, y):
        return x / y
 
    def showInfo(self, x, y):
        print("%d + %d = %d" % (x, y, self.add(x, y)))
        print("%d - %d = %d" % (x, y, self.sub(x, y)))
        print("%d * %d = %d" % (x, y, self.mul(x, y)))
        if y != 0:
            print("%d / %d = %.1f" % (x, y, self.div(x, y)))
        else:
            print("0으로 나눌 수 없습니다.")
 
c = Calc()
c.showInfo(5, 3)