'''
	[문제] 
	  	어느 도시에 전체 인구가 400000명이다. 
	    그중 나이가 19세 이하 인구는 35%이다.
	    그리고 나이가 40세 이상 인구는 25%이다.	      
	 	위 도시의 19세 이하 인구에서 40세 이상 인구수를 뺀 인구수를 구하시오.		 
	[정답] 
		40000
'''

'''
    100% : 400000명 = 1% : n명
    100n = 400000
    n = 400000 / 100
'''

전체_인구수 = 400000

십구세이하_퍼센트 = 35
사십세이상_퍼센트 = 25

일퍼센트_인구수 = 전체_인구수 / 100

십구세이하_인구수 = 일퍼센트_인구수 * 십구세이하_퍼센트
사십세이상_인구수 = 일퍼센트_인구수 * 사십세이상_퍼센트

차이 = 십구세이하_인구수 - 사십세이상_인구수
print(차이)
