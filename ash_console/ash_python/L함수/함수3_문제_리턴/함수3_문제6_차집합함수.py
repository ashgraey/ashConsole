"""
	[문제]
		a와  b를 매개변수로 받아서 
		서로 겹치지않는 값만 배열로 만들어서 반환해주는 함수를 만드시오.
		단, 한번저장된값은 중복하여저장되지않는다.
	[정답]
        [12, 32, 43, 65, 21, 2, 4, 5]
"""
def quiz(a, b):
    c = []
    for i in range(len(a)):
        check = False
        for j in range(len(c)):
            if a[i] == c[j]:
                check = True
        if check == False:
            c.append(a[i])
    for i in range(len(b)):
        check = False
        for j in range(len(c)):
            if b[i] == c[j]:
                check = True
        if check == False:
            c.append(b[i])
    return c
a = [12, 32, 32, 43, 65, 43];
b = [21, 12, 43, 2, 4, 5];

c = quiz(a, b)
print(c)