"""
    [문제]
        철수는 타자연습 게임을 만들기 위해 단어들을 선정했다. 
        문제를 단순히 내면 재미없기때문에 두글자는 단어대신 * 로 출력하려고한다. 
        * 위치는 랜덤이고,   별은 반두시 두개가되도록 각단어들을 만들어서 
        새로운리스트로 반환하는 함수를 만드시오.

        [예시]
            h*m*
            *eac*
            spr**ng
            fr*nt*nd
            java*cr*pt
 """
import random
def getStarWord(word):
    sample = ""
    while True:
        r1 = random.randint(0, len(word)-1)
        r2 = random.randint(0, len(word)-1)
        if r1 != r2:
            for i in range(len(word)):
                if i == r1 or i == r2:
                    sample += "*"
                else:
                    sample += word[i]
            break
    return sample

def getChangeWord(wordList):
    sampleList = []
    for i in range(len(wordList)):
        word = wordList[i]
        starWord = getStarWord(word)
        sampleList.append(starWord)
    print(sampleList)


wordList = ["html" , "react" , "spring" , "frontend" , "javascript"]

getChangeWord(wordList)