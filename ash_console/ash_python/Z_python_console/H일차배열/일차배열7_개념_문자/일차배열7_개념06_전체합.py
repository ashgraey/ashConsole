"""
    [문제]
        아래 리스트들은 학생들의 데이터이다. 
        각학생들의 국어점수와 영어점수의 합을 sttotal에 저장하시오.
"""
import random

stno = [1001, 1002, 1003, 1004]
stname = ["김철수" , "이만수" , "신정아" , "이영희"]
stkor = [10 , 20 , 30 , 40]
steng = [60 , 80 , 32 , 13]
sttotal = []

for i in range(len(stkor)):
    sttotal.append(stkor[i] + steng[i])

print(sttotal)
