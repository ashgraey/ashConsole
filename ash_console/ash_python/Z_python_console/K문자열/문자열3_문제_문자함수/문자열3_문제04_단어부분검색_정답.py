'''
    [문제]
        a리스트는 단어들이 모여있는 리스트이다.
        search는 검색하고 싶은 단어이다.
        a리스트에서 해당 단어를 검색해서 출력하시오.
        단, 부분 검색도 되어야한다.
        
    [예시] 
        school, teacher, child
'''


a =["school", "teacher", "child","father", "love"]

search = "ch"

i = 0
while i < len(a):
    j = 0
    while j < len(a[i]) - len(search) + 1:
        count = 0
        k = 0
        while k < len(search):
            if search[k] == a[i][j + k]:
                count += 1
            else:
                count = 0
            if count == len(search):
                print(a[i], end=" ")
                break
            k += 1
        j += 1
    
    i += 1