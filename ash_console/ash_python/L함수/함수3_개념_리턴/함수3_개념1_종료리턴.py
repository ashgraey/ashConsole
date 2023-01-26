'''
    [함수리턴]
        함수는 리턴을 통해서 함수를 즉시 종료할수있다.

'''


def test():
    a = 10
    print("a : " , a)
    return
    b = 20  # 즉시 종료되기때문에 색깔이 어둡다
    print("b : " , b)


test()