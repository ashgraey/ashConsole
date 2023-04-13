import React from 'react'
import { useEffect } from 'react';
import {useRef} from 'react'

/*
   [개념] appendChild vs append
        (1) 공통점 : 부모 태그에 자식 태그를 추가하는 메서드
        (2) 차이점
            * append
                한번에 여러 자식 태그를 추가할 수 있고,
                문자열도 추가할 수 있다.
*/
function _0401_추가_appendChild() {

    const list = useRef(null);

        
    
    function init(){
        let parent = list.current;

        let ul = document.createElement("ul");
        parent.appendChild(ul);

        let li1 = document.createElement("li");
        li1.innerText = "사과";
        ul.appendChild(li1);
        
        let li2 = document.createElement("li");
        li2.innerText = "바나나";
        ul.appendChild(li2);
        
        let li3 = document.createElement("li");
        li3.innerText = "딸기";
        ul.appendChild(li3);

    }
   
    useEffect(()=>{ 
        init();
    }, []);


    return (
        <>
            <h4>과일 목록1</h4>
            <div ref={list}>

            </div>
            
        </>
    )
}

export default _0401_추가_appendChild
