import React from 'react'
import {useRef} from 'react'

function _0307_onclick4_ref() {

    const fruits = useRef(null);
    const result = useRef(null);

    function checkSelection( msg) {
        let elem = fruits.current;
        if (elem.value == 0) {
            alert(msg);
            result.current.innerText = msg;
            elem.focus();
        } else {
            result.current.innerText = "선택하신 과일은 " + elem.children[elem.value].innerText + "입니다.";
        }
    }

    return (
        <>
        과일선택 
            <select ref= {fruits}>
                <option value="0">선택하세요</option>
                <option value="1">사과</option>
                <option value="2">배</option>
                <option value="3">바나나</option>
            </select>
            <input type='button' onClick={(e) =>{checkSelection( '하나를 선택하여야 합니다.')}} value='확인' ></input>
            
            <p ref={result}></p>

        </>
    )
}

export default _0307_onclick4_ref
