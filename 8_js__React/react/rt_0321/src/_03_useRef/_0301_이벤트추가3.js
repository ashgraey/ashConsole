import React from 'react'
import {useEffect} from 'react'

function _0301_이벤트추가3() {
    function downEvent() {
        let btn = document.querySelector("#btn");
        btn.innerText = "마우스 버튼을 눌렀다.";
    }
    function upEvent() {
        let btn = document.querySelector("#btn");
        btn.innerText = "그리고 마우스 버튼에서 손을 뗐다.";
    }
    function init(){

        let btn = document.querySelector("#btn");
        
        btn.addEventListener("mousedown", downEvent);
        btn.addEventListener("mouseup", upEvent);
    }


    useEffect(()=>{ 
        init();
    }, []);


    return (
        <>
            <button id="btn">버튼마우스</button>
        </>
    )
}

export default _0301_이벤트추가3
