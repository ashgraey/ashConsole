import React from 'react'
import { useEffect } from 'react';
import {useRef} from 'react'

function _0402_추가_append() {

    const list = useRef(null);

    
    function init(){
        let parent = list.current;

        let ul = document.createElement("ul");
        parent.append(ul);

        let li1 = document.createElement("li");
        li1.innerText = "사과";
        
        let li2 = document.createElement("li");
        li2.innerText = "바나나";

        let li3 = document.createElement("li");
        li3.innerText = "딸기";
        
        ul.append(li1, li2, li3);
    }
   
    useEffect(()=>{ 
        init();
    }, []);

  return (
    <>
      <h4>과일 목록</h4>
        <div ref={list}>

        </div>

    </>
  )
}

export default _0402_추가_append
