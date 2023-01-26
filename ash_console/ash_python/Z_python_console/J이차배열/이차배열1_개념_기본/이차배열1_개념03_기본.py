'''
    [문제]
        c리스트에 1~9를 순차적으로 저장하고, 출력하시오.
    [정답]
        c :  [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
'''
c = []

for i in range(3):
    c.append([0,0,0])
print("c : " , c)

num = 1
for i in range(len(c)):
    for j in range(len(c[i])):
        c[i][j] = num
        num += 1
print("c : " , c)