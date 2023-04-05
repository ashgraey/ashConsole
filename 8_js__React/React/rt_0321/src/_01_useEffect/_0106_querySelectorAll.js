import React from 'react'
import {useEffect} from 'react'

function _0106_querySelectorAll() {
    function init(){
        let list = document.querySelectorAll("p.content");
       
        for(let i=0; i<list.length; i++) {
            // 텍스트 변경
            list[i].innerText = "텍스트 변경";
        }
    }
   

    useEffect(()=>{ 
        init();
    }, []);

  return (
    <>
      
        <p class="content">querySelectorAll() 메서드1</p>
        <p class="content">querySelectorAll() 메서드2</p>

    </>
  )
}

export default _0106_querySelectorAll
