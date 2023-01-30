"""
	[문제]
		sum 리스트에 랜덤으로 1~10 사이의숫자  3개를 저장하는 함수를 만든다.
		단, 3개의 숫자의 합은 반드시 20이여야하며, 똑같은 숫자는 없어야한다. 
		위치는 상관없다. 
 
	[예시1]
 		1,10,9 (o)
	[예시2] 
 		8,8,4 (x)
	
"""
import random
def total20(sumList) :
    while True :
        r = random.randint(1, 10)
        ck = False
        
        j = 0 
        while j < len(sumList) :
            if sumList[j] == r :
                ck = True
                break 
            j += 1 
    
        if ck == False :
            sumList.append(r)
    
        if len(sumList) == 3 :
            total = 0
            ck = False
            for i in range(len(sumList)) :
                total += sumList[i]
            
                if total == 20 : 
                    ck = True
            if ck == True : 
                break 
            else :
                sumList = []
    return sumList

sumList = []
a = total20(sumList)
print(a)