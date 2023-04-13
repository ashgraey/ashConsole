import React from 'react'
import {useRef} from 'react'

function _0303_onchange_ref() {

    const mySelect = useRef(null);
    const selected = useRef(null);

    function selectSub() {

      selected.current.innerText = "선택한 과목 : " + mySelect.current.value;

    }

    return (
      <>
          <h4>과목을 선택하세요.</h4>
          <select ref={mySelect}  onChange={selectSub} >
              <option value="html">HTML</option>
              <option value="css">CSS</option>
              <option value="javascript">JavaScript</option>
          </select>
          <p ref={selected} >선택한 과목 : </p>

      </>
    )
}

export default _0303_onchange_ref
