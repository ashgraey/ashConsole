import React from 'react'
import {useRef} from 'react'

function _0307_onclick1_ref() {
    
    const id = useRef(null);

    function checkID() {
        let s = id.current.value;
        if (s.length < 6) {
            alert("아이디는 6글자 이상이어야 합니다.");
        }
    }

    return (
        <>
            아이디: <input type="text" ref={id}></input>
            <button onClick={checkID}>검사</button>
        </>
    )
}

export default _0307_onclick1_ref
