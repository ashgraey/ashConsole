class Ex01:
    def setNum(self):
        self.num = 10
 
    def test1(self):
        tot = 0
        for i in range(1, 6):
            tot += i
        print("1부터 5까지의 합 =", tot)
 
    def test2(self):
        lst = []
        for i in range(3):
            num = int(input("정수 입력 : "))
            lst.append(num)
 
        max_num = 0
        for i in range(3):
            if max_num < lst[i]:
                max_num = lst[i]
        print("최대값 =", max_num)
 
e = Ex01()
 
# 문제 1) 1부터 5까지의 합을 출력하는 메서드
e.test1()
 
# 문제 2) 정수 3개를 입력받아 최대값을 출력하는 메서드
e.test2()