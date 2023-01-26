'''
    [랜덤만들기]
        지금까지 사용했던 랜덤함수를 직접만들어보자.

'''
import time
def myRandum(min , max):
    num = time.time() # 현재시간을 1/1000 초로 가져온다. (밀리세컨드)
    print(num)
    num = num * 1103515245 + 12345 # 굉장히 큰수를 곱하고 더해준다.
    num = num / 65536 # 적당히큰수로 나눠준다.
    num = int(num % 32768) # 적당히큰수로 나머지를 한다. 
    num = num % max  + 1 # 최종적으로 원하는 범위 설정을 한다. 
    return num

r = myRandum(1, 5)
print(r , end=" ")
    