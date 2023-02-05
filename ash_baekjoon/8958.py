'''
문제 8958//
"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.

"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

input//
첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 문자열은 O와 X만으로 이루어져 있다.

output//
각 테스트 케이스마다 점수를 출력한다.

'''

size = int(input())

for i in range(size):
    ox = list(str(input()))

    score = 0
    cnt = 0
    for j in range(len(ox)):
        if ox[j] == "O":
            cnt += 1
            score += cnt

        if ox[j] == "X":
            cnt = 0

    print(score)


# # 정답 코드
# n = int(input())
# for _ in range(n):
#     ox_list = list(input())
#     score = 0
#     sum_score = 0  # 새로운 ox리스트를 입력 받으면 점수 합계를 리셋한다.
#     for ox in ox_list:
#         if ox == 'O':
#             score += 1  # 'O'가 연속되면 점수가 1점씩 커진다.
#             sum_score += score  # sum_score = sum_score + score
#         else:
#             score = 0
#     print(sum_score)


# size = int(input())
# for _ in range(size):

#     ox_list = list(input())
#     print(ox_list)

#     score = 0
#     total_score = 0
#     for ox in ox_list:
#         if ox == 'O':
#             score += 1
#             total_score += score
#             print(score)

#         else:
#             score = 0
#     print(total_score)
