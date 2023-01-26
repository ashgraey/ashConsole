'''     
    [문제]
        text변수의 내용을 변경하려 한다.
        change변수의 앞부분은 교체할 단어이고, 뒷부분은 삽입할 단어이다.
        text변수의 내용을 변경하시오.
    [정답]
        text = "Life is too short." (변경 전)          
        text = "Life is too long."  (변경 후)
'''


text = "Life is too short."
change = "short,long"

changeList = change.split(",")
print("교체할 단어 =", changeList[0])
print("삽입할 단어 =", changeList[1])

check = -1
i = 0
while i < len(text) - len(changeList[0]) + 1:
    count = 0
    j = 0 
    while j < len(changeList[0]):
        if text[i + j] == changeList[0][j]:
            count += 1
        else:
            count = 0
        j += 1
    if count == len(changeList[0]):
        check = i
        break
    i += 1

if check != -1:
    front = text[:check]
    back  = text[check + len(changeList[0]):]
    
    text = ""
    text += front
    text += changeList[1]
    text += back

    print(text)
else:
    print("교체 불가!")