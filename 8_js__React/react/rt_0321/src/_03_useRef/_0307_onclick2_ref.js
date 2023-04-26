import React from 'react'

import {useRef} from 'react'

function _0307_onclick2_ref() {
    const user = useRef(null);

    function checkNotEmpty() {
        let field = user.current;
        if (field.value.length == 0) {
            alert("필드가 비어있네요!");
            field.focus();
        }
    }
    return (
        <>
        이름:    <input type='text' ref={user} ></input>
        <input type='button' onClick={checkNotEmpty} value='확인'></input>
        </>
    )
}

export default _0307_onclick2_ref
