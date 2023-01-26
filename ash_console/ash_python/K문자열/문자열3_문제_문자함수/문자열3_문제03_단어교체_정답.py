'''     
    [문제]
        text변수의 내용을 변경하려 한다.
        change변수의 앞부분은 교체할 단어이고, 뒷부분은 삽입할 단어이다.
        text변수의 내용을 변경하시오.
    [정답]
        text = "Life is too short." (변경 전)          
        text = "Life is too long."  (변경 후)
'''

#       012345678901234567
text = "Life is too short."
change = "short,long"

changeList = change.split(",")
print("교체할 단어 =", changeList[0])
print("삽입할 단어 =", changeList[1])
# print(changeList)
# print(len(text)) : 18

check = -1
i = 0
while i < len(text) - len(changeList[0]) + 1: # 18 - 4 + 1 : 15 
    count = 0
    j = 0 
    # 0 1 2 3.. 1 2 3 4... 2 3 4 5...
    # 4회전씩,j가 14일때까지 문자열 하나씩 비교
    while j < len(changeList[0]): # 4
        if text[i + j] == changeList[0][j]:
            count += 1
        else:
            count = 0
        j += 1
        # 연속성 검사
        # count == 4, check = i(인덱스값)
        # i = 12
    if count == len(changeList[0]):
        check = i
        break
    i += 1
# print(check) # check : 12
if check != -1:
    # check = 12
    front = text[:check]
    # print("front : ", front) : life is too long
    back  = text[check + len(changeList[0]):]
    # print("back : ", back) : .
    
    text = ""
    text += front
    text += changeList[1]
    text += back

    print(text)
else:
    print("교체 불가!") # check == -1 / 중복되는 값이 없다면 check의 값은 변하지 않음