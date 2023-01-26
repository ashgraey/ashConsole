'''
[문제]
    0에서 100사이의 랜덤 숫자를 시험 점수로 저장한다.
    시험점수에 해당하는 학점을 출력하시오.
    아래는 점수표이다.
    100~91 이면 A학점,
    90~81  이면 B학점,
    80이하는 "재시험"
    
    단, 만점이거나, A학점과 B학점의 일의 자리가 8점이상이면 + 기호를 추가하시오.
    [예] 
        100 => A+
        88 ==> B+
        82 ==> B
        23 ==> 재시험
'''
'''
    랜덤을 테스트할 때는 원하는 값이 나올 때까지 무한반복을 하게된다.
    아래와 같이 일정 숫자가 나오도록 폭을 조정하면 테스트하기 쉽다. 
'''
import random

# 100(A+) / 98(A+) / 91(A) / 88(B+) / 82(B) / 51(재시험)

r = random.randint(0, 5)
if r == 0:
    score = 100
if r == 1:
    score = 98
if r == 2:
    score = 91
if r == 3:
    score = 88
if r == 4:
    score = 82
if r == 5:
    score = 51

#score = random.randint(0, 100)
print("성적 =", score)

if 98 <= score and score <= 100:
    print("A+")
if 91 <= score and score <= 97:
    print("A")
if 88 <= score and score <= 90:
    print("B+")
if 81 <= score and score <= 87:
    print("B")
if score <= 80:
    print("재시험")

print("------------------------------")

one = score % 10        # 일의 자리 구하기
if score == 100:
    print("A+")
if 91 <= score and score <= 99:
    if one >= 8:
        print("A+")   
    if one < 8:
        print("A")   
if 81 <= score and score <= 90:
    if one >= 8:
        print("B+")   
    if one < 8:
        print("B")
if 0 <= score and score <= 80:
    print("재시험")