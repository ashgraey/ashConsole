"""
    [문제]
        stno는 학생번호리스트이다.
        stname 은 학생이름리스트이다.
        두리스트는 한세트이다. 
        랜덤으로 학생번호를 선택하고 해당번호의 학생데이터를 삭제하시오.
    [예시]
        r = 1002

        stno = [1001, 1003, 1004]
        stname = ["김철수" , "신정아" , "이영희"]
"""
import random


stno = [1001, 1002, 1003, 1004]
stname = ["김철수" , "이만수" , "신정아" , "이영희"]


r = random.randint(1001, 1004)
print("r : " , r)
for i in range(len(stno)):
    if stno[i] == r:
        del(stno[i])
        del(stname[i])
        break

print(stno)
print(stname)
