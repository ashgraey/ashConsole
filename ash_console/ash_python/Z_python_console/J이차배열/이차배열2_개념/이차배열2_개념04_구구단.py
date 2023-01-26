'''
    [문제]
        game리스트의 가로 한 줄은 구구단 앞의 숫자와 뒤의 숫자를 의미한다.
        앞의 숫자와 뒤의 숫자의 곱을 result리스트에 추가하시오.
    [예시]
        4 * 6 : result = [24]
        3 * 6 : result = [24, 18]
        ...
    [정답]
        result = [24, 18, 24, 81, 6, 42]
'''
game = [
    [4,6],
    [3,6],
    [8,3],
    [9,9],
    [2,3],
    [6,7]
]

result = []

for i in range(len(game)):
    z = game[i][0] * game[i][1]
    print(game[i][0], "*", game[i][1], "=", z)
    result.append(z)

print(result)