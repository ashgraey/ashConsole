import React from 'react'
import {useEffect} from 'react'

function _0108_innerHTML1() {
    function init(){
        let element = document.querySelector("#target");
        
        console.log(element.innerText);     // 텍스트 지우기
        console.log(element.innerHTML);     // <span color="red">텍스트</span> 지우기
    }
   
    useEffect(()=>{ 
        init();
    }, []);

    return (
        <>
           <p id="target"><span color="red">텍스트</span> 지우기</p>
        </>
    )
}

export default _0108_innerHTML1
