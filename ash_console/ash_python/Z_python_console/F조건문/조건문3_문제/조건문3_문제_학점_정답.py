'''
    [문제]
        0에서 100 사이의 랜덤 숫자를 시험 점수로 저장한다.
        시험점수에 해당하는 학점을 출력하시오.
        아래는 점수표이다.
        100~91 이면 A학점,
        90~81  이면 B학점,
        80 이하는 "재시험"
        
        단, 만점이거나, A 학점과 B 학점의 일의 자리가 8점 이상이면 + 기호를 추가하시오.
        [예] 
            100 => A+
            88 ==> B+
            82 ==> B
            23 ==> 재시험
'''

import random

score = random.randint(0, 100)
print(score)

if 98 <= score and score <= 100:
    print("A+")
if 91 <= score and score < 98:
    print("A")
if 88 <= score and score <= 90:
    print("B+")
if 81 <= score and score < 88:
    print("B")
if score <= 80:
    print("재시험")
