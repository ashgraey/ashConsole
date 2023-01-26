'''
	[문제]
        아래 game 리스트는 철수와 민수가 서로 끝말잇기를 한 결과이다. 
        끝말잇기가 틀린 단어를 출력하시오.     
        자전거 - 거미 : 정답
        거미 - 미용실 : 정답
        미용실 - 실업자 : 정답
        자석 : 서유기 : 오답
    [결과]
        서유기
    [힌트]
        아래 첫글자와 마지막글자 출력하는법을 참고하시오.
        text = "안녕하세요"
        print("첫글자 :", text[0])
        print("마지막글자 :", text[-1])
'''

game = ["자전거", "거미", "미용실", "실업자", "자석", "서유기", "기러기"]
wrongWord = ""
for i in range(len(game) - 1):
    if game[i][-1] == game[i + 1][0]:
        print(game[i], "-", game[i + 1], ": 정답")
    else:
        print(game[i], "-", game[i + 1], ": 오답")
        wrongWord = game[i + 1]

print("틀린 단어 =", wrongWord)

	
