"""
	[문제]
		아래 문제수만큼 함수를 만들어서 풀어보시오.

		문제 1) 각층별 관리비 합 출력
		정답 1) 4400, 7100, 5400		
	
		문제 2) 관리비가 가장 많이 나온 집, 적게 나온 집 출력
		정답 2) 가장 많이 나온 집(201), 가장 적게 나온 집(303)		

		문제 3) 관리비 많이 나온순서대로 관리비와 호수 출력 
		정답 3) 정렬해서 출력한다.
"""

def quiz1(aptList , payList , totalList):
	
	for i in range(len(payList)):
		total = 0
		for j in range(len(payList[i])):
			total += payList[i][j]
		totalList.append(total)
	
def quiz2(aptList , payList , minmaxapt):
	max = payList[0][0]
	min = payList[0][0]
	maxapt = 0
	minapt = 0
	for i in range(len(payList)):
		for j in range(len(payList[i])):
			if max < payList[i][j]:
				max = payList[i][j]
				maxapt = aptList[i][j]

			if min > payList[i][j]:
				min = payList[i][j]
				minapt = aptList[i][j]
	minmaxapt["min"] = minapt
	minmaxapt["max"] = maxapt

def quiz3(aptList , payList , sortApt , sortPay):
	

	for i in range(len(aptList)):
		for j in range(len(aptList[i])):
			sortApt.append(aptList[i][j])
			sortPay.append(payList[i][j])
			

	for i in range(len(sortPay)):
		for j in range(len(sortPay)):
			if(sortPay[i] > sortPay[j]):
				temp = sortPay[i]
				sortPay[i] = sortPay[j]
				sortPay[j] = temp

				temp = sortApt[i]
				sortApt[i] = sortApt[j]
				sortApt[j] = temp

aptList = [
		[101, 102, 103],	
		[201, 202, 203],	
		[301, 302, 303]
			
	]
payList = [
		[1000, 2100, 1300],	
		[4100, 2000, 1000],	
		[3000, 1600,  800]
	]

totalList = []
quiz1(aptList , payList , totalList)
print(totalList)

minmaxapt = {"max" : 0 , "min" : 0}
quiz2(aptList , payList , minmaxapt)
print(minmaxapt)

sortPay = []
sortApt = []
quiz3(aptList , payList , sortApt , sortPay)
print(sortApt)
print(sortPay)