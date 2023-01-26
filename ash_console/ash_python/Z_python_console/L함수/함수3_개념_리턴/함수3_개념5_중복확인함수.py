'''
    [중복확인 함수]
        아래 리스트에 랜덤숫자(1~10)을 다섯개 추가한다. 
        단 이미 저장된숫자는 저장하지않는다. 

'''
import random

def duplicateCheck(a , r):
    for i in range(len(a)):
        if r == a[i]:
            return True
    return False
def appendNumber(a):
    i = 0
    while i < 5:
        r = random.randint(1, 10)
        if duplicateCheck(a , r) == False:
            a.append(r)
            i += 1
            
a = [1,2,3]
appendNumber(a)
print(a)