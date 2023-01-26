'''
[회원가입과 로그인] 
	[1] 가입된 아이디와 비번으로 로그인 시 입력한 아이디와 비밀번호를 비교한다.
	[2] "로그인 성공" 또는 "로그인 실패"를 출력하시오.
	[3] 중첩if 문을 사용하면 아래와 같이 아이디가 틀렸습니다. 비밀번호가 틀렸습니다. 
		세부적으로 표현하기 쉽다. 
'''

join_id = "qwer1234"
join_pw = "1234qwer"
		
log_id = "qwer1234"
log_pw = "1234qwer"

if join_id == log_id: 
	if join_pw == log_pw:
		print("로그인성공")
	if join_pw != log_pw:
		print("비밀번호가 틀립니다.")

if join_id != log_id:
	print("아이디가 틀립니다.")