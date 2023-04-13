import React from 'react'
import {useRef} from 'react'

function _0307_onclick5_ref() {
    const number = useRef(null);
	
	function ok(){
		let num = number.current.value;
		//정규식 패턴(숫자만 입력할 수 있도록)
		let num_pattern = /^[0-9]+$/;  //0~9사이의 숫자
		
		// num_pattern.test(num)); 결과는 true 또는 false
		if( !num_pattern.test(num) ){
			alert("숫자만 입력할 수 있습니다.");
		}
	}
    return (
        <>
        숫자 : <input ref={number}></input>
            <input type="button" value="확인" onClick={ok}></input>

        </>
    )
}

export default _0307_onclick5_ref
