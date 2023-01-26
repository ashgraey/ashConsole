
class Member:
    number = 0
    name = str()
    score = 0
    
    def printMember(self):
        print(self.number , " : " , self.name , " : " , self.score)
    
class MemberDAO:
    memberList = [] 
    def insertMember(self, member):
        self.memberList.append(member)
        
    def deleteMember(self, index):
        self.memberList.remove(index)
    
    def getMember(self , index):
        return self.memberList[index]
    
    def updateMember(self, index , member):
        self.memberList[index] = member
        
    
    def printAllMember(self):
        for i in range(len(self.memberList)):
            print(self.memberList[i].printMember())
        
    
class MemberController:
    memberDAO = MemberDAO()
    
    def init(self, member_data):     
        token1 = member_data.split("/")
        for i in range(len(token1)):
            token2 = token1[i].split(",")
            member = Member()
            member.number = int(token2[0])
            member.name = token2[1]
            member.score = int(token2[2])
            self.memberDAO.insertMember(member)

    def insert(self):
        pass
    
    def printAll(self):
        self.memberDAO.printAllMember();
            
    
    def run(self):
        while True:
            print("[1]추가 [2]삭제 [3]수정 [4]전체출력 [0]종료")
            select = int(input())
            if select == 1:
                pass
            elif select == 2:
                pass
            elif select == 3:
                pass
            elif select == 4:
                self.printAll()
            elif select == 0:
                break
    
member_data = "1001,김철수,30/1002,이만수,40/1003,이영희,69"

memberController = MemberController()
memberController.init(member_data)
memberController.run()