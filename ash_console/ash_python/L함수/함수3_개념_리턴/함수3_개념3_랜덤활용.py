'''
    [직접만든랜덤활용하기]
        [1] 중복숫자금지
            랜덤숫자 (1~size)를 size개수만큼 추가한 리스트를 만드시오. 
            단, 중복숫자는 없어야한다.
'''
import time # 시간 관련 함수를 사용할수있다. 
def myRandum(min , max):
    num = time.time() # # 현재시간을 1/1000 초로 가져온다. (밀리세컨드)
    num = num * 1103515245 + 12345 # 굉장히 큰수를 곱하고 더해준다.
    num = num / 65536 # 적당히큰수로 나눠준다.
    num = int(num % 32768) # 적당히큰수로 나머지를 한다. 
    num = num % max  + 1 # 최종적으로 원하는 범위 설정을 한다. 
    return num
    
def ranList(size):
    a = []
    i = 0
    while i < size:
        r = myRandum(1 , size)
        check = False
        for j in range(len(a)):
            if r == a[j]:
                check = True
                break
        if check == False:
            a.append(r)
            i += 1
    return a
a = ranList(10)
print(a)