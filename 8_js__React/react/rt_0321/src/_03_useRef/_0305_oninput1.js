import React from 'react'

function _0305_oninput1() {
    function changeText() {
        // alert(document.querySelector("#name").value);
        document.querySelector("#result").innerText = document.querySelector("#name").value;
    }
    return (
        <>
            <input type="text" id="name" placeholder="이름을 입력하세요." onInput={changeText}></input>
            <p id="result"></p>

        </>
    )
}

export default _0305_oninput1
