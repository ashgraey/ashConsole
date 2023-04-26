import React from 'react'
import {useEffect} from 'react'

function _0105_querySelector() {
    function init(){
         // tag명으로 선택
         let element = document.querySelector("h3");
         console.log(element.innerText);
         
         // id명으로 선택
         element = document.querySelector("#main");
         console.log(element.innerText);
         
         // class명으로 선택 : 첫 번째 요소를 반환
         element = document.querySelector(".subject");
         console.log(element.innerText);     // HTML
 
         // 내용 변경
         element.innerText = "Hypertext Markup Language";
    }

    useEffect(()=>{ 
        init();
    }, []);

//     window.onload = function() {
//         init();
//    }
    return (
        <>
            <h3 id="main">학습 과목</h3>
            <ul>
                <li class="subject">HTML</li>
                <li class="subject">CSS</li>
                <li class="subject">JavaScript</li>
            </ul>
        </>
    )
}

export default _0105_querySelector
