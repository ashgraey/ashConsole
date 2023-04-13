import React from 'react'
import {useEffect} from 'react'

/*
    리엑트에서 속성변경

    기본의 css 문법을 사용하면 에러가 발생한다.
    [예] 
        style="display: none"

    [리엑트 스타일 문법 ]
        style = {}  안에 json 문법으로 {key : value , key : value , ... } 를 사용해야한다. 
    [예] 
        style={{display:"none"}}
*/

function _0207_textContent() {

    function init(){       
        let element = document.querySelector("#content");
        console.log(element.innerText);       // 
        console.log(element.innerHTML);       // <span style="display: none">숨겨진 텍스트</span> 
        console.log(element.textContent);     // 숨겨진 텍스트
    }
   
    useEffect(()=>{ 
        init();
    }, []);

    return (
        <>
        <div id="content">

                {/* <span style="display: none">숨겨진 텍스트</span> */}
                <span style={{display:"none"}}>
                숨겨진 텍스트
                </span> 

            </div>
        </>
    )
}

export default _0207_textContent
