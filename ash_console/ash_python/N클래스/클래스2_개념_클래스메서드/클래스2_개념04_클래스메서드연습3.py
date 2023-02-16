class Ex03:

    def test1(self, lst):
        cnt = 0
        for i in range(len(lst)):
            if lst[i] % 4 == 0:
                cnt += 1
        return cnt

    def test2(self, lst):
        cnt = self.test1(lst)  # return cnt = 3
        # 배열을 이런식으로도 생성이 가능하네? cnt = 3, temp = [0] * 3 == temp = [0, 0, 0]
        temp = [0] * cnt
        j = 0
        for i in range(len(lst)):
            if lst[i] % 4 == 0:
                temp[j] = lst[i]
                j += 1
        return temp


e = Ex03()

lst = [87, 12, 21, 56, 100]

# 문제 1) 4의 배수의 개수를 리턴해주는 메서드
cnt = e.test1(lst)
print("4의 배수의 개수 =", cnt)

# 문제 2) 4의 배수만 리스트 타입으로 리턴해주는 메서드
temp = e.test2(lst)
print(temp)

# temp = [0] * 5
# print(temp)
