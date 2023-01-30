'''
    [문제]
        arr리스트의 값을 체크하여
        짝수의 개수를 출력하는 함수를 만드시오.
    [정답]
        2
'''


def evenCnt(arr) :
    cnt = 0 
    for i in range(len(arr)) :
        if arr[i] % 2 == 0 :
            cnt += 1 

    return cnt

arr = [2, 45, 1, 12]
result = evenCnt(arr)
print("evenCnt : ", result)