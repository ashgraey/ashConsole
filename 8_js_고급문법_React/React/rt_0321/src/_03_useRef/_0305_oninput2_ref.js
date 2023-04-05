import React from 'react'
import {useRef} from 'react'
function _0305_oninput2_ref() {

  const range = useRef(null);
  const result = useRef(null);

    function changeRange() {
        let value = range.current.value;
        result.current.innerText = value;
    }
  return (
    <>
        <input type="range" ref={range} onInput={changeRange}></input>
        <p  ref={result}></p>

    </>
  )
}

export default _0305_oninput2_ref
