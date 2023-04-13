import React from 'react'

function _0306_onkeydown() {
    function keydownFunction() {
        document.querySelector("#myInput").style.backgroundColor = "red";
    }
    
    function keyupFunction() {
        document.querySelector("#myInput").style.backgroundColor = "green";
    }
    return (
        <>
        <input type="text" id="myInput" onKeyDown={keydownFunction} onKeyUp={keyupFunction}></input>
        </>
    )
}

export default _0306_onkeydown
