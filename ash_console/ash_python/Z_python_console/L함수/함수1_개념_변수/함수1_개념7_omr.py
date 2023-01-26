'''
    [문제]
        철수는 수학 시험을 치렀다. 시험 점수를 채점하시오.
        omr리스트는 정답이다.
        me리스트에 랜덤숫자(1~4) 를 5개 저장 후,
        omr과 비교하여 아래와 같이 출력하는 함수를 만드시오. 
    [예시]
        [1,4,3,2,1]
        [2,4,4,3,1]
        [x,o,x,x,o]
'''
import random

def omrCheck(omr, me):
    ox = []
    for i in range(len(omr)):
        if omr[i] == me[i]:
            ox.append("o")
        else:
            ox.append("x")
    print("omr =", omr)
    print("me =", me)
    print("정오표 =", ox)

omr = [1,4,3,2,1]
me = []

for i in range(len(omr)):
    r = random.randint(1, 4)
    me.append(r)
omrCheck(omr, me)