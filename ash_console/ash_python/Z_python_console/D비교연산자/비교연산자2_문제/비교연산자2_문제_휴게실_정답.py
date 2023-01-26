'''
   [문제]
      철수는 고속버스를 타고 여행을 떠나려 한다.
      출발시간까지 1시간 여유가 있다.
      고속버스 역과 상점을 시속 3km로 걸어서 왕복하고,
      10분 동안 물건을 쇼핑하려고 한다.
      역에서 1.3km 떨어진 상점을 다녀올 수 있을지 구하시오.
   
      위 식을 표현하고, 풀이 과정을 주석으로 작성하시오.
'''
'''
    거리 = 속력 * 시간
    시간 = 거리 / 속력

    편도_거리 * 2 / 철수_분속 + 쇼핑_시간 <= 여유_시간
'''

여유_시간 = 60

철수_분속 = 3 / 60
쇼핑_시간 = 10
편도_거리 = 1.3
print(편도_거리 * 2 / 철수_분속 + 쇼핑_시간 <= 여유_시간)
