import React from 'react'

function _0307_onclick5() {
    function ok(){
		let num = document.getElementById("num").value;
		//정규식 패턴(숫자만 입력할 수 있도록)
		let num_pattern = /^[0-9]+$/;  //0~9사이의 숫자
		
		// num_pattern.test(num)); 결과는 true 또는 false
		if( !num_pattern.test(num) ){
			alert("숫자만 입력할 수 있습니다.");
		}
	}
    return (
        <>
        숫자 : <input id="num"></input>
            <input type="button" value="확인" onClick={ok}></input>

        </>
    )
}

export default _0307_onclick5
