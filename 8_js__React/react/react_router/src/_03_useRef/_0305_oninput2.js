import React from 'react'

function _0305_oninput2() {
    function changeRange() {
        let value = document.querySelector("#range").value;
        document.querySelector("#result").innerText = value;
    }
  return (
    <>
        <input type="range" id="range" onInput={changeRange}></input>
        <p id="result"></p>

    </>
  )
}

export default _0305_oninput2
