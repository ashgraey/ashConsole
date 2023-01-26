"""
	[문제]
		a와  b를 매개변수로 받아서 
		서로 겹치는 값만 배열로 만들어서 반환해주는 함수를 만드시오.
		단, 한번 저장된값은 다시 중복 저장되지않는다.
	[정답]
		[12, 43]
"""
def quiz(a, b):
    c = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]: 
                check = False
                for k in range(len(c)):
                    if c[k] == a[i]:
                        check = True
                if check == False:
                    c.append(a[i]) 
    return c
                
a = [12, 32, 32, 43, 65, 43];
b = [21, 12, 43, 2, 4, 5];

c = quiz(a, b)
print(c)