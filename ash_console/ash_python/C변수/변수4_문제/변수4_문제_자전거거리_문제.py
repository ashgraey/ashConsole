'''
	[문제]
	 	철수는 자전거를 타고 일정한 빠르기로 2시간 동안 37876m를 갔다.
	 	철수가 자전거를 타고 30초 동안 간 거리를 구하시오.
	 	소수점 두 자리까지 구하시오. 
	 	
	[정답] 
		157.82
'''
'''
7200 : 374876 = 30 : ?
7200? = 374876 * 30 
? = 374876 * 30 / 7200
'''
초변환_2시간 = (60 * 60) * 2 
거리 = 37876
_30초거리 = 거리 * 30 / 초변환_2시간
print(round(_30초거리, 2))