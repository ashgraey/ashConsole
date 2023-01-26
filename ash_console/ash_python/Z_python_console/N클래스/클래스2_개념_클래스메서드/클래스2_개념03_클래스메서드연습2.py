class Ex02:
     
    def test1(self, x, y):
        tot = 0
        for i in range(x, y+1):
            tot += i
        print("%d부터 %d의 합 = %d" % (x, y, tot))
 
    def test2(self, lst):
        max_num = 0
        for i in range(len(lst)):
            if max_num < lst[i]:
                max_num = lst[i]
        print("최대값 =", max_num)
 
    def test3(self, lst, x, y):
        temp = lst[x]
        lst[x] = lst[y]
        lst[y] = temp
 
e = Ex02()
 
# 문제 1) x부터 y까지의 합을 출력하는 메서드
x = 1
y = 10
e.test1(x, y)
 
# 문제 2) lst를 전달받아 최대값을 출력하는 메서드
lst = [87, 100, 35, 12, 46]
e.test2(lst)
 
# 문제 3) lst를 전달받아 인덱스 2개를 입력받고, 해당 위치의 값을 교체하는 메서드 
idx1 = 1
idx2 = 4
e.test3(lst, idx1, idx2)
print(lst)