import React from 'react'
import {useEffect} from 'react'

function _0301_이벤트추가2() {
    function init(){
        let btn = document.querySelector("#btn");
        btn.onclick = function() {
            alert("클릭!");
        }
    }
   
    useEffect(()=>{ 
        init();
    }, []);



    return (
        <>
            <button id="btn">버튼</button>

        </>
    )
}

export default _0301_이벤트추가2
