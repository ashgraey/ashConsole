import React from 'react'

function _0303_onchange() {
    function selectSub() {
        let value = document.querySelector("#mySelect").value;

        document.querySelector("#selected").innerText = "선택한 과목 : " + value;
    }

  return (
    <>
        <h4>과목을 선택하세요.</h4>
        <select id="mySelect" onChange={selectSub}>
            <option value="html">HTML</option>
            <option value="css">CSS</option>
            <option value="javascript">JavaScript</option>
        </select>
        <p id="selected">선택한 과목 : </p>

    </>
  )
}

export default _0303_onchange
