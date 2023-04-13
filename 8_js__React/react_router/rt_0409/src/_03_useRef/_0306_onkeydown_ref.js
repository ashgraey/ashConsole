import React from 'react'
import {useRef} from 'react'

function _0306_onkeydown_ref() {
    const myInput = useRef(null);
  
    function keydownFunction() {
        myInput.current.style.backgroundColor = "red";
    }
    
    function keyupFunction() {
        myInput.current.style.backgroundColor = "green";
    }
    return (
        <>
        <input type="text" ref={myInput} onKeyDown={keydownFunction} onKeyUp={keyupFunction}></input>
        </>
    )
}

export default _0306_onkeydown_ref
