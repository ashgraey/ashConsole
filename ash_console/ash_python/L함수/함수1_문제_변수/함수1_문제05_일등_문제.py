'''
    [문제]
        아래 리스트는 시험 점수와 학생 이름이다.
        일등의 학생 이름을 출력해주는 함수를 만드시오.
    [정답]
        1등 학생 = 박민지
'''

def scoreCk(score) :
    max = 0
    maxIdx = 0
    for i in range(len(score)) :
        if max < score[i] :
            max = score[i]
            maxIdx = i
    
    return maxIdx

name = ["이만수", "김철수", "박민지"]  
score = [54, 32, 92]

maxIdx = scoreCk(score)
print("1등 이름 : ", name[maxIdx], "1등 점수 : ", score[maxIdx])