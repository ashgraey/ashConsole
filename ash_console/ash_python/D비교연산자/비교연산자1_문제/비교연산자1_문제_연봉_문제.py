'''
	[문제]
		작년 내 연봉은 970원이다. 
        올해는 11퍼센트 인상되었다. 
		올해 우리 회사 평균 월급은 91원이다. 
		올해의 내 연봉이 올해의 우리 회사 평균 연봉보다 큰지 확인하시오.

		위 내용을 비교연산자로 표현하시오.
    [정답]
        False
'''
작년연봉 = 970
올해인상금액 = 970 * 0.11  
회사평균월급 = 91
올해연봉 = 작년연봉 + 올해인상금액
회사연봉 = 회사평균월급 * 12
print(올해연봉)
print(회사연봉)
print(올해연봉 > 회사연봉)