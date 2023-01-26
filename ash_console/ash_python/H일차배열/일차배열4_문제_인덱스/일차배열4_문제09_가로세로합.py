'''
	[가로세로합]	
		아래 a 리스트는 한줄 리스트이지만 아래와 같이 사각형으로 놓였다고했을때,  
		[1] a 리스트의 각 가로합은 garo 리스트에 저장 
		[2] a 리스트의 각 세로합은 sero 리스트에 저장
'''	



a = [1, 2, 3, 4,
     5, 6, 7, 8,
     9, 10,11,12]

garo = [0, 0, 0]
sero = [0, 0, 0, 0]

garoIdx = 0 
for i in range(len(a)) :
	garo[garoIdx] += a[i]

	if i % 4 == 3 :
		garoIdx += 1 
print(garo)

seroIdx = 0
for i in range(len(a)) :
	sero[seroIdx] += a[i]
	seroIdx += 1 

	if i % 4 == 3 :
		seroIdx = 0
print(sero) 