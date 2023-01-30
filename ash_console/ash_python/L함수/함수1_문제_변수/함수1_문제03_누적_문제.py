'''
    [문제]
        1~10 사이의 숫자를 랜덤으로 2개 저장하고,
        작은 숫자부터 큰 숫자까지의 합을 출력하는 함수를 만드시오.
    [예시]
        5, 3 ==> 3 + 4 + 5 = 12
        2, 6 ==> 2 + 3 + 4 + 5 + 6 = 20
'''
import random

def numTot(min, max) :

    print("min : ", min, "max : ", max)
    
    tot = 0 
    i = min 
    while i <= max :
  
        tot += i
        if i == max :
            print(i, end = " = ")
        else : 
            print(i, end = " + ")
        
        i += 1 
    
    return tot
    
r1 = random.randint(1, 10)
r2 = random.randint(1, 10)

max = 0 
min = 0
if r1 > r2 :
    max = r1
    min = r2
else :
    max = r2
    min = r1 

result = numTot(min, max)
print("numTotal : ", result)