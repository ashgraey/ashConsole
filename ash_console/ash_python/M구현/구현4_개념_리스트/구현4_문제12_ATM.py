"""
	[ATM] 

 		[메인메뉴] => "1.회원가입 2.로그인 3.전체회원정보 0.종료"
		[로그인메뉴] => "1.입금 2.송금 3.잔액조회 4.회원탈퇴 0.로그아웃"
	   
"""


class Atm :
    def __init__(self, id, pw, money) :
        self.id = id
        self.pw = pw
        self.money = money
    
    def main(self) :
        print("1.회원가입 2.로그인 3.전체회원정보 0.종료")
        select = int(input())
        if select == 1 :
            self.signUp()
        elif select == 2 :
            self.logIn()
        elif select == 3 :
            self.allMember()
        elif select == 0 :
            self.exit()
    
    def signUp(self) :
        if len(self.id) == 0 :
            print("회원가입을 진행하겠습다.")
            print("ID : ")
            self.id.append(input())
            print("PW : ")
            self.pw.append(input())
            print("MONEY : ")
            self.money.append(input())
        else :
            print("이미 가입된 정보가 있습니다.")
            # 초기화 작업
            self.id = []		
            self.pw = []		
            self.money = []		
	
    def logIn(self) :
        if len(self.id) != 0 :
            print("====== 로그인 ======")
                
		
            


member_id = []
member_pw = []
member_money = []
atm = Atm(member_id, member_pw, member_money)



