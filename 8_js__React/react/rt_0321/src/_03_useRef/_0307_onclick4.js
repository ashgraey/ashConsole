import React from 'react'

function _0307_onclick4() {
    function checkSelection( msg) {
        let elem = document.getElementById('fruits');
        if (elem.value == 0) {
            alert(msg);
            document.querySelector("#result").innerText = msg;
            elem.focus();
        } else {
            document.querySelector("#result").innerText = "선택하신 과일은 " + elem.children[elem.value].innerText + "입니다.";
        }
    }

    return (
        <>
        과일선택 
            <select id="fruits">
                <option value="0">선택하세요</option>
                <option value="1">사과</option>
                <option value="2">배</option>
                <option value="3">바나나</option>
            </select>
            <input type='button' onClick={(e) =>{checkSelection( '하나를 선택하여야 합니다.')}} value='확인' ></input>
            
            <p id="result"></p>

        </>
    )
}

export default _0307_onclick4
