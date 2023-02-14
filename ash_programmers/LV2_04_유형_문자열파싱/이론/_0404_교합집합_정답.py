
"""
    다음 a와 b의 교집합 갯수와 합집합 개수를 구하시오.

    교집합 은 1,4,3  이렇게 3개이고 
    합집합 은 1,1,2,3,4,5,6,7 이렇게 8개이다. 

"""
a = [1,4,3,7]
b = [1,1,2,3,4,5,6]

c1 = len(a) + len(b)
c2 = 0
for i , v in enumerate (a):
    if v in b:
        index = b.index(v)
        del(b[index])
        c2 += 1

c1 = c1 - c2
print("교집합 : " , c2)
print("합집합 : " , c1)