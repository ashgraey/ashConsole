function getOnChangeInputId(){
    var memberId = document.getElementById("memberId");
    var msgId = document.getElementById("msgId");
    var userIdCheck = RegExp(/^[A-Za-z0-9_\-]{6,20}$/); 
    if(userIdCheck.test(memberId.value)){
        msgId.innerHTML = "";         
        return true;

    }else{          
        msgId.innerHTML = `<span style='width: 480px; color: #B3130B; font-size: 12px;'>6자리 이상의 영문 혹은 숫자를 조합</span>`;
        memberId.value = "";
        memberId.focus();
        return false;
    }
}

function getOnChangeInputPw(){
    var passwdCheck = RegExp(/^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^*()\-_=+\\\|\[\]{};:\'",.<>\/?]).{8,16}$/);
    var memberPw = document.getElementById("memberPw");
    var msgPw = document.getElementById("msgPw");
    if(passwdCheck.test(memberPw.value)){
        msgPw.innerHTML = "";
        return false;        
    }else{
        msgPw.innerHTML = `<span style='width: 480px; color: #B3130B; font-size: 12px;'>영문 대문자와 소문자, 숫자, 특수문자를 하나 이상 포함하여 8~16자 조합</span>`;
        memberPw.value = "";
        memberPw.focus();
        return true;
    }
}

function getOnChangeInputPwCheck(){
    var memberPw = document.getElementById("memberPw");
    var memberPwCheck = document.getElementById("memberPwCheck");
    var msgPwCheck = document.getElementById("msgPwCheck");
    if(memberPw.value == memberPwCheck.value){
        msgPwCheck.innerHTML = "";
        return false;        
    }else{
        msgPwCheck.innerHTML = `<span style='width: 480px; color: #B3130B; font-size: 12px;'>동일한 비밀번호를 입력해주세요.</span>`;
        memberPwCheck.value = "";
        memberPwCheck.focus();
        return true;
    }
}

function getOnChangeInputName(){
    var nameCheck = RegExp(/^[가-힣]{2,6}$/);

    var memberName = document.getElementById("memberName");
    var msgName = document.getElementById("msgName");
    if(nameCheck.test(memberName.value)){
        msgName.innerHTML = "";
        return false;        
    }else{
        msgName.innerHTML = `<span style='width: 480px; color: #B3130B; font-size: 12px;'>2~6글자의 한글만 입력</span>`;
        memberName.value = "";
        memberName.focus();
        return true;
    }
}

function getOnChangeInputPhone2(){
    var phoneNumberCheck = RegExp(/^01[0179][0-9]{7,8}$/);
    var memberPhone1 = document.getElementById("memberPhone1");
    var memberPhone2 = document.getElementById("memberPhone2");
    var phone = memberPhone1.value + memberPhone2.value;
    var msgPhone = document.getElementById("msgPhone");
    if(phoneNumberCheck.test(phone)){
        msgPhone.innerHTML = "";
        return false;        
    }else{
        msgPhone.innerHTML = `<span style='width: 480px; color: #B3130B; font-size: 12px;'>전화번호 형식에 맞게 입력하세요.</span>`;
        memberPhone1.value = "010";
        memberPhone2.value = "";
        memberPhone2.focus();
        return true;
    }  
}


function getOnChangeInputEmail(){
    var emailCheck = RegExp(/^[A-Za-z0-9_\.\-]+@[A-Za-z0-9\-]+\.[A-Za-z0-9\-]+/);
    var memberEmail = document.getElementById("memberEmail");

    var msgEmail = document.getElementById("msgEmail");
    if(emailCheck.test(memberEmail.value)){
        msgEmail.innerHTML = "";
        return false;        
    }else{
        msgEmail.innerHTML = "<span style='width: 480px; color: #B3130B; font-size: 12px;'>이메일 형식에 맞게 입력하세요.</span>";
        memberEmail.value = "";
        memberEmail.focus();
        return true;
    }          
}



function execDaumPostcode() {
    new daum.Postcode({
    oncomplete: function(data) {	
      // 우편번호와 주소 정보를 해당 필드에 넣는다.
      document.getElementById('memberZipcode').value = data.zonecode; //5자리 새우편번호 사용
      document.getElementById('memberAddress1').value = data.roadAddress;
      document.getElementById('memberAddress2').value = data.jibunAddress;
    }
  }).open();
}

function checkValue() {
    var memberId = document.getElementById("memberId");
    var memberPw = document.getElementById("memberPw");
    var memberPwCheck = document.getElementById("memberPwCheck");
    var memberName = document.getElementById("memberName");
    var memberPhone2 = document.getElementById("memberPhone2");
    var memberZipcode = document.getElementById("memberZipcode");
    var memberAddress1 = document.getElementById("memberAddress1");
    var memberAddress2 = document.getElementById("memberAddress2");
    var memberAddress3 = document.getElementById("memberAddress3");
    var memberEmail = document.getElementById("memberEmail");
    if(!memberId.value) {
        alert("아이디를 입력해주세요.");
        memberId.focus();
        return false;
    }
    
    if(!memberPw.value) {
        alert("비밀번호를 입력해주세요.");
        memberPw.focus();
        return false;
    }

    if(!memberPwCheck.value) {
        alert("비밀번호 재확인을 입력해주세요.");
        memberPwCheck.focus();
        return false;
    }
    
    if(!memberName.value) {
        alert("이름을 입력해주세요.");
        memberName.focus();
        return false;
    }

    if(!memberPhone2.value) {
        alert("전화번호를 입력해주세요.");
        memberPhone2.focus();
        return false;
    }

    if(!memberZipcode.value) {
        alert("우편번호를 입력해주세요.");
        memberZipcode.focus();
        return false;
    }
   
    if(!memberEmail.value) {
        alert("이메일을 입력해주세요.");
        memberEmail.focus();
        return false;
    }
    
    if(!memberAddress1.value) {
        alert("지번주소를 입력해주세요.");
        memberAddress1.focus();
        return false;
    }

    if(!memberAddress2.value) {
        alert("도로명주소를 입력해주세요.");
        memberAddress2.focus();
        return false;
    }
    
    if(!memberAddress3.value) {
        alert("나머지주소를 입력해주세요.");
        memberAddress3.focus();
        return false;
    }


    return true;
}

function join(){

    if(checkValue()){
        
    }
}

function testButton(){
    var memberId = document.getElementById("memberId");
    var memberPw = document.getElementById("memberPw");
    var memberPwCheck = document.getElementById("memberPwCheck");
    var memberName = document.getElementById("memberName");
    var memberPhone1 = document.getElementById("memberPhone1");
    var memberPhone2 = document.getElementById("memberPhone2");
    var memberZipcode = document.getElementById("memberZipcode");
    var memberAddress1 = document.getElementById("memberAddress1");
    var memberAddress2 = document.getElementById("memberAddress2");
    var memberAddress3 = document.getElementById("memberAddress3");
    var memberEmail = document.getElementById("memberEmail");

    memberId.value = "abcd1234";
    memberPw.value = "qwer1234!Q";
    memberPwCheck.value =  memberPw.value;
    memberName.value = "김철수";
    memberPhone1.value = "011";
    memberPhone2.value = "33334444";
    memberZipcode.value = "111-111";
    memberAddress1.value = "김천구";
    memberAddress2.value = "김천동";
    memberAddress3.value = "111-111";
    memberEmail.value = "abc@naver.com";
}   