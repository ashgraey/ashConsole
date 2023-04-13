import React from 'react'
import {useRef} from 'react'

/*
    

*/
function _0302_onblur_ref() {
    //const inputEl = React.useRef(null); // import 하지않았을경우는React.을 앞에붙여서 사용할수있다.
    const msg = useRef(null);
   

    function changeUpper() {
        msg.current.value = msg.current.value.toUpperCase();
        msg.current.style.backgroundColor = "yellow";
    }
    return (
        <>
            <input ref={msg} type="text" placeholder="소문자로 입력하세요." onBlur={changeUpper}></input>
        </>
    )
}

export default _0302_onblur_ref
