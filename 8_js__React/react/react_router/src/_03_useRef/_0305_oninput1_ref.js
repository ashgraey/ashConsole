import React from 'react'
import {useRef} from 'react'

function _0305_oninput1_ref() {

    const name = useRef(null);
    const result = useRef(null);

    function changeText() {

        result.current.innerText = name.current.value;
    }
    return (
        <>
            <input type="text" ref={name} placeholder="이름을 입력하세요." onInput={changeText}></input>
            <p ref={result}></p>

        </>
    )
}

export default _0305_oninput1_ref
