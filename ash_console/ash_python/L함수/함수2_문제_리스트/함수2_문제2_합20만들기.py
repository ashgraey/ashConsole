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
def make20(sum):
    count = 0;
    total = 0
    while(True):     
        if count == 3 and total == 20 :
            break
        elif count == 3 and total != 20:
            count = 0
            total = 0        
            
        r = random.randint(1, 10)
        check = False
        for i in range(len(sum)):
            if r == sum[i]:
                check = True
                break
        if check == False:
            sum[count] = r
            total += r		
            count += 1
sum = [0,0,0]
make20(sum)
print(sum)

