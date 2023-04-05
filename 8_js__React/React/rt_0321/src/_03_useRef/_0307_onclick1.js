import React from 'react'

function _0307_onclick1() {
    function checkID() {
        let s = document.getElementById("id").value;
        if (s.length < 6) {
            alert("아이디는 6글자 이상이어야 합니다.");
        }
    }

    return (
        <>
            아이디: <input type="text" id="id"></input>
            <button onClick={checkID}>검사</button>
        </>
    )
}

export default _0307_onclick1
