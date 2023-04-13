import React from 'react'

function _0307_onclick2() {
    function checkNotEmpty() {
        let field = document.getElementById('user');
        if (field.value.length == 0) {
            alert("필드가 비어있네요!");
            field.focus();
        }
    }
    return (
        <>
        이름:    <input type='text' id='user' ></input>
        <input type='button' onClick={checkNotEmpty} value='확인'></input>
        </>
    )
}

export default _0307_onclick2
