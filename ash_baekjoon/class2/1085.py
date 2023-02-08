'''
문제 직사각형에서 탈출//
한수는 지금 (x, y)에 있다. 
직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다. 
직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

input//
첫째 줄에 x, y, w, h가 주어진다.

output//
첫째 줄에 문제의 정답을 출력한다.
'''

x, y, w, h = map(int, input().split())
# print("y : ", x, "x : ", y, "w : ", w - x, "h : ", h - y)
print(min(x, y, w-x, h-y))  # min최솟값 구하는 함수

# https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FIdFI1%2FbtreXp6BMJJ%2FOHJ3HdR43RnPo8En8TZtX1%2Fimg.png
# 1. (x, y) 좌표를 직사각형 내에서 임의의로 지정했을 떄, 경계면까지의 거리를 나타낸 그림이다.
# 2.각각의 길이는 위의 그림과 같다
# 2-1) 왼쪽 아래 꼭지점이 (0, 0) 이기 때문에 y축에서 (x, y)의 거리는 x
# 2-2) x축에서 (x, y)의 거리는 y
# 2-3) 오른쪽 위 꼭짓점 (w, h)의 x축과 평행한 경계면 까지의 거리는 h-y
# 2-4) (w, h)의 y축과 평행한 경계면 까지의 거리는 w-x
# 3. 각각의 길이를 구하고, min함수를 통해 최소값을 구하여 출력한다.
