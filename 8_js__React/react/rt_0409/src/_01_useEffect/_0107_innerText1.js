import React from 'react'
import {useEffect} from 'react'
function _0107_innerText1() {

    function init(){
        let element = document.querySelector("#target");
        element.innerText = "";
    }
   
    useEffect(()=>{ 
        init();
    }, []);

    return (
        <>
            <p id="target">텍스트 지우기</p>
        </>
    )
}

export default _0107_innerText1
