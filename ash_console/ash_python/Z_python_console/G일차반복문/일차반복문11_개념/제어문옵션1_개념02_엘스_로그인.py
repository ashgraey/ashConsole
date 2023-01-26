'''
  	[회원가입과 로그인] 	
		1. 가입된 아이디와 비번과 로그인시 입력한 아이디와 비밀번호를 비교한다.
		2. "로그인" 또는 "로그인실패" 를 출력하세요. 
'''

join_id = "qwer1234"
join_pw = "1234qwer"
		
log_id = "qwer1234"
log_pw = "1234qwer"


if join_id == log_id and join_pw == log_pw:
    print("로그인")
else:
    print("로그인실패")