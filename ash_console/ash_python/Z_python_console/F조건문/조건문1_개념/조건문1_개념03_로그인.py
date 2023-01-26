'''
[회원가입과 로그인] 
	[1] 가입된 아이디와 비번으로 로그인 시 입력한 아이디와 비밀번호를 비교한다.
	[2] "로그인 성공" 또는 "로그인 실패"를 출력하시오.
'''

join_id = "qwer1234"
join_pw = "1234qwer"
		
log_id = "qwer1234"
log_pw = "1234qwer"

    
if join_id == log_id and join_pw == log_pw:
    print("로그인 성공")

if join_id != log_id or join_pw != log_pw:
    print("로그인 실패")