"""
	[회원가입] 
		메뉴 => [1.회원가입 2.정보수정 3.회원탈퇴 4.전체출력 0. 종료]
		
 	   	1. 회원가입 = > ID가 있는지 확인하고 없으면 회원가입 한다.
	   	2. 정보수정 = > ID가 있는지 확인하고 있으면 수정한다. 수정은 비밀번호나 이름만 수정할수있다.
	   	3. 삭제 = >  ID가 있는지 확인하고 있으면 삭제
		4. 전체출력 = > 회원 전체 정보를 출력한다. 
"""


class SignUpPg :
	def __init__(self, id, pw, name) :
		self.id = id
		self.pw = pw
		self.name = name
		self.user = -1

	def menu(self) :
		print("[1.회원가입 2. 정보수정 3.회원탈퇴 4.전체출력 0.종료]")
		self.user = int(input())

		if self.user == 1 :
			self.signUp()
		elif self.user == 2 :
			self.update()
		elif self.user == 3 :
			self.memberOut()
		elif self.user == 4 :
			self.allPrint()
		elif self.user == 0 :
			self.exit()

	def exit(self) :
		if self.user == 0 :
			return False 
		return True
	
	def allPrint(self) :
		# if len(self.id) != 0 :
		print("id : ", self.id, "pw : ", self.pw, "name : ", self.name)

	
	def signUp(self) :
		if len(self.id) == 0 :
			print("회원가입을 진행합니다.")
			print("id : ")
			signUpId = input()
			self.id.append(signUpId)
			print("pw : ")
			signUpPw = input()
			self.pw.append(signUpPw)
			print("name : ")
			signUpName = input()
			self.name.append(signUpName)
		else :
			print("등록된 회원 정보가 있습니다.")
			self.run()
	
	def memberOut(self) :
		self.id = []
		self.pw = []
		self.name = []

	def update(self) : 
		if len(self.id) != 0 :
			print("1. pw 2. 이름")
			updateUser = int(input())

			if updateUser == 1 :
				print("변경할 비밀번호를 입력하세요.")
				self.pw = []
				updatePw = input()
				self.pw.append(updatePw)
			if updateUser == 2 :
				print("변경할 이름을 입력하세요.")
				self.name = []
				updateName = input()
				self.name.append(updateName)


	def run(self) :
		
		while True :
			self.menu()

			if self.exit() == False :
				break
		
			# break 
		 


member_id = []
member_pw = []
member_name = []
signUpPg = SignUpPg(member_id, member_pw, member_name)
signUpPg.run()
