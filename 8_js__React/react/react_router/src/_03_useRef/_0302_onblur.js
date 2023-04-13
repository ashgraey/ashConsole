import React from 'react'
/*
    onBlur 로 카멜식을 사용한다.

*/
function _0302_onblur() {

    function changeUpper() {
        let element = document.querySelector("#msg");
        element.value = element.value.toUpperCase();
        element.style.backgroundColor = "yellow";
    }
    return (
        <>
            <input type="text" id="msg" placeholder="소문자로 입력하세요." onBlur={changeUpper}></input>
        </>
    )
}

export default _0302_onblur
