import React from 'react'
import {useEffect} from 'react'

function _0104_tag() {
    function init(){
        // 태그 선택
        let element = document.getElementsByTagName("li")[1];
        console.log(element.innerText);     // CSS

        // 내용 변경
        element.innerText = "Cascading Style Sheets";
    }

    useEffect(()=>{ 
        init();
    }, []);


//     window.onload = function() {
//         init();
//    }
  return (
    <>
        <h3>학습 과목</h3>
        <ul>
            <li>HTML</li>
            <li>CSS</li>
            <li>JavaScript</li>
        </ul>
    </>
  )
}

export default _0104_tag
