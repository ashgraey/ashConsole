import React from 'react'

function _0307_onclick3() {
    function checkLength(min, max) {
        let elem = document.getElementById('idcheck')
        console.log(elem)
        let s = elem.value;
        if (max < s.length || s.length < min) {
            alert(min + " 문자와 " + max + " 문자 사이로 입력해주세요!");
            elem.value = "";
            elem.focus();
        }
    }
    
    return (
        <>
        아이디(6-8 문자): <input type='text' id='idcheck' autoFocus ></input>
        <input type='button'  onClick={(e) =>{checkLength(6,8)}} value='확인' ></input>
        </>
    )
}

export default _0307_onclick3
